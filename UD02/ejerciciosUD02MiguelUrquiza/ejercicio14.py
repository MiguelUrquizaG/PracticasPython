'''
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
'''

print("Bienvenido este programa te pide una palabra y comprueba si es palíndromo.")

palabra = list(input("Introduzca la palabra: "))
palabraInversa =list(reversed(palabra))

if palabra == palabraInversa:
    print("Soy palindromo")
else:
    print("No soy palindromo")


print("Gracias por usar el programa.")