'''
2. Crea un programa que añada la fecha y hora actuales al final de un fichero
'''
from datetime import datetime

fichero = open('ejercicio02/fichero.txt','a')
fichero.write("\n"+str(datetime.now()))

fichero.close()


