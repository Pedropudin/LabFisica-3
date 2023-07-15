import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from graph_analysis import *
from graph_analysis import GraphController as gc


# controller = gc()
# controller.readChannels('Data2/scope_9.csv')

# x = controller.time_data()
# y1 = controller.channel_1_data()
# y2 = controller.channel_2_data()

# plt.xlabel(TEMPO)
# plt.ylabel("volts")

# plt.grid()

# plt.plot(x, y1, 'r-',  label='data')
# plt.plot(x, y2, 'b-',  label='data')
# plt.show()

file = pd.read_csv('Data3/passaBaixa.csv', sep=",")
x = GraphController.toFLoat(list(file["frequencia(Hz)"]),1)
y1 = GraphController.toFLoat(list(file["V0(V)"]),1)
y2 = GraphController.toFLoat(list(file["Vr(V)"]),1)
y3 = GraphController.toFLoat(list(file["Vc(V)"]),1)

plt.xlabel("Frequência (Hz)")
plt.ylabel("volts")

plt.grid()

plt.plot(x, y1, 'r-',  label='data')
plt.plot(x, y2, 'b-',  label='data')
plt.plot(x, y3, 'g-',  label='data')
plt.show()