with open('DadosOsciloscopio/trans_9_1.csv','r') as file:
    file.readline()
    file.readline()
    data = file.readlines()
    x = [] #seconds
    y = [] #volts
    search = True
    time = []
    for i in data: #2_000 dados aqui
        x,y = map(float,i.split(", "))
        if search:
            if y>=4:
                time.append(x)
                search = False
        elif y<=3:
            search = True
print(time[1] - time[0])
print(time[2] - time[1])
print((time[2] - time[0])/2)
        

