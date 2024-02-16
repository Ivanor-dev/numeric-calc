def newton (f, fLinha, x0, epsilon, iterMax):

    if abs(f(x0)) <= epsilon:
        print("%d\t%e\t%e\t%e" % (0, x0, f(x0), fLinha(x0)))
        return x0;
    

    for k in range(1, iterMax + 1):

        x1 = x0 - f(x0)/fLinha(x0)

        print("%d\t%e\t%e\t%e" % (k, x1, f(x1), fLinha(x1)))

        if abs(f(x1)) <= epsilon:
            return x1;

        x0 = x1
    
    print("ERROR: Número máximo de iterações atingido")
    return x1

def f(x):
    return x**3 - 9*x + 3


def fLinha(x):
    return 3*x**2 - 9


newton(f, fLinha, 0.5, 0.00001, 20)