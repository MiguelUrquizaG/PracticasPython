'''
Escribe un programa que cuente cuántas líneas NO vacías contiene un fichero 'entrada.txt' que
tenga varias líneas de prueba
'''

fichero = open('ejercicio01/entrada.txt','r')
contadorLineas = 0

for linea in fichero:
    if not linea.startswith("\n"):
        contadorLineas+=1
print("La cantidad de lineas NO vacias son: ",contadorLineas)