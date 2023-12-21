import math as math

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


def posicaoFalsa(a, b, epslon):
    raiz = (acharY(b) * a - acharY(a) * b)/(acharY(b) - acharY(a))
    if abs(acharY(raiz)) <= epslon:
        return raiz
    else:
        if acharY(raiz) * acharY(a) < 0:
            return posicaoFalsa(a, raiz, epslon)
        else:
            return posicaoFalsa(raiz, b, epslon)



equacao()

a = float(input("ponto A: "))

b = float(input("ponto B: "))

epslon = float(input("precisão: "))

print(posicaoFalsa(a, b, epslon))