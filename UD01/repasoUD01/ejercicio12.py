'''
Escribe un programa que genere un número aleatorio entre 0 y 10 y nos pida adivinarlo Tenemos 3 intentos.

import random

aleatorio = random.randint(0,10)
isAcertado =False
intentosMax=3

while intentosMax>0 and not isAcertado:
    numAcertado = int(input("Introduzca el número: "))
    intentosMax-=1
    if aleatorio != numAcertado:
        print(f'No has acertado te quedan {intentosMax} intentos.')
    else:
        isAcertado = True   

if isAcertado:
    print(f'Enhorabuena has acertado el número, era {aleatorio}')
else:
    print( f'No has acertado el número este era el --> {aleatorio} ')
    
'''

'''
num = 3.12313141241232
print(round(num,2))

'''

num = 9

print(f'{num=}')