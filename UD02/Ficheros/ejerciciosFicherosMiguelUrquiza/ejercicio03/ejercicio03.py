'''
Haz un programa que copie el contenido de un fichero llamado 'origen.txt' en otro llamado
'copia.txt'.
'''
fichero = open('ejercicio03/origen.txt','r')
copia = open('ejercicio03/copia.txt','w')

copia.writelines(fichero.readlines())


