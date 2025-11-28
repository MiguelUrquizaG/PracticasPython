'''
Escribe una función filtrar_calorias (lista_comidas, max_calorias) que reciba una lista de tuplas
(nombre_comida, calorías) y devuelva una nueva lista solo con las comidas cuya cantidad de calorías
sea menor o igual que max_calorias. Si la lista está vacía, devuelve una lista vacía.
'''

lista = [('Macarrones',200),('Patatas',300)]
max=int(input('Introduzca el máximo de calorías: '))


def filtrar_calorias(lista_comidas,max_calorias):
    nuevaLista = []
    for comida in lista:
        nombre, calorias = comida
        if calorias <= max:
            nuevaLista.append(comida)
    return nuevaLista


print(filtrar_calorias(lista,max))