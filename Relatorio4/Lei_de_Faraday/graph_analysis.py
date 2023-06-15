from scipy.optimize import curve_fit
from matplotlib import pyplot
import numpy as np
import pandas as pd

TEMPO = "Segundos(s)"
CANAL1 = "Canal 1(V)"
CANAL2 = "Canal 2(V)"


file = pd.read_csv('data/1152.csv', sep=",")

x = list(float(b) for b in list(file[TEMPO]))
y = list(float(b) for b in list(file[CANAL1]))

pyplot.plot(x, y, 'r-', label='data')
pyplot.xlabel("Tempo (s)")
pyplot.ylabel("Potencial (V)")

pyplot.scatter(x, y)
pyplot.show()


