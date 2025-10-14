
print("Bievenido, este programa indica que número es mayor entre dos")

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))

if num1 >num2:
    print(f'El número {num1} (que es el primer número introducido) es mayor que el {num2}.')
elif num1 == num2:
    print(f'Ambos números son iguales.')
else:
    print(f'El número {num2} (que es el segundo introducido) es mayor que el {num1}.')


print("Gracias por usar el programa.")