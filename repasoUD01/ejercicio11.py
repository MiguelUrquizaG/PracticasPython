'''
Escribe un programa que pida primero un número entero y después pida números enteros hasta que la suma
de los números introducidos coincida con el número inicial. El programa termina escribiendo la lista de
números
'''

numMax = int(input("Introzuca el número a alcanzar: "))
sumaNum=0
isAcertado = False

while sumaNum <numMax and not isAcertado:
    numInput = int(input("Introduzca el número: "))
    sumaNum+=numInput
    if sumaNum >numMax:
        sumaNum -= numInput
        print(f'Te has pasado de número, te redirijo a introducción de número el valor actual es {sumaNum}')
    elif sumaNum == numMax:
        isAcertado = True


if isAcertado:
    print(f'Acertaste el número era: {numMax}')


