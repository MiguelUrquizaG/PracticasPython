'''
5. Realiza un programa que lea el fichero 'datos.txt' y cree un nuevo fichero 'invertido.txt' con las
líneas en orden inverso.
'''

datos = open('ejercicio05/datos.txt','r')
invertido = open('ejercicio05/invertido.txt','w')

textoAlReves = datos.readlines()
textoAlReves.reverse()
textoAlReves[0] = textoAlReves[0]+"\n"

invertido.writelines(textoAlReves)