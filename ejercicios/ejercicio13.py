'''
Implementa una función que calcule el factorial de un número. Recuerda que el factorial de un número es
el producto de todos los números desde ese número hasta 1. Por ejemplo, el factorial de 3, 3!, es 6
'''

num = int(input("Introduzca el número para realizar el factorial: "))
factorial=num
numARestar = num -1

while numARestar is not 0:
    
    factorial *= numARestar
    numARestar -= 1
    

print(f'El factorial de {num} es {factorial}')
