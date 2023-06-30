import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from graph_analysis import GraphController as gc

FREQUENCIA = "Frequência(kHz)"
PICO1 = "Pico(V)"
PICO2 = "PicoR(V)"

FACTORX = 1e3
FACTORY = 1/2
C = 0.1 * (1e-6)
R = 100 + 15
L = 46 * (1e-3)

def rlc_ressonancia(f):
    w = f * 2 * np.pi
    G = R**2
    H = ((1/(w*C)) - (L*w))**2
    F = G + H
    return (R)/np.sqrt(F)

file = pd.read_csv('data/ressonancia_rlc_100.csv', sep=",")
x = np.sort(gc.toFLoat(list(file[FREQUENCIA]),FACTORX))
vp = gc.toFLoat(list(file[PICO1]),FACTORY)
vr = gc.toFLoat(list(file[PICO2]),FACTORY)
y = np.array(vr)/np.array(vp)

w0 = np.sqrt(1/(L*C) - ((R/(2*L))**2))
f0 = w0/(2*np.pi)
xdata = np.arange(min(x), max(x), 1)
ydata = rlc_ressonancia(xdata)
plt.plot(xdata, ydata, 'r-', label='data')

p = xdata

y_reta = np.empty(len(ydata))
y_reta.fill(max(ydata)/(np.sqrt(2)))

x_p = []
a0 = max(ydata)/(np.sqrt(2))
for i in range(len(ydata)):
    if rlc_ressonancia(xdata[i]) <= a0+0.001 and rlc_ressonancia(xdata[i]) >= a0-0.001:
        x_p.append(xdata[i])

x1_reta = np.empty(len(xdata))
x1_reta.fill(x_p[0])

x2_reta = np.empty(len(xdata))
x2_reta.fill(x_p[1])

print("Fator Q: " + str(f0/(x_p[1]-x_p[0])))
print("Frequencia ressonancia: " + str(f0))

plt.plot(xdata, y_reta, linestyle='dashdot')
plt.plot(x1_reta, ydata, linestyle='dashdot')
plt.plot(x2_reta, ydata, linestyle='dashdot')
plt.xlabel("Frequência (Hz)")
plt.ylabel("Vr/Vp (adimensional)")

gc.drawError(xdata,ydata,plt,0.4)

plt.grid()

plt.scatter(x, y)
plt.show()