import matplotlib.pyplot as plt

with open('DadosOsciloscopio/scope_5_1.csv','r') as file:
    file.readline()
    file.readline()
    data = file.readlines()
    x = [] #seconds
    y = [] #volts
    for i in data:
        i = i.split(", ")
        x.append(float(i[0]))
        y.append(float(i[1]))

fig,ax = plt.subplots()

ax.plot(x,y)

plt.show()