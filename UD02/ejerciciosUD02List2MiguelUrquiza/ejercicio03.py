'''
Crear un diccionario que tenga como claves el dni de un estudiante y como valor la nota media de su
expediente. La nota media se generará de manera aleatoria entre 1 y 10.
Escribir el código necesario en un menú para hacer los siguiente:
a) Mostrar los datos.
b) Modificar la nota.
c) Añadir un nuevo estudiante.
d) Crear un nuevo diccionario (no modificar el original) solo con los estudiantes que tienen nota media
mayor a un valor dado por teclado (por ejemplo, para comprobar que pueden entrar en un ciclo según esa
nota de corte).
'''

import random

diccionarioAlumnosNotas={}
dni= ''
dniABuscar=''

while dni!='0':

    print('Introduzca 0 para parar de agregar')
    dni = input('Introduzca su dni: ')
    while dni in diccionarioAlumnosNotas:
        print('Introduzca 0 para parar de agregar')
        print('Dni ya registrado introduzca otro.')
        dni = input('Introduzca su dni: ')

    if dni !='0':
        diccionarioAlumnosNotas[dni] = round(random.uniform(1,10),2)
    

for dni, media in diccionarioAlumnosNotas.items():
    print(f'La nota media del alumno con DNI {dni} es: {media}')

dniABuscar = input('Introduzca el DNI al cuál desea modificarle la nota: ')

if dniABuscar in diccionarioAlumnosNotas:
    diccionarioAlumnosNotas[dniABuscar] =round(float(input('Introduzca la nueva nota media: ')),2)

print(diccionarioAlumnosNotas)
