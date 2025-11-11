'''
Dada la tupla productos = ("pan", "leche", "huevos", "queso")
1. Mostrar el primer y último elemento.
2. Contar cuántas veces aparece un producto (elige uno).
3. Convertir a lista, modificar un elemento y volver a tupla.
4. Añadir un nuevo producto (tupla concatenada).
'''

productos = ("pan","leche","huevos","queso")
cantVecesPalabra=0
productoABuscar=''
productoAAgregar=''
nuevoProducto=()
opcion = -1

while opcion !=0:

    print('0. Salir')
    print('1. Mostrar el primer y último elemento.')
    print('2. Contar cuántas veces aparece un producto (elige uno).')
    print('3. Convertir a lista, modificar un elemento y volver a tupla.')
    print('4. Añadir un nuevo producto (tupla concatenada).')
    opcion = int(input('Introduzca que desea hacer: '))

    match opcion:
        case 0:
            print('Saliendo...')
        case 1:
            print(f'La primera palabra es: {productos[0]} y la última es {sorted(productos,reverse=True)[0]}')
        case 2:
            productoABuscar = input('Introduzca la palabra que desea buscar: ')
            if productoABuscar in productos:
                print(f'La cantidad de veces que sale {productoABuscar} es: {productoABuscar.count(productoABuscar)}')
            else:
                print(f'{productoABuscar} no se encuentra en la lista.')
        case 3:
            productos = list(productos)
            productoABuscar = input('Indica la palabra que deseas modificar: ')
            if productoABuscar in productos:
                print(f'La palabra a cambiar es: {productoABuscar}')
                productos[productos.index(productoABuscar)] = input('Indica como quieres modificarla: ')
            else:
                print('No se encuentra esa palabra en la lista.')
            productos = tuple(productos)
            print(productos)
        case 4:
            productoAAgregar = input('Introduzca la palabra que desea agregar: ')
            nuevoProducto = (productoAAgregar,)
            productos += nuevoProducto

            print(productos)







