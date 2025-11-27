'''
Escriba un programa que pida un número. Después pregunte cuántos números se van a introducir, pida
esos números, y escriba cuántos de esos números era mayor que el anterior.
'''

numInicial= int(input('Introduzca un número: '))
cantNumeros = int(input('Introduzca cuántos números desea introducir: '))
numTemporal = 0

def compare(numInicial,cantNumeros):
    numSuperiores=[]
    for _ in range(cantNumeros):
        numTemporal = int(input('Introduzca un número: '))
        if numTemporal > numInicial:
            numSuperiores.append(numTemporal)

    return numSuperiores




print(f'Los números superiores a {numInicial} son: {compare(numInicial=numInicial,cantNumeros=cantNumeros)}')