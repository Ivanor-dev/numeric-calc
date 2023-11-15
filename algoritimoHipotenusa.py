from math import *

def __Hipotenusa(cateto, hipotenusa, count):
    resultado = pow(hipotenusa, 2) - 2 * cateto

    if resultado < 0.0000001 and resultado > 0:
        return hipotenusa
    else:
        if resultado < 0:
            hipotenusa = hipotenusa + (hipotenusa/(2 + (4 * count)))
        else:
            hipotenusa = hipotenusa - (hipotenusa/(2 + (4 * count)))
        return __Hipotenusa(cateto, hipotenusa, count + 1)

erroAbsoluto = __Hipotenusa(1,1,0)

print(__Hipotenusa(1,1,0))
print(erroAbsoluto - 1.41421356237)
    
    
   





