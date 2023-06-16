from graph_analysis import *
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

controller = GraphController()

controller.readChannels('data/1152.csv')

t = controller.time_data()
y1 = controller.channel_1_data()
y2 = controller.channel_2_data()
y3 = GraphController.smooth(controller.ddpInduzidaHall(), 35)


plt.plot(t, y1, 'b-')
plt.plot(t, y2, 'r-')
plt.plot(t, y3, 'g-')
plt.xlabel("Tempo (s)")
plt.ylabel("Potencial (V)")

plt.grid()

plt.show()
