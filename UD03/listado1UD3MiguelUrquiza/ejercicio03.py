'''
Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre
un mensaje cada vez que un número no sea mayor que el anterior.
'''

cantNumeros = int(input('Introduzca la cantidad de números que desea introducir: '))

def compare_numbers(cantidadNumeros):
    primero= True
    numAnterior=0
    nuevoNum = 0
    for _ in range(cantidadNumeros):
        nuevoNum = int(input('Introduzca un número: '))
        if(nuevoNum > numAnterior and not primero):
            print(f'El nuevo número ({nuevoNum}) es mayor que el anterior ({numAnterior})')
        primero = False
        numAnterior = nuevoNum

compare_numbers(cantNumeros)