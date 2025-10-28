'''
Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera 
lista los nombres de la segunda lista.
'''

print("Bienvenido este programa permite rellenar dos listas y eliminar las palabras de la primera lista que aparezcan en la segunda.")

lista1 =[]
lista2=[]
cantPalabrasLista1 = int(input("Introduzca la cantidad de palabras que desea en la lista 1: "))
cantPalabrasLista2 = int(input("Introduzca la cantidad de palabras que desea en la lista 2: "))

for i in range (0,cantPalabrasLista1):
    lista1.append(input(f'Introduzca la palabra nº{i+1} que desea añadir a la lista 1: '))

for i in range(0,cantPalabrasLista2):
    lista2.append(input(f'Introduzca la palabra nº{i+1} que desea añadir a la lista 2: '))


print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')

for palabra2 in lista2:
    if lista1.count(palabra2)>0:
        for palabra in lista1:
            if palabra == palabra2:
                lista1.remove(palabra)

print(f'El resultado de la lista 1 es: {lista1}')

print("Gracias por utilizar el programa.")