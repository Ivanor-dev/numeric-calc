import numpy as np
iterator = 0

x = int(input("coloque o x0"))

while(True):
    iterator=+1
    xProximo = x - ((4*np.cos(x) - (np.exp)**x)/(-4*np.sin(x) - (np.exp)**x))
    erroRel = abs(xProximo - x) / abs(xProximo)
    if erroRel < 0.01:
        print(f"raiz aproximada: ${xProximo}")
        print(f"quantidade de iteraçoes: ${iterator}")
        break
    x = xProximo
