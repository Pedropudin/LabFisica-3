import numpy as np
import pandas as pd


TEMPO = "Tempo(s)"
CANAL1 = "Canal 1(V)"
CANAL2 = "Canal 2(V)"
FACTORX=1
FACTORY=1
MU_0 = 4*np.pi*1e-7

class GraphController:

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

    @staticmethod
    def drawError(x,y,plot,errorPerc=1,errorOffset=0):
        yErrorMin = y*(1-errorPerc) - errorOffset
        yErrorMax = y*(1+errorPerc) + errorOffset
        plot.fill_between(x, yErrorMin, yErrorMax, color='#f07269', alpha=0.4)

    @staticmethod
    def drawErrorDifference(x,y,y_real,plot):
        diff = y-y_real
        plot.fill_between(x, y-diff, y+diff, color='#f07269', alpha=0.4)

    def drawErrorLists(x,y,error,plot):
        mError = GraphController.modList(error)
        plot.fill_between(x, y-mError, y+mError, color='#f07269', alpha=0.4)


    def readChannels(self, path):
        file = pd.read_csv(path, sep=",")
        self.x = GraphController.toFLoat(list(file[TEMPO]),FACTORX)
        self.y1 = GraphController.toFLoat(list(file[CANAL1]),FACTORY)

        if (CANAL2 in file.head(0)):
            self.y2 = GraphController.toFLoat(list(file[CANAL2]),FACTORY)

    @staticmethod
    def mod(a):
        return a if a>0 else a*-1

    def modList(a):
        return list(map(GraphController.mod,a))

    @staticmethod
    def toFLoat(a, fator):
        return list(float(b)*fator for b in a)
    
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



