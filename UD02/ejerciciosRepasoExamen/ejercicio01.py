'''

Vas a crear un programa en Python que permita gestionar los ingresos diarios de un gimnasio por las reservas de clases.
Cada elemento de la lista será un número decimal (float) que representa el dinero recaudado en un día.

El programa no debe usar clases ni objetos, solo listas (y si hace falta, tuplas puntualmente).
Debe incluir un menú con las siguientes opciones:

    1.Registrar un nuevo ingreso diario (añadir un nuevo valor a la lista).

    2.Eliminar el ingreso de un día (por ejemplo, si se cancela una clase y hay que devolver el dinero).

    3.Mostrar todos los ingresos con su número de día y formato legible.

    4.Indicar el día con menor ingreso y cuántas veces se repitió esa cantidad.

    5.Aumentar el ingreso de un día concreto (por ejemplo, si se suman suplementos o nuevas reservas).

    6.Calcular el total recaudado en todos los días registrados.

    7.Ordenar los ingresos de menor a mayor.

    8.Calcular la mediana de ingresos diarios.

    9.Calcular el porcentaje de días con ingresos superiores a 100 €.

    10.Dividir la lista en dos nuevas listas: una con los días en los que se recaudó más de la media, y otra con los que se recaudó menos o igual.

El programa debe comenzar con una lista ya creada con algunos valores iniciales (por ejemplo, ingresos = [85.5, 120.0, 95.0, 150.0, 60.5, 200.0]).

Debe mostrar un menú en bucle hasta que el usuario decida salir, y cada opción debe realizar su acción sobre la lista y mostrar el resultado correspondiente.
'''

ingresos = [85.5, 120.0, 95.0, 150.0, 60.5, 200.0]
opcion =-1
nuevoIngreso=0.0
dia=0
menor =0.0
totalRecaudado=0.0
media =0.0
cantDiasMas100Euros=0
cantASuperar=100.0
porcentajeDias=0.0
listaIngresosSuperioresMedia=[]
listaIngresosInferioresMedia=[]

while opcion != 0:
    print('------------------------------------------------------------------------------------')
    print('0. Salir')
    print('1. Añadir nuevo valor')
    print('2. Eliminar ingreso de un día')
    print('3. Mostrar los ingresos con su número de día y formato legible.')
    print('4. Indicar el día de menor ingreso y cuántas veces se repitió esa cantidad.')
    print('5. Aumentar ingreso de un día concreto.')
    print('6. Calcular total recaudado.')
    print('7. Ordenar los ingresos de menor a mayor.')
    print('8. Calcular la mediana de ingresos diarios.')
    print('9. Calcular porcentaje de días con ingresos superiores a 100€')
    print('10. Dividir en dos listas: una valores mayores a la media otra con valores menores o igual a la media.')

    opcion = int(input('Introduzca que desea hacer: '))


    match opcion:
        case 0:
            print('Saliendo...')
        case 1:
            nuevoIngreso = round(float(input('Introduce el valor a añadir: ')),2)
            ingresos.append(nuevoIngreso)
            print(ingresos)
        case 2:
            print(len(ingresos))
            for i, ingreso in enumerate(ingresos):
                print(f'Dia {i+1} los ingresos fueron: {ingreso}')
            dia = int(input('Introduzca el día del cuál quiere eliminar el ingreso: '))


            while dia > len(ingresos):
                print('No existe ese indice.')
                dia = int(input('Introduzca el día del cuál quiere eliminar el ingreso: '))

            del ingresos[dia]
            print(ingresos)
        case 3:
            for i, ingreso in enumerate(ingresos):
                print(f'Dia {i} los ingresos recaudados: {ingreso}€')
        case 4:
            menor = min(ingresos)
            print(f'El menor valor es: {menor}€')
            if ingresos.count(menor) >1:
                print(f'Se repite {ingresos.count(menor)} veces')
            else:
                print('Solo aparece 1 vez.')
        case 5:
            for i, ingreso in enumerate(ingresos):
                print(f'Dia {i} los ingresos fueron: {ingreso}')
            dia = int(input('Introduzca el día del cuál quiere aumentar el ingreso: '))
            while dia > len(ingresos):
                print('No existe ese indice.')
                dia = int(input('Introduzca el día del cuál quiere aumentar el ingreso: '))
            
            nuevoIngreso = round(float(input('Introduzca el valor a añadir: ')),2)

            ingresos[dia] += nuevoIngreso
        case 6:
            totalRecaudado = sum(ingresos)
            print(f'El total recaudado es {totalRecaudado}€')
        case 7:
            print(f'{sorted(ingresos)}')
            
        case 8:
            media = sum(ingresos)/len(ingresos)
            print(f'La media es: {media}€')
        case 9:
            for ingreso in ingresos:
                if ingreso >cantASuperar:
                    cantDiasMas100Euros+=1
            porcentajeDias = (cantDiasMas100Euros*100)/len(ingresos)
            print(f'El porcentaje de días que superan los 100€ es: {porcentajeDias}%')
        case 10:
            media = sum(ingresos)/len(ingresos)
            print(f'La media es: {media}€')
            for ingreso in ingresos:
                if ingreso>media:
                    listaIngresosSuperioresMedia.append(ingreso)
                else:
                    listaIngresosInferioresMedia.append(ingreso)
            print(listaIngresosSuperioresMedia)
            print(listaIngresosInferioresMedia)