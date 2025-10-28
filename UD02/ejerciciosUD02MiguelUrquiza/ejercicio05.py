'''
Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga
cuántas veces aparece esa palabra en la lista.
'''
print("Bienvenido, este programa te permite rellenar una lista de palabras y después buscar cuantas veces sale una palabra que se le indique.")

listaPalabras=[]
cantPalabras=int(input("Cuántas palabras desea añadir: "))

for i in range(0,cantPalabras):
    listaPalabras.append(input("Introduzca la palabra a introducir: "))



palabraABuscar=input("Introduzca la palabra a buscar: ")

print(f'La palabra "{palabraABuscar}" aparece {listaPalabras.count(palabraABuscar)} veces.')

print("Gracias por usar el programa.")
