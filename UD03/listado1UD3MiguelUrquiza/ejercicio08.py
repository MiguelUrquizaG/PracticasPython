'''
Crea una función maraton_series(horas) que reciba un número de horas vistas de series y devuelva
una tupla con (dias, horas_restantes).
Ejemplo: 27 horas → (1, 3).
'''

horasVistas = int(input('Introduzca la cantidad de horas vistas: '))

def maraton_series(horas):
    dias=0
    while horas >=24:
        horas -= 24
        dias+=1
    return (dias,horas)
    

print(maraton_series(horasVistas))