'''
Haz un programa que copie el contenido de un fichero llamado 'origen.txt' en otro llamado
'copia.txt'.
'''
fichero = open('ejercicio03/origen.txt','r')
copia = open('ejercicio03/copia.txt','w')

copia.writelines(fichero.readlines())
# Si es muy grande el archivo no copiarlo así si no recorriendo linea por linea.
fichero.close()
copia.close()


