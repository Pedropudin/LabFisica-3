import matplotlib.pyplot as plt
import numpy as np

def readCSV(csv):
    '''
    Recebe: nome do csv
    Retorna: listas com os valores
    '''
    with open(csv,'r') as file:
        tam = len(file.readline().split(','))
        x = []
        if tam == 2:
            y = []
            for i in file.readlines():
                i = i.replace(' ','').split(',')
                x.append(float(i[0]))
                y.append(float(i[1]))
            return x,y
        if tam == 3:
            y1 = []
            y2 = []
            for i in file.readlines():
                i = i.replace(' ','').split(',')
                x.append(float(i[0]))
                y1.append(float(i[1]))
                y2.append(float(i[2]))
            return x,y1,y2

def fase(x,y1,y2):
    '''
    Recebe os dados de dois gráficos
    Retorna a diferença de fase entre eles, que é dada por f*2*pi*{intervalo de tempo entre máximos consecutivos}
    '''
    pass
        
#----------------12.7.1--------------#
'''x,y1 = readCSV('./Data1/scope_0_1.csv')
_,y2 = readCSV('./Data1/scope_0_2.csv')

x,y1,y2 = np.array(x),np.array(y1),np.array(y2)

plt.plot(x,y1,label='Canal 1')
plt.plot(x,y2,label='Canal 2')
plt.legend()
plt.show()'''

_,ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(45,2)
plt.show()
        