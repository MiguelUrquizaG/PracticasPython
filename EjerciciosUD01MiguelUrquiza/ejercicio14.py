'''
Crea una función en python, triangulo, que reciba un número entero, e imprima un patrón como este por
pantalla. Este sería el resultado de llamar a triangulo(5)
'''
'''
print("Bienvenido, este programa genera un triángulo en base a la medida que le digas")

triangulo = int(input("Introduce la longitud: "))

for i in range(1,triangulo+1):
    for j in range (0,i):
        print("*", end="")
    print()

for k in range(triangulo-1,0,-1):
    for l in range (0,k):
        print("*",end="")

    print()


for i in range(0,triangulo):
    print("*"*i)

for j in range(triangulo,0,-1):
    print("*" *j)
'''
import math
serial_number = '\n\t \n  Hola\t\n 48374983274832  \n\n\t \t \n'

print(serial_number.strip('\n'))

print(math.pow(3,2))
age=16
match age:
    case j if j<17:
        print("Menor")
    case _ :
        print("Mayor")

texto ="Hola, me llamo Miguel, y soy programador"

print(texto.split(","))
'''
print("Gracias por utilizar el programa")
'''