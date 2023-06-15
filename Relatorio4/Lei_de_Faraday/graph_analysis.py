from scipy.optimize import curve_fit
from matplotlib import pyplot
import numpy as np
import pandas as pd

file = pd.read_csv('data/1152.csv', sep=",")

x = list(float(b) for b in list(file["second"]))
y = list(float(b) for b in list(file["Volt1"]))

pyplot.plot(x, y, 'r-', label='data')
pyplot.xlabel("Tempo (s)")
pyplot.ylabel("Potencial (V)")

pyplot.scatter(x, y)
pyplot.show()


