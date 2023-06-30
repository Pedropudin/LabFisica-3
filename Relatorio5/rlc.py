import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

FREQUENCIA = "Frequência(kHz)"
PICO1 = "Pico(V)"
PICO2 = "PicoR(V)"

FACTORX = 1e3
FACTORY = 1/2
C = 0.1 * (1e-6)
R = 100
L = 46 * (1e-3)

def toFLoat(a, fator):
    return list(float(b)*fator for b in a)

def smooth( y, box_pts):
        box = np.ones(box_pts)/box_pts
        y_smooth = np.convolve(y, box, mode='same')
        return y_smooth

def drawError(x,y,errorPerc=1,errorOffset=0):
    yErrorMin = y*(1-errorPerc) - errorOffset
    yErrorMax = y*(1+errorPerc) + errorOffset
    plt.fill_between(x, yErrorMin, yErrorMax, color='#f07269', alpha=0.4)


def rlc_ressonancia(f, v0):
    w = f * 2 * np.pi
    G = R**2
    H = ((1/(w*C)) - (L*w))**2
    F = G + H
    return (v0*R)/np.sqrt(F)


file = pd.read_csv('data/ressonancia_rlc.csv', sep=",")
x = np.sort(toFLoat(list(file[FREQUENCIA]),FACTORX))
y1 = toFLoat(list(file[PICO1]),FACTORY)
y2 = toFLoat(list(file[PICO2]),FACTORY)

popt, _ = curve_fit(rlc_ressonancia, x, y2)
v0 = popt

print(np.sqrt(1/(L*C) + ((R/(2*L))**2)))

xdata = np.arange(min(x), max(x), 1)
ydata = rlc_ressonancia(xdata, v0)
plt.plot(xdata, ydata, 'r-', label='data')

plt.plot(xdata, ydata, 'r-',  label='data')
plt.xlabel("Frequência (Hz)")
plt.ylabel("Amplitude (V)")

drawError(xdata,ydata,0.4)

plt.grid()

plt.scatter(x, y2)
plt.show()