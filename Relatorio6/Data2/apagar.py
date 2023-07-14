import matplotlib.pyplot as plt

numero = input('numero do scope')

with open('scope_'+numero+'.csv','r') as file:
	file.readline();file.readline()

	x = []
	y1 = []
	y2 = []
	for i in file.readlines():
		i = i.split(',')
		x.append(float(i[0]))
		y1.append(float(i[1]))
		y2.append(float(i[2]))

plt.plot(x,y1,label='canal 1')
plt.plot(x,y2,label='canal 2')
plt.legend()
plt.show()
