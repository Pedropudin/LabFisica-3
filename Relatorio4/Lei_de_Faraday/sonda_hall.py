import math
import numpy as np
#from LabIFSC import *
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


permeabilidadeAr = (4*math.pi)*1e-7

def get_dados(csv,factorx=1e-2,factory=1e-3,fundox=0,fundoy=0):
    with open(csv,'r') as file:
        data = {}
        l = file.readlines()
        for i in range(1,len(l)):
            linha = l[i].split(',')
            try:
                data[(float(linha[0])*factorx)-fundox] = (float(linha[1])*factory)-fundoy
            except:
                print("Ou string nula, ou algum 0")

    return data

def get_coefAngular(x,y):
    assert len(x) == len(y), "As duas listas devem ter o mesmo tamanho"
    N = len(x)
    
    xbar = sum(x)/N
    ybar = sum(y)/N
    
    x2 = 0
    rms = 0
    rms2 = 0
    rmsy = 0
    for i in range(N):
        x2 += (x[i])**2
        rms += (x[i]-xbar)
        rmsy += (x[i]-xbar)*y[i]
        rms2 += (x[i]-xbar)**2
    
    a = rmsy/rms2    
    b = ybar - a*xbar
    
    deltay = 0
    for i in range(N):
        deltay += (a*x[i] + b - y[i])**2
        
    deltay = math.sqrt(deltay/(N-2))
    
    deltaa = deltay/(math.sqrt(rms2))
    deltab = math.sqrt(x2/(N*rms2))*deltay
    
    return a, deltaa
        
    

def campoBobina(x,espiras,corrente,permeabilidade,raio):
    return espiras * (permeabilidade * corrente * raio**2)/(2*(x**2 + raio**2))**(3/2)

def campoHall(tensao,coeficiente):
    return tensao*coeficiente

def campoSolenoide(espiras,corrente,comprimento,permeabilidade):
    return (permeabilidade*espiras*corrente)/comprimento


#Dados
comprimentoSolenoide = 149*1e-3 #erro de 5e-5
espirasSolenoide = 760

data = get_dados('data/calibracao-segundodDia.csv',factorx = 1,factory=1)#arquivo
amperagem = np.array(list(data.keys()))
voltagem = np.array(list(data.values()))

campoCalculado = [campoSolenoide(espirasSolenoide,i,comprimentoSolenoide,permeabilidadeAr) for i in amperagem]
    
param = np.polyfit(voltagem,campoCalculado,1)
#print(param)
    
coeficienteHall = param[0]
coef,erro = get_coefAngular(voltagem,campoCalculado)
print(f"O Coeficiente é {coeficienteHall}T/V")    
    
#plt.plot(voltagem,campoCalculado,label='Dados Coletados')
plt.plot(voltagem,[(param[0]*i + param[1]) for i in voltagem],label=f'Melhor Reta',color='blue')
plt.scatter(voltagem,campoCalculado,label='Dados Coletados',color='red')
plt.grid(True)
plt.xlabel('Voltagem(V)');plt.ylabel('Campo Magnético(T)')
plt.legend()
#plt.savefig('Results/calibracao.png')
plt.show()