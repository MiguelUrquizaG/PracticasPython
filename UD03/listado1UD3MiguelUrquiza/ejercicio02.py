'''
Escriba un programa que pida tres números enteros distintos y que escriba una lista que empiece por
el más pequeño y termine en el más grande.
'''

num1 = int(input('Introduzca el primer número: '))
num2 = int(input('Introduzca el segundo número: '))
num3 = int(input('Introduzca el tercer número: '))


def ordenar_lista(numero1,numero2,numero3):
    listaNumeros = [numero1,numero2,numero3]

    listaNumeros.sort()
    return listaNumeros


print(f'La lista ordenada de menor a mayor queda: {ordenar_lista(num1,num2,num3)}')





