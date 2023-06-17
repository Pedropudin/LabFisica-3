from graph_analysis import *
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

controller = GraphController()
controller.readChannels('data/1153_canal_2_1.csv')
# controller.readChannels('data/1153_canal_2_2.csv')
# controller.readChannels('data/1153_canal_2_3.csv')


def tensaoCircuito():
    t = controller.time_data()
    y1 = controller.channel_1_data()
    y2 = controller.channel_2_data()
    y3 = GraphController.smooth(controller.ddpInduzida(), 10)
    plt.plot(t, y1, 'b-')
    plt.plot(t, y2, 'r-')
    plt.plot(t, y3, 'g-')
    plt.xlabel("Tempo (s)")
    plt.ylabel("Potencial (V)")
    print('Pico da tensao na bobina menor: ' + str(np.nanmax(y2)))
    print('Pico da tensao na bobina maior: ' + str(np.nanmax(y1)))

    plt.grid()

    plt.show()

def correnteCircuito():
    t = controller.time_data()
    y1 = controller.channel_1_data()
    
    corrente = np.array(GraphController.smooth(y1, 35))/10
    
    
    plt.plot(t, corrente, 'g-')
    
    plt.xlabel("Tempo (s)")
    plt.ylabel("Corrente (A)")
    
    print('Pico corrente da bobina maior: ' + str(np.nanmax(corrente)))

    plt.grid()

    plt.show()

tensaoCircuito()
correnteCircuito()


'''
SENOIDAL

Pico da tensao na bobina menor: 0.0030552763500000003
Pico da tensao na bobina maior: 0.0172864323
Pico corrente da bobina maior: 0.0016631730208857137

'''

'''
TRIANGULAR

Pico da tensao na bobina menor: 0.0016995916900000001
Pico da tensao na bobina maior: 0.01634736194
Pico corrente da bobina maior: 0.0015615964991142859

'''

'''
QUADRADA

Pico da tensao na bobina menor: 0.09648241425000001
Pico da tensao na bobina maior: 0.018492462459999998
Pico corrente da bobina maior: 0.0017274946293428573

'''