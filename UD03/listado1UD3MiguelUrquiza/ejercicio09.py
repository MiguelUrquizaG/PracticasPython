'''
Define una función mas_procrastina(diccionario_horas) que reciba un diccionario con pares {nombre:
horas_procrastinando} y devuelva el nombre de la persona que más horas ha procrastinado.
Si el diccionario está vacío, devuelve None.
'''

diccionario = {'Miguel':2,'Pepe':4}

def mas_procrastina (diccionario_personas):
    if len(diccionario) == 0:
        return None

    valor = max(diccionario.values())
    for nombre,hora in diccionario.items():
        if hora == valor:
            return nombre



print(mas_procrastina(diccionario))