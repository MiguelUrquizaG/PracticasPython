'''
6. Crea un programa que lea de un fichero y tenga las siguientes funcionalidades en un menú:
- La palabra de mayor longitud.
- Las veces que aparece una palabra.
- Lea una línea aleatoria del fichero.
- Dos funcionalidades más inventadas por tí.
'''
import random

opcion=-1
fichero =  open('ejercicio06/fichero.txt','r')
cantidad = len(fichero.readlines())
fichero.close()



while opcion!=0:
    print('0. Salir')
    print('1. La palabra de mayor longitud')
    print('2. Las veces que aparece una palabra.')
    print('3. Lea una línea aleatoria del fichero.')
    print('4. Mostrar todo el texto en mayuscula')
    print('5. Contar numero de palabras')
    opcion = int(input('Selecciona una opción: '))

    match opcion:
        case 0:
            print('Saliendo...')
        case 1:
            fichero =  open('ejercicio06/fichero.txt','r')
            linea=[]
            maxPalabra=0
            palabraGrande = ""

            for lineas in range(cantidad):
                linea = fichero.readline().split()
                for palabra in linea:
                    if len(palabra) > maxPalabra:
                        palabraGrande = palabra
                        maxPalabra = len(palabra)

            print(palabraGrande)

            fichero.close()
        case 2:
            fichero =  open('ejercicio06/fichero.txt','r')

            palabraABuscar =input('Indica la palabra que deseas buscar: ')
            cantidadVecesPalabra=0

            for lineas in range(cantidad):
                linea = fichero.readline().lower().split()
                cantidadVecesPalabra += linea.count(palabraABuscar)


            print(f'La palabra {palabraABuscar} se ha encontrado {cantidadVecesPalabra} veces.')
            fichero.close()
        case 3:
            fichero =  open('ejercicio06/fichero.txt','r')

            lineasTexto = fichero.readlines()

            print(lineasTexto[random.randint(0,cantidad-1)])
        case 4:
            fichero =  open('ejercicio06/fichero.txt','r')

            lineasFichero = fichero.readlines()

            for i,linea in enumerate(lineasFichero):
                lineasFichero[i] = linea.upper()

            print(lineasFichero)
            fichero.close()
        case 5:
            fichero =  open('ejercicio06/fichero.txt','r')
            cantidadPalabras =0
            for lineas in range(cantidad):
                linea = fichero.readline().split()
                cantidadPalabras+=len(linea)
                
            print(f'Hay {cantidadPalabras} palabras')
            fichero.close()
