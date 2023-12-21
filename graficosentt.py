import matplotlib.pyplot as plt
import math as math

PI = math.pi
i = 0
x = [0*PI ,PI/4, (2*PI)/4, (3*PI)/4, PI, (5*PI)/4, (6*PI)/4, (7*PI)/4, 2*PI]
ySin = []

def sinFunction(x, i):

    y = math.sin(x[i])
    ySin.append(y)

while(i < 8):
    sinFunction(x, i)
    i += 1


plt.plot(x, ySin)

plt.show()