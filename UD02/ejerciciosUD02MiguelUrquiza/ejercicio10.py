'''
Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los elementos
repetidos (dejando únicamente el primero de los elementos repetidos).
'''

listaPalabras=[]
cantPalabras=int(input("Cuántas palabras desea añadir: "))

for i in range(0,cantPalabras):
    listaPalabras.append(input(f'Introduzca la palabra nº{i+1} que desea añadir: '))

for palabra in listaPalabras:
    if listaPalabras.count(palabra)>1:
        listaPalabras.reverse()
        while listaPalabras.count(palabra)>1:
            listaPalabras.remove(palabra)
        listaPalabras.reverse()
        

print(listaPalabras)