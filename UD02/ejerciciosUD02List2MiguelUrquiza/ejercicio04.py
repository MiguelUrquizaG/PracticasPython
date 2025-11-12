'''
Si tenemos un diccionario para un inventario de un frutero inteligente, por ejemplo, inventario =
{"manzanas": 10, "naranjas": 5, "peras": 8}
Crear los siguientes apartados:
1. Mostrar todas las claves y valores.
2. Aumentar manzanas en 5.
3. Eliminar peras.
4. Calcular el total de frutas.
'''
inventario={"manzanas":10,"naranjas":5,"peras":12,"plátano":32}
opcion =-1
cantidadAgregar=5
cantidadTotalFrutas=0

while opcion!=0:
    print('0. Salir')
    print('1. Mostrar todas las claves y valores.')
    print('2. Aumentar manzanas en 5.')
    print('3. Eliminar peras.')
    print('4. Calcular el total de frutas.')
    opcion = int(input('Introduzca que desea hacer: '))

    match opcion:
        case 0:
            print('Saliendo...')
        case 1:
            for nombres, cantidad in inventario.items():
                print(f'Nombres: {nombres} | Cantidad: {cantidad}')
        case 2:
            inventario['manzanas'] +=cantidadAgregar
        case 3:
            del(inventario)['peras']
        case 4:
            for cantidad in inventario.values():
                cantidadTotalFrutas+=cantidad
            print(f'La cantidad total de frutas es: {cantidadTotalFrutas}')


print('Gracias por utilizar el programa.')