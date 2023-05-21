from matplotlib import pyplot
import numpy as np

def q1Eq(t, r, c, v0):
    tau = r*c
    return  c*(v0 * np.exp(-(t/tau)))

def q2Eq(t, r, c, v0):
    tau = r*c
    return  c*(1-(v0 * np.exp(-(t/tau))))

def iEq(t, r, c, v0):
    return  q1Eq(t, r, c, v0)/r
    

r = 100
c1, c2 = 0.05, 0.05

x = np.linspace(0,10,2000)
# q1 = list(q1Eq(b, r, c1, 10) for b in list(x))
# q2 = list(q2Eq(b, r, c2, 10) for b in list(x))
i = list(iEq(b, r, c2, 10) for b in list(x))


# pyplot.plot(x, q1, 'r-', label='data')
# pyplot.plot(x, q2, 'b-', label='data')
pyplot.plot(x, i, 'b-', label='data')

pyplot.xlabel("Tempo (s)")
# pyplot.ylabel("Carga (C)")
pyplot.ylabel("Corrente (A)")

pyplot.show()