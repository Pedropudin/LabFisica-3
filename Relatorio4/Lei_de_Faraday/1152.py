from graph_analysis import *
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

controller = GraphController()

def tensaoCircuito():
    controller.readChannels('data/1152.csv')

    t = controller.time_data()
    y1 = controller.channel_1_data()
    y2 = controller.channel_2_data()
    y3 = GraphController.smooth(controller.ddpHall(), 35)
    plt.plot(t, y1, 'b-')
    plt.plot(t, y2, 'r-')
    plt.plot(t, y3, 'g-')
    plt.xlabel("Tempo (s)")
    plt.ylabel("Potencial (V)")

    print('Pico corrente: ' + str(np.nanmax(y1)/10))
    print('Pico tensao hall: ' + str(np.nanmax(y3)))

    plt.grid()

    plt.show()

def campoMagnetico():
    controller.readChannels('data/1152.csv')

    t = controller.time_data()
    y1 = GraphController.smooth(controller.ddpHall()/HALL, 35)

    plt.plot(t, y1, 'g-')
    plt.xlabel("Tempo (s)")
    plt.ylabel("Campo magnético (T)")

    print('Pico campo magnetico: ' + str(np.nanmax(y1)))
   
    plt.grid()

    plt.show()


tensaoCircuito()
campoMagnetico()