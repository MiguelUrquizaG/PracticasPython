'''
Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un
número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir
la lista.
'''

cantPalabras=int(input('Introduzca cuántas palabras quiere añadir a la lista de palabras: '))
listaPalabras=[]

for i in range(0,cantPalabras):
    palabra = input(f'Introduzca la palabra nº{i+1} que quiere añadir: ')
    listaPalabras.append(palabra)


print(listaPalabras)

