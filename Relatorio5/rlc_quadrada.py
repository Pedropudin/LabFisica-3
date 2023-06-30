import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from graph_analysis import *
from graph_analysis import GraphController as gc


C = 0.1 * (1e-6)
R = 15
L = 46 * (1e-3)


def rlc_error(t,x0,R,L,C):
    dt = 0.0001
    gamma = R/(2*L)
    w = rlc_freq(R,L,C)
    a = - gamma*(np.exp(-gamma*t))*np.sin(w*t)
    b = np.sin(w*t)*w*np.exp(-gamma*t)
    return x0 * (a+b) * dt

def rlc_freq(R,L,C):
    gamma = R/(2*L)
    w0 = 1/np.sqrt(L*C)
    return np.sqrt((w0**2) - (gamma**2))

def rlc_periodo(R,L,C):
    return (2 * np.pi)/rlc_freq(R,L,C)

def rlc_tau(x,y):
    i = len(x)//2
    f = len(x)//2 + 100
    return (x[f]-x[i])/(np.log(gc.mod(y[i]/y[f])))

def rlc_previsao(t, x0, delta):
    gamma = R/(2*L)
    w = rlc_freq(R,L,C)
    return x0*np.exp(-gamma*t)*np.sin(w*t - delta) + 11


controller = gc()
controller.readChannels('data/scope_1.csv')
# controller.readChannels('data/scope_2.csv')
# controller.readChannels('data/scope_3.csv')


x = controller.time_data()
y = controller.channel_1_data()

popt, _ = curve_fit(rlc_previsao, x, y)
x0, delta = popt

xdata = np.linspace(x[0],x[-1],len(y))
ydata = rlc_previsao(xdata, x0, delta)

plt.plot(xdata, ydata, 'r-', label='data')

plt.xlabel(TEMPO)
plt.ylabel(CANAL1)

plt.grid()


print("Tau: " + str(rlc_tau(x,y)))
print("Periodo: " + str(rlc_periodo(R,L,C)))


gc.drawErrorDifference(xdata, ydata, y, plt)

plt.plot(x, y, 'b-',  label='data')
plt.show()