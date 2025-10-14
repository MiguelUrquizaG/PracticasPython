
print("Bienvenido, este programa te indica entre que número está el que has introducido")

num1 = int(input("Introduzca un número: "))

if num1 >= 0 and num1<=10:
    print(f'El número está entre 0 y 10 y es: {num1}')
elif num1>10 and num1<=20:
    print(f'El número está entre 11 y 20 y es: {num1}')
elif num1>20 and num1<=30:
    print(f'El número está entre 21 y 30 y es: {num1}')
else:
    print(f'El número no está entre 0 y 10 y es: {num1}')


print("Gracias por utilizar el programa.")