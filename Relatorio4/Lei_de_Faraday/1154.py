from graph_analysis import *
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

controller = GraphController()
# controller.readChannels('data/1154_freq_1.csv')
# FREQ = 2000/FACTORX
# controller.readChannels('data/1154_freq_2.csv')
# FREQ = 1500/FACTORX
# controller.readChannels('data/1154_freq_3.csv')
# FREQ = 500/FACTORX
controller.readChannels('data/1154.csv')
FREQ = 1000/FACTORX

def ddp(t,L):
    w = 2 * np.pi * FREQ
    i0 = np.nanmax(GraphController.smooth(controller.channel_1_data(),35))/10
    return w*np.sin(w*t)*L*i0

def indutanciaMutua():
    t = controller.time_data()

    y1 = controller.channel_1_data()
    y2 = controller.channel_2_data()
    
    popt, _ = curve_fit(ddp, t, y1)
    L = popt[0]

    y3 = ddp(np.array(t),L)
    
    plt.plot(t, y1, 'b-')
    plt.plot(t, y2, 'r-')
    plt.plot(t, y3, 'g-')
    plt.xlabel("Tempo (s)")
    plt.ylabel("Potencial (V)")

    plt.grid()

    plt.show()

indutanciaMutua()