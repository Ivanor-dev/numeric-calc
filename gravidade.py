import matplotlib.pyplot as plt

a = 9.8
i = 0
s = 0
x = [-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
y = []

def velocityToTime(x, i):

    v = (a * x[i])

    return v

while(i < 14):
    s += velocityToTime(x, i)
    y.append(s)
    i += 1

    


plt.plot(x, y)

plt.xlabel("Time")
plt.ylabel("Distance")
plt.title("")

plt.show()

