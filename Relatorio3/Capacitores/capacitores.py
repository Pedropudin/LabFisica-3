from scipy.optimize import curve_fit
from matplotlib import pyplot
import numpy as np
import pandas as pd

def rcEquation(t, r, c, v0):
    tau = r*c
    return  v0 * np.exp(-(t/tau))

file = pd.read_csv('data/capacitor_1.csv', usecols= ['DDP'])

y = list(float(b) for b in list(file["DDP"]))
x = list(range(0,len(y)))

popt, _ = curve_fit(rcEquation, x, y)
r, c, v0 = popt

xdata = np.linspace(x[0],x[-1],2000)
ydata = rcEquation(xdata, r, c, y[0])
pyplot.plot(xdata, ydata, 'r-', label='data')

pyplot.xlabel("Tempo (s)")
pyplot.ylabel("Potencial (V)")

pyplot.scatter(x, y)
pyplot.show()