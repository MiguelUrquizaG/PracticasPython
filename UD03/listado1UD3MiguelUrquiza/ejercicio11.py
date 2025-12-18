'''
Crea una función estado_bateria(porcentaje) que:
- Devuelva "Perfecto" si porcentaje está entre 80 y 100.
- Devuelva "Aceptable" entre 30 y 79.
- Devuelva "Modo ahorro YA" entre 10 y 29.
- Devuelva "Busca un enchufe" si es menor que 10
'''

def estado_bateria(porcentaje):
    porcentajePerfecto = porcentaje<=100 and porcentaje>=80
    porcentajeAceptable=porcentaje<=79 and porcentaje>=30
    porcentajeBajo = porcentaje<=29 and porcentaje >=10
    porcentajeMinimo = porcentaje<10

    match porcentaje:
        case porcentaje if porcentajePerfecto:
            return 'Perfecto'
        case porcentaje if porcentajeAceptable:
            return 'Aceptable'
        case porcentaje if porcentajeBajo:
            return 'Modo ahorro SHA'
        case porcentaje if porcentajeMinimo:
            return 'Busca un enchufe'
        

print(estado_bateria(85))