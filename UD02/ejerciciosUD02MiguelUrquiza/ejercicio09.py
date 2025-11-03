'''
Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista 
igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta). 
'''
print("Bienvenido este programa permite rellenar una lista de palabras y crea otra invirtiendo esta creada.")

listaOriginal=[]
cantPalabras=int(input("Cuántas palabras desea añadir: "))

for i in range(0,cantPalabras):
    listaOriginal.append(input(f'Introduzca la palabra nº{i+1} que desea añadir: '))

listaInvertida = list(reversed(listaOriginal))

print(listaOriginal)
print(listaInvertida)