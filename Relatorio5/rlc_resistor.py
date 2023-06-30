import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from graph_analysis import *
from graph_analysis import GraphController as gc


C = 0.1 * (1e-6)
RESISTORES = [48,280,1090,2860,4660]
rr = np.empty(len(RESISTORES))
# rr.fill(15+470)
# RESISTORES+= rr
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
    R = RESISTORES[0]
    gamma = R/(2*L)
    w = rlc_freq(R,L,C)
    return x0*np.exp(-gamma*t)*np.sin(w*t - delta)

def getFitting(function, x, y):
    popt, _ = curve_fit(function, x, y)
    x0, delta = popt
    return x0, delta

def removeEndAndStart(l, K):
    a = list(l)
    del a[:K]
    for i in range(K):
        a.pop()
        
    return a

controller = gc()

# controller.readChannels('data/scope_7.csv')
# controller.readChannels('data/scope_8.csv')
# controller.readChannels('data/scope_9.csv')
# controller.readChannels('data/scope_10.csv')
controller.readChannels('data/scope_11.csv')

x = controller.time_data()
y = controller.channel_1_data()
# y = gc.smooth(controller.channel_1_data(),10)
# y = removeEndAndStart(y,100)
# x = removeEndAndStart(x,100)

x0, delta = getFitting(rlc_previsao, x, y)

xdata = np.linspace(x[0],x[-1],len(x))
# ydata = rlc_previsao(xdata, x0, delta)

# plt.plot(xdata, ydata+11, 'r-', label='data')

plt.xlabel(TEMPO)
plt.ylabel(CANAL1)

plt.grid()

plt.plot(x, y, 'b-',  label='data')
plt.show()