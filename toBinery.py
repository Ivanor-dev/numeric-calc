a = int(input("Digite um numero:"))

resto = []
def dividePor2(a):
    numDiv2 = a // 2
    numResto = a%2
    resto.append(numResto)
    if numDiv2 > 0:
        dividePor2(numDiv2)
    else:
        return

dividePor2(a)

while(len(resto) > 0):
    bitSignify = resto.pop()
    print(bitSignify)