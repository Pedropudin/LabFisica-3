#importações
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import griddata

def plot_contour(x,y,z,resolution = 50,contour_method='linear'):
    resolution = str(resolution)+'j'
    X,Y = np.mgrid[min(x):max(x):complex(resolution),   min(y):max(y):complex(resolution)]
    points = [[a,b] for a,b in zip(x,y)]
    Z = griddata(points, z, (X, Y), method=contour_method)
    return X,Y,Z

conv_let = {'a':-9,'b':-8,'c':-7,'d':-6,'e':-5,'f':-4,'g':-3,'h':-2,'i':-1,'j':0,'k':1,'l':2,'m':3,'n':4,'o':5,'p':6,'q':7,'r':8,'s':9}
conv_num = {0:-13,1:-12,2:-11,3:-10,4:-9,5:-8,6:-7,7:-6,8:-5,9:-4,10:-3,11:-2,12:-1,13:0,14:1,15:2,16:3,17:4,18:5,19:6,20:7,21:8,22:9,23:10,24:11,25:12,26:13}

x, y, z = [],[],[]

with open('placas_paralelas.csv','r') as placas:
    for i in range(57):
        val = placas.readline().split(',')
        x.append(conv_let[val[0]])
        y.append(conv_num[int(val[1])])
        z.append(float(val[2][:-1]))

X,Y,Z = plot_contour(x,y,z,resolution = 50,contour_method='linear')

with plt.style.context("seaborn-white"):
    fig, ax = plt.subplots(figsize=(13,8))
    ax.scatter(x,y, color="black", linewidth=9, edgecolor="ivory", s=50)
    contours=ax.contourf(X,Y,Z,20, cmap='GnBu_r',origin="lower")
    plt.colorbar(contours, shrink=0.67,label="Voltagem")
    plt.clabel(contours, inline=True, fontsize=8, fmt='%.1f')

plt.savefig('placas_paralelas.png', format='png')
plt.show()

