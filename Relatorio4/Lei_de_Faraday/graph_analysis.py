from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter


TEMPO = "Segundos(s)"
CANAL1 = "Canal 1(V)"
CANAL2 = "Canal 2(V)"
FACTORX=1e-2
FACTORY=1e-3
HALL = 0.0036955570480154084

l_menor = 59.90*1e-3
r_menor = 8.10*1e-3
n_menor = 2100

l_maior = 14.90*1e-2
r_maior = 34.50*1e-3
n_maior = 760

def indutancia(r, L, N):
    mi0 = 4*np.pi*1e-7
    return mi0*N*np.pi*(r**2)/L

def toFLoat(a, fator):
    return list(float(b)*fator for b in a)

def ddpInduzidaHall(L,y,x):
    arr = [0]
    R = 10
    for i in range(len(y)-1):
        if ((x[i+1]-x[i])!=0):
            arr.append(-(L/R)*(y[i+1]-y[i])/(x[i+1]-x[i]))
        else:
            arr.append(0)
    return arr

def mediaProporcao(l1,l2):
    s = 0
    j = 0
    for i in range(len(l1)):
        if (l2[i]!=0):
            a = l1[i]/l2[i]
            if isNaN(a):
                j+=1
            else:
                s += a
    return s/(len(l1)-j)

def isNaN(num):
    return num != num

Lmaior = indutancia(r_maior, l_maior, n_maior)
Lmenor = indutancia(r_menor, l_menor, n_menor)

file = pd.read_csv('data/1152.csv', sep=",")

x = toFLoat(list(file[TEMPO]),FACTORX)
y1 = toFLoat(list(file[CANAL1]),FACTORY)
y2 = toFLoat(list(file[CANAL2]),FACTORY)
y3 = ddpInduzidaHall(Lmaior, savgol_filter(y1, 51, 3),x)

plt.plot(x, y1, 'b-')
plt.plot(x, y2, 'r-')
plt.plot(x, y3, 'g-')
plt.xlabel("Tempo (s)")
plt.ylabel("Potencial (V)")

plt.grid()

# pyplot.scatter(x, y1, c="b")
# pyplot.scatter(x, y2, c="r")
plt.show()


