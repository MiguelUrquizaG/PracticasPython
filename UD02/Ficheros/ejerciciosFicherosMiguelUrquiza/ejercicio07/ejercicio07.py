'''
Crea un programa que lea los datos de clientes y los vaya escribiendo en un fichero de texto, de tal
manera que dicho fichero quede algo así como el siguiente:
'''

fichero = open('ejercicio07/clientes.txt','a')
nombre =''
while nombre !='0':
    nombre = input('Introduzca su nombre: ')
    if nombre =='0':
        break
    apellido1 = input('Introduzca su primer apellido: ')
    apellido2 = input('Introduzca su segundo apellido: ')
    edad = input('Introduzca su edad: ')
    cantRequisitos=4
    fichero.write('Nombre: \t'+nombre +"\n" + 'Apellido1:\t '+apellido1 + "\n" + 'Apellido2:\t'+ apellido2 +"\n" + 'Edad: \t\t' + edad+"\n")



