import matplotlib.pyplot as plt

with open('DadosOsciloscopio/trans_9_1.csv','r') as file:
    file.readline()
    file.readline()
    data = file.readlines()
    x = [] #seconds
    y = [] #volts
    for i in data:
        i = i.split(", ")
        x.append(float(i[0]))
        y.append(float(i[1]))

plt.xlabel('Tempo')
plt.ylabel('Voltagem')
plt.plot(x,y)

plt.savefig('transformador.png')

plt.show()