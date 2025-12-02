'''
Escriba un programa que pida tres números enteros distintos y que escriba una lista que empiece por
el más pequeño y termine en el más grande.
'''

# num1 = int(input('Introduzca el primer número: '))
# num2 = int(input('Introduzca el segundo número: '))
# num3 = int(input('Introduzca el tercer número: '))
#Indicar cantidad números introducidos.
#Hacer en la función un while para que introduzca números distintos.
# Mezcla de los dos pero creo que la de Gabriel está mejor.
cantNum =4
listaNumeros=[]

def ordenar_lista(cantNumeros):
    #listaNumeros = [numero1,numero2,numero3]
    # No se leen numeros dentro de una función
    for _ in range (cantNumeros):
        num = int(input('Introduzca el número: '))
        # while num in listaNumeros:
        #     print('El número ya se encuentra en la lista.')
        #     num = int(input('Introduzca el número: '))
        listaNumeros.append(num)

    maxNum = max(listaNumeros)
    minNum = min(listaNumeros)

    if listaNumeros.count(maxNum)>1:
        for _ in range(listaNumeros.count(maxNum)):
            listaNumeros.remove(maxNum)
            listaNumeros.append(maxNum)

    listaNumeros.remove(minNum)
    listaNumeros.insert(0,minNum)
    

    # listaNumeros.sort()
    return listaNumeros


print(f'La lista ordenada de menor a mayor queda: {ordenar_lista(cantNum)}')





