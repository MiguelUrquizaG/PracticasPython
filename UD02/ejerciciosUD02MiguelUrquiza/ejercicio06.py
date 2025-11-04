'''
 Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y 
sustituya la primera por la segunda en la lista.
'''
print("Bienvenido este programa permite rellenar una lista de palabras y sustituir una palabra de esta lista por otra introducida")

listaPalabras=[]
cantPalabras=int(input("Cuántas palabras desea añadir: "))
isPalabra=False

for i in range(0,cantPalabras):
    listaPalabras.append(input(f'Introduzca la palabra nº{i+1} que desea añadir: '))


print("A continuación le voy a pedir una palabra de la lista la cuál desee sustituir.")
print(f'Le muestro la lista para que pueda elegir {listaPalabras}')
palabraSustituir=input("Introduzca la palabra: ")

while palabraSustituir not in listaPalabras:
        print("La palabra seleccionada no pertenece a la lista.")
        print(f'Le muestro la lista para que pueda elegir {listaPalabras}')
        palabraSustituir = input("Por favor introduzca una palabra existente: ")


print("Ahora necesito que introduzca la palabra que desea añadir en el lugar de la anterior.")
palabraSustituta = input("Introduzca la palabra: ")



if listaPalabras.count(palabraSustituir)>1:
      for palabra in listaPalabras:
            if palabra == palabraSustituir:
                listaPalabras[listaPalabras.index(palabra)] = palabraSustituta
else:
    indice = listaPalabras.index(palabraSustituir)
    listaPalabras[indice]=palabraSustituta  
            

'''
for i in range(len(palabras)):
    if palabras[i] == palabraaSustituir:
        palabras[i] = palabraSustituta
'''

print(f'El resultado es: {listaPalabras}')

print("Gracias por usar el programa.")