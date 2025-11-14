#Para abrir un fichero se utiliza la función open, el segundo parametro es 
# en que manera quiero abriirlo r -> read
f = open('temps.txt','r')
print("Primera: ",f.read())
#Read devuelve todo el fichero.
#Seek pone el puntero donde queremos.
#Es muy importante cerrar los ficheros cuando terminemos
#de trabajar con él 
print('Ultima')
f.seek(0)
linea1 = f.readline()
print(linea1)

print('Bucle')
f.seek(0)
for  linea in f:
    print(linea, end="")
    
f.seek(0)
#readlines devuelve una lista de lineas.

print('\nSegunda lista.')
lineas = f.readlines()
for linea in lineas:
    print(linea, end="")

f.close()
#Obligatoriamente se tiene que utilizar close() para cerrar el fichero