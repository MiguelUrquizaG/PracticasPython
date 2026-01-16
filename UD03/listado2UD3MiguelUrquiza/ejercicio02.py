import math


def calculadora(valor:float,funcion):
    resultado =0.0
    tabla = {}
    match(funcion):
        case 1:
            for num in range(0,valor):
             resultado = math.sin(valor)
            

