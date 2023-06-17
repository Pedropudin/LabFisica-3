from graph_analysis import *
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

controller = GraphController()
controller.readChannels('data/1153.csv')

def tensaoCircuito():

    t = controller.time_data()
    y1 = controller.channel_1_data()
    y2 = controller.channel_2_data()
    y3 = GraphController.smooth(controller.ddpHall(), 35)
    plt.plot(t, y1, 'b-')
    plt.plot(t, y2, 'r-')
    plt.plot(t, y3, 'g-')
    plt.xlabel("Tempo (s)")
    plt.ylabel("Potencial (V)")
    print('Pico tensao hall: ' + str(np.nanmax(y3)))
    print('Pico tensao circuito: ' + str(np.nanmax(y1)))

    plt.grid()

    plt.show()

def correnteCircuito():
    t = controller.time_data()
    y1 = controller.channel_1_data()
    
    corrente = np.array(GraphController.smooth(y1, 35))/10
    
    
    plt.plot(t, corrente, 'g-')
    
    plt.xlabel("Tempo (s)")
    plt.ylabel("Corrente (A)")
    
    print('Pico corrente: ' + str(np.nanmax(corrente)))

    plt.grid()

    plt.show()

def campoMagnetico():
    t = controller.time_data()
    y1 = GraphController.smooth(controller.ddpHall()/HALL, 35)

    plt.plot(t, y1, 'g-')
    plt.xlabel("Tempo (s)")
    plt.ylabel("Campo magnético (T)")

    print('Pico campo magnetico: ' + str(np.nanmax(y1)))
   
    plt.grid()

    plt.show()

tensaoCircuito()
correnteCircuito()
campoMagnetico()