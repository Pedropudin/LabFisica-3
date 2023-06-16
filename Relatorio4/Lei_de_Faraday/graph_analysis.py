import numpy as np
import pandas as pd


TEMPO = "Segundos(s)"
CANAL1 = "Canal 1(V)"
CANAL2 = "Canal 2(V)"
FACTORX=1e-2
FACTORY=1e-3
HALL = 270.59520
HALL_ERROR = 0.00004
MU_0 = 4*np.pi*1e-7

class Solenoide:
    def __init__(self, r, l, n, dr, dl):
        self.r = r
        self.l = l
        self.n = n
        self.dr = dr
        self.dl = dl

    def indutancia(self):
        A = np.pi*(self.r**2)
        return MU_0*A*self.n/self.l

class GraphController:
    def __init__(self):
        self.bobina_menor = Solenoide(8.10*1e-3,59.90*1e-3,2100, 0.05*1e-3, 0.05*1e-3)
        self.bobina_maior = Solenoide(34.50*1e-3,14.90*1e-2,760, 0.05*1e-3, 0.01*1e-2)

    def indutanciaMutua(self):
        n2 = self.bobina_maior.n * (self.bobina_maior.l/self.bobina_menor.l)
        n1 = self.bobina_menor.n
        l = self.bobina_menor.l
        r = self.bobina_menor.r
        return MU_0*n2*n1*np.pi*(r**2)/l

        return 

    @staticmethod
    def period(y,x):
        choosen = y[len(y)//2]
        initial = x[len(y)//2]
        final = 0
        for i in range((len(y)//2)+1, (len(y)//2)-1):
            if (y[i]==choosen):
                final = x[i]
                break

        return final - initial

    def readChannels(self, path):
        file = pd.read_csv(path, sep=",")
        self.x = GraphController.toFLoat(list(file[TEMPO]),FACTORX)
        self.y1 = GraphController.toFLoat(list(file[CANAL1]),FACTORY)
        self.y2 = GraphController.toFLoat(list(file[CANAL2]),FACTORY)

    @staticmethod
    def toFLoat(a, fator):
        return list(float(b)*fator for b in a)
    
    def ddpHall(self):
        R = 10
        y = self.channel_1_data()
        return MU_0*self.bobina_maior.n*np.array(y)*HALL/(R*self.bobina_maior.l)

    def ddpHallError(self):
        R = 10
        er = (self.bobina_maior.dl*HALL + HALL_ERROR*self.bobina_maior.l)/(self.bobina_maior.l**2)
        return MU_0*self.bobina_maior.n*(er)/R

    def ddpInduzida(self):
        arr = [0]
        R = 10
        y = self.channel_1_data()
        x = self.time_data()
        L = self.bobina_maior.indutancia()

        for i in range(len(y)-1):
            if ((x[i+1]-x[i])!=0):
                arr.append((-L/R)*(y[i+1]-y[i])/(x[i+1]-x[i]))
            else:
                arr.append(0)
        return arr
    
    def time_data(self):
        return self.x

    def channel_1_data(self):
        return self.y1

    def channel_2_data(self):
        return self.y2

    @staticmethod
    def mediaProporcao(l1,l2):
        s = 0
        j = 0
        for i in range(len(l1)):
            if (l2[i]!=0):
                a = l1[i]/l2[i]
                if GraphController.isNaN(a):
                    j+=1
                else:
                    s += a
        return s/(len(l1)-j)

    @staticmethod
    def smooth( y, box_pts):
        box = np.ones(box_pts)/box_pts
        y_smooth = np.convolve(y, box, mode='same')
        return y_smooth

    @staticmethod
    def isNaN(num):
        return num != num



