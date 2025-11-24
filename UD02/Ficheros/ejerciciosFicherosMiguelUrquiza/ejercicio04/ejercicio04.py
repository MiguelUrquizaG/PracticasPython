'''
4. Crea un programa que lea un fichero llamado 'texto.txt' y genere 'numerado.txt' con todas las líneas
precedidas de su número.
'''
fichero = open('ejercicio04/texto.txt','r')
numerado = open('ejercicio04/numerado.txt','w')

cantidad=len(fichero.readlines())
fichero.close()
fichero = open('ejercicio04/texto.txt','r')

for i, linea in enumerate(fichero.readlines()):
    numerado.write("Linea: "+str(i+1)+' '+linea)

fichero.close()
numerado.close()