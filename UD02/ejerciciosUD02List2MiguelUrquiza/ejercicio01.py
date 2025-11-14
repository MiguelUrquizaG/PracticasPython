'''
Dada la tupla temperaturas = (21, 24, 19, 30, 25, 28). Crear el código necesario para:
1. Mostrar el valor máximo y mínimo.
2. Calcular la temperatura media.
3. Convertir la tupla en lista, añadir una nueva temperatura y volver a convertir a tupla.
4. Comprobar si 30 está presente.
'''

temperaturas=(21,24,19,30,25,28)
valorMaximo=0
valorMinimo=0
temperaturaMedia=0.0
opcion = -1
while opcion!=0:
    print('0. Salir')
    print('1. Mostrar máximo y mínimo')
    print('2. Calcular temperatura media')
    print('3. Convertir lista añadir temperatura y volver a lista')
    print('4. Comprobar si la temperatura 30 está en la lista.')
    opcion = int(input('Introduzca la opción que desea hacer: '))
    match opcion:
        
        case 0:
            print('Saliendo...')
        case 1:
            valorMaximo = max(temperaturas)
            valorMinimo=min(temperaturas)
            print(f'El valor máximo es: {valorMaximo}')
            print(f'El valor mínimo es: {valorMinimo}')
        case 2:
            temperaturaMedia = sum(temperaturas)/len(temperaturas)
            print(f'La temperatura media: {temperaturaMedia}ºC')
        case 3:
            temperaturas = list(temperaturas)
            temperaturas.append(float(input('Introduzca la temperatura que desea añadir: ')))
            temperaturas = tuple(temperaturas)
            print(temperaturas)
        case 4:
            if 30 in temperaturas:
                print('30 SI está en la lista de temperaturas.')
            else:
                print('30 SI está en la lista de temperaturas.')
        