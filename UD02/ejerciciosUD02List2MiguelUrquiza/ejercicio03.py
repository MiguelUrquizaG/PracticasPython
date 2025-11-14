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
notaMedia=0.0
notaASuperior=0.0
diccionarioAlumnosSuperiorNota={}
opcion =-1

while dni!='0':
    print('Introduzca 0 para parar de agregar')
    dni = input('Introduzca su dni: ')
    while dni in diccionarioAlumnosNotas:
        print('Introduzca 0 para parar de agregar')
        print('Dni ya registrado introduzca otro.')
        dni = input('Introduzca su dni: ')
    if dni !='0':
        diccionarioAlumnosNotas[dni] = round(random.uniform(1,10),2)


while opcion!=0:
    match opcion:
        case 0:
            print('Saliendo...')
        case 1:
            for dni, media in diccionarioAlumnosNotas.items():
                print(f'La nota media del alumno con DNI {dni} es: {media}')  
        case 2:
            dniABuscar = input('Introduzca el DNI al cuál desea modificarle la nota: ')
            if dniABuscar in diccionarioAlumnosNotas:
                diccionarioAlumnosNotas[dniABuscar] =round(float(input('Introduzca la nueva nota media: ')),2)
            print(diccionarioAlumnosNotas)
        case 3:
            dni = input('Introduzca el dni que desea agregar: ')
            while dni in diccionarioAlumnosNotas:
                print('El dni se encuentra en el diccionario.')
                dni = input('Introduzca de nuevo un dni diferente: ')

            notaMedia = round(float(input('Introduzca el valor de la nota media: ')),2)
            diccionarioAlumnosNotas[dni]=notaMedia
        case 4:
            notaASuperior=round(float(input('Introduzca el valor de nota a superior: ')),2)

            for dni,notas in diccionarioAlumnosNotas.items():
                if notas > notaASuperior:
                    diccionarioAlumnosSuperiorNota[dni]=notas
            print(f'Los alumnos que han superado la nota de corte son:  {diccionarioAlumnosSuperiorNota}')








