'''
Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y 
elimine esa palabra de la lista. 

'''

print("Bienvenido, en este programa se permitirá rellenar una lista de palabras y eliminar la palabra indicada de la lista.")

listaPalabras=[]
cantPalabras = int(input("Introduzca la cantidad de palabras que desee añadir en la lista: "))

for i in range(0,cantPalabras):
    listaPalabras.append(input(f'Introduzca la palabra nº{i+1} que desee añadir: '))


print(f'Le muestro la lista para que elimine una {listaPalabras}')
palabraAEliminar = input("Indique la palabra de la lista que desee eliminar: ")

while palabraAEliminar not in listaPalabras:
    print("----------------------------------------------------------")
    print("La palabra seleccionada no se encuentra en la lista.")
    print(f'Le muestro la lista para que elimine una {listaPalabras}')
    palabraAEliminar = input("Por favor introduzca una palabra que pertenezca a la lista: ")

if listaPalabras.count(palabraAEliminar)>1:
    for palabra in listaPalabras:
        if palabra == palabraAEliminar:
            listaPalabras.remove(palabra)
else:
    listaPalabras.remove(palabraAEliminar)


print(f'El resultado es: {listaPalabras}')

print("Gracias por utilizar el programa.")