'''
Con dos listas con números aleatorios haz que si la division entre ambos es exacta se resten y si no se suman
y el resultado de esas operaciones se vaya guardando en una variable para la cual vaya guardando
la suma de los resultados de cada operación
'''
import random
lista_numeros2=[]
lista_numeros=[]
numAleatorio=0
suma=0
resultadoOperacion=0

for i  in range(0,10):
    numAleatorio=random.randint(1,10)
    lista_numeros.append(numAleatorio)
    numAleatorio=random.randint(1,10)
    lista_numeros2.append(numAleatorio)

print("Lista 1",lista_numeros)
print("Lista 2",lista_numeros2)
print(list(zip(lista_numeros ,lista_numeros2)))

for numero,numero2 in zip(lista_numeros,lista_numeros2):
    if numero%numero2==0:
        resultadoOperacion=numero-numero2
    else:
        resultadoOperacion=numero+numero2
    suma+= resultadoOperacion
    print(suma)

print("La suma final es:",suma)