import matplotlib.pyplot as plt
import math as math

x = []
y = []
coeficientes = []

def representarFuncao(numOrdem):
    i = numOrdem

    while(i + 1 > 0):
        print(i)
        a = int(input("numero do coeficiente:"))
        coeficientes.append(a)
        i -= 1

    while(i < 9):
        x.append(-4+i)
        i += 1

def acharY(x):
    i = 0
    while(i < len(x)):
        j = 0
        resultado = 0
        while(j < len(coeficientes)):
            polinomio = math.pow(x[i], len(coeficientes) - j)
            resultado += coeficientes[j]*polinomio
            j += 1
        i += 1
        y.append(resultado)


grauPolinomio = int(input("Indique o grau do polinómio: "))

representarFuncao(grauPolinomio)
acharY(x)

plt.plot(x,y)


plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()

