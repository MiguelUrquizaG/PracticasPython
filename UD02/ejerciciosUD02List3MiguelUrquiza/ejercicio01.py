
listaRecaudado = [150.2,1000.0,100.0,200.0,200.0,300.0,223.3,32.3]
opcion =-1
totalRecaudado=0.0
maxRecaudado=0.0
media =0.0
cantDias=30
porcentajeDiasOcupados=0.0
base =100.0
corteLista=5
indiceBuscado=0

lista1=[]
lista2=[]

print('Bienvenido este programa funciona como gestor de recaudado en un apartamento turístico.')

while opcion !=0:
    opcion = int(input('Indique que desea hacer: '))
    print('0. Salir')
    print('1. Agregar una nueva recaudación')
    print('2. Poner a cero una recaudación')
    print('3. Imprimir toda la lista')
    print('4. Buscar el día en que más he ganado y decir cuántos días he ganado esa cantidad.')
    print('5. Sumar una cantidad a un día como gasto extra')
    print('6. Calcular cuánto he recaudado en todas las recaudaciones.')
    print('7. Ordenar la lista de mayor a menor.')
    print('8. Calcular la media diaria.')
    print('9. Calcular el porcentaje de días al mes (suponiendo 30 días) en que he tenido la habitación alquilada.')
    print('10. Dividir la lista en dos nuevas listas. Una de ellas debe ser la que tenga las 5 menores recaudaciones, la otra las restantes.')

    match opcion:
        case 0:
            print('Saliendo...')
        case 1:
            listaRecaudado.append(float(input('Indique lo recaudado: ')))
        case 2:
            for i,recaudado in enumerate(listaRecaudado):
                print(f'{i}: {recaudado}')
            listaRecaudado[int(input('Indique que el indice que desee poner en 0: '))] = 0.0
            print(listaRecaudado)
        case 3:
            for i,recaudado in enumerate(listaRecaudado):
                print(f'Cliente {i+1}: {recaudado}€')
        case 4:
            maxRecaudado=max(listaRecaudado)
            print(f'Lo máximo recaudado ha sido: {maxRecaudado} el día {listaRecaudado.index(maxRecaudado)} se ha repetido {listaRecaudado.count(maxRecaudado) -1} vez/veces aparte de la ya indicada.')
        case 5:
            for i,recaudado in enumerate(listaRecaudado):
                print(f'{i}: {recaudado}')
            indiceBuscado = int(input('Indique que el indice que sumar recaudación: '))
            if indiceBuscado >= len(listaRecaudado):
                print('Valor no encontrado.')
            else:
                listaRecaudado[indiceBuscado] += float(input('Introduce la cantidad que desea introducir: '))
                print(listaRecaudado)
        case 6:
            totalRecaudado = sum(listaRecaudado)
            print(f'El total recaudado es: {totalRecaudado}€')
        case 7:
            listaRecaudado.sort(reverse=True)
            print(listaRecaudado)
        case 8:
            media = sum(listaRecaudado)/len(listaRecaudado)
            print(f'La media recaudada es: {media}€')
        case 9:
            porcentajeDiasOcupados = round((len(listaRecaudado)*base)/cantDias,2)
            print(f'El porcentaje de días ocupados (sobre 30) es: {porcentajeDiasOcupados}%')
        case 10:
            listaRecaudado.sort()
            lista1 = listaRecaudado[:corteLista+1]
            lista2 = listaRecaudado[corteLista:] 
            print(f'Lista con los 5 valores mas pequeños: {lista1}')
            print(f'Lista con el resto de valores: {lista2}')

print('Gracias por utilizar el programa.')