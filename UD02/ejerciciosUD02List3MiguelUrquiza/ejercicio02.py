diccionario={
    'cabeza':'amigo',
    'aro':'circunferencia | claro, sí'
    }

clave=''
valor=''
palabraBuscada=''
palabraModificar = ''
opcion =-1
palabrasFavoritas={}

print('Bienvenido al programa')
while opcion!=0:
    print('0. Salir')
    print('1. Añadir una nueva palabra')
    print('2. Imprimir diccionario')
    print('3. Buscar palabra')
    print('4. Modificar palabra')
    print('5. Añadir palabras favoritas al diccionario.')
    print('6. Eliminar palabra')
    print('7. Ordenar lista alfabéticamnte')

    opcion = int(input('Introduzca lo que desea realizar: '))

    match opcion:
        case 0:
            print('Saliendo')
        case 1:
            clave = input('Introduzca la palabra que desea introducir: ')
            valor = input(f'Introduzca el significado de la palabra {clave}: ')
            diccionario[clave]=valor
        case 2:
            for palabra, significado in diccionario.items():
                print(f'{palabra} -> {significado}')
        case 3:
            palabraBuscada = input('Introduzca la palabra de la cuál quiere saber el significado: ')
            significadoPalabraBuscada =diccionario.get(palabraBuscada,'La palabra buscada no existe en el diccionario o está mal escrita.')
            print(significadoPalabraBuscada)
        case 4:
            for palabra, significado in diccionario.items():
                print(f'{palabra}: {significado}')
            
            palabraBuscada = input('Introduzca la palabra a la cuál le desea cambiar el significado: ')
            if palabraBuscada  not in diccionario:
                print('Palabra no existente')
            else:
                nuevoValor = input(f'Indica el nuevo significado que le quieres dar : ')
                diccionario[palabraBuscada] = nuevoValor
                for palabra, significado in diccionario.items():
                    print(f'{palabra}: {significado}')
        case 5:
            while len(palabrasFavoritas)<2:
                clave = input('Introduzca la palabra que desea añadir: ')
                valor = input('Introduzca el significado de esta palabra: ')
                palabrasFavoritas[clave] = valor
                #palabrasFavoritas={clave:valor}
            
            diccionario.update(palabrasFavoritas)
        case 6:
            valor = input('Introduzca la palabra que desee eliminar: ')
            if valor in diccionario:
                del diccionario[valor]
            else:
                print('Esa palabra no se encuentra en el diccionario.')
        case 7:
            for palabra,significado in sorted(diccionario.items()):
                print(f'{palabra}: {significado}')
