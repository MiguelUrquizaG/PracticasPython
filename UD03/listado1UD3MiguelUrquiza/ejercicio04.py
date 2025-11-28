'''
Escriba un programa que pida un número y dibuje dos cuadrados de ese número de estrellas en
diagonal, como muestran los ejemplos siguientes:
'''

longitudDiagonales = int(input('Introduzca la longitud de la diagonal: '))
print()
def doble_Cuadrado(longitud):
    for _ in range(longitud):
        print("*\t"*longitud+"\n")
    for _ in range(longitud):
        print("\t"*longitud+"*\t"*longitud+"\n")


doble_Cuadrado(longitudDiagonales)