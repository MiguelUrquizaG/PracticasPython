print("Bievenido, este programa indica entre que números está el indicado.")

num1 = int(input("Introduzca un número: "))

if num1 >= 0 and num1<=10:
    print(f'El número está entre 0 y 10 y es: {num1}')
else:
    print(f'El número no está entre 0 y 10 y es: {num1}')

print("Gracias por usar el programa.")