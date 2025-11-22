'''
Escribe un programa que cuente cuántas líneas NO vacías contiene un fichero 'entrada.txt' que
tenga varias líneas de prueba
'''

fichero = open('ejercicio01/entrada.txt','r')
contadorLineas = 0

cantidad = len(fichero.readlines())

fichero.close()
fichero = open('ejercicio01/entrada.txt','r')

for i in range(cantidad):
    if not fichero.readline().startswith("\n"):
        contadorLineas+=1
print("La cantidad de lineas NO vacias son: ",contadorLineas)