import numpy as np
import pandas as pd


TEMPO = "Segundos(s)"
CANAL1 = "Canal 1(V)"
CANAL2 = "Canal 2(V)"
FACTORX=1e-2
FACTORY=1e-3
HALL = 0.0036955570480154084
MU_0 = 4*np.pi*1e-7

class Solenoide:
    def __init__(self, r, l, n):
        self.r = r
        self.l = l
        self.n = n

    def indutancia(self):
        A = np.pi*(self.r**2)
        return MU_0*A*self.n/self.l

class GraphController:
    def __init__(self):
        self.bobina_menor = Solenoide(8.10*1e-3,59.90*1e-3,2100)
        self.bobina_maior = Solenoide(34.50*1e-3,14.90*1e-2,760)

    def readChannels(self, path):
        file = pd.read_csv(path, sep=",")
        self.x = GraphController.toFLoat(list(file[TEMPO]),FACTORX)
        self.y1 = GraphController.toFLoat(list(file[CANAL1]),FACTORY)
        self.y2 = GraphController.toFLoat(list(file[CANAL2]),FACTORY)

    @staticmethod
    def toFLoat(a, fator):
        return list(float(b)*fator for b in a)
    
    def ddpInduzidaHall(self):
        arr = [0]
        R = 10
        y = self.channel_1_data()
        L = self.bobina_maior.indutancia()

        for i in range(len(y)-1):
            if ((self.x[i+1]-self.x[i])!=0):
                arr.append((L/R)*(y[i+1]-y[i])/(self.x[i+1]-self.x[i]))
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



