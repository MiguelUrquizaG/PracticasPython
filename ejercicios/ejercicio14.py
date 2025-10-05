'''
Crea una función en python, triangulo, que reciba un número entero, e imprima un patrón como este por
pantalla. Este sería el resultado de llamar a triangulo(5)
'''

triangulo = int(input("Introduce la longitud: "))

for i in range(1,triangulo+1):
    for j in range (0,i):
        print("*", end="")
    print()

for k in range(triangulo-1,0,-1):
    for l in range (0,k):
        print("*",end="")

    print()

