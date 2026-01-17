import math

tabla = {}

valor = int( input('Introduce un valor: '))


# for num in range(1,valor+1):
#     tabla[num] = 0.0



print('1. Seno')
print('2. Coseno')
print('3. Tangente')
print('4. Exponencial')
print('5. Logaritmo Neperiano')
opcion = int(input('Introduzca que desea hacer:'))


def calculadora(valor:float,opcion):
    resultado =0.0
    match(opcion):
        case 1:
            for num in range(1,valor+1):
                resultado = math.sin(num)
                tabla[num] = resultado
        case 2:
            for num in range(1,valor+1):
                tabla[num] = math.cos(num)
        case 3: 
            for num in range(1,valor+1):
                tabla[num] = math.tan(num)
        case 4:
            for num in range(1,valor+1):
                tabla[num] = math.exp(num)
        case 5:
            for num in range(1,valor+1):
                tabla[num] = math.log(num)


calculadora(valor,opcion)


for num,valor in tabla.items():
    print(f'El número {num} su resultado es {valor}')