'''
11. Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes 
listas (en las que no debe haber repeticiones): 
Lista de palabras que aparecen en las dos listas. 
Lista de palabras que aparecen en la primera lista, pero no en la segunda. 
Lista de palabras que aparecen en la segunda lista, pero no en la primera. 
Lista de palabras que aparecen en ambas listas. 
'''

lista1=[]
lista2=[]
valor =""

listaPalabrasEnAmbasListas=[]
listaPalabrasLista1=[]
listaPalabrasLista2=[]


while valor !="0":
    print("Pulse 0 para parar de añadir")
    valor = input("Introduzca el valor que desea añadir a la lista1: ")
    if valor!="0":
        lista1.append(valor)

valor=""

while valor !="0":
    print("Pulse 0 para parar de añadir")
    valor = input("Introduzca el valor que desea añadir a la lista2: ")
    if valor!="0":
        lista2.append(valor)



#Lista de palabras que aparecen en las dos listas
for palabra in lista1:
    if palabra in lista2 and palabra not in listaPalabrasEnAmbasListas:
        listaPalabrasEnAmbasListas.append(palabra)

print(listaPalabrasEnAmbasListas)
#Lista de palabras que aparecen en la primera lista
for palabra in lista1:
    if palabra not in listaPalabrasLista1 and palabra not in lista2:
        listaPalabrasLista1.append(palabra)

print(listaPalabrasLista1)
#Lista de palabras que aparecen en la segunda lista, pero no en la primera.
for palabra in lista2:
    if palabra not in listaPalabrasLista2 and palabra not in lista1:
        listaPalabrasLista2.append(palabra)
print(listaPalabrasLista2)
#Lista de palabras que aparecen en ambas listas
print(listaPalabrasLista1+listaPalabrasLista2+listaPalabrasEnAmbasListas)