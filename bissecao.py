import math as math

x = []
y = []
coeficientesPolinomio = []

def equacao():
    qPolinomia = int(input("Grau do polinomio: "))
    i = 0
    while(i <= qPolinomia):
        coeficiente = float(input("coeficiente do polinomio {}: ".format(i)))
        coeficientesPolinomio.append(coeficiente)
        i += 1

def acharY(x):
        j = 0
        resultado = 0
        while j < len(coeficientesPolinomio):
            polinomio = math.pow(x, len(coeficientesPolinomio) - j - 1)
            resultado += coeficientesPolinomio[j]*polinomio
            j += 1
        
        return resultado

def bissecao(a, b, epslon):

        print("passou")
        raiz = b - a
        if abs(raiz) < epslon:
            return (b + a) / 2
        else:
            if acharY((b + a) / 2) * acharY(a) < 0 or acharY((b + a) / 2) * acharY(b) < 0:
                return bissecao((b + a) / 2, b, epslon)
            else:
                return bissecao(a, (b + a) / 2, epslon)

equacao()

a = float(input("ponto A: "))


b = float(input("ponto B: "))

epslon = float(input("precisão: "))

print(bissecao(a, b, epslon))
