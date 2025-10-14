''' Escribe un programa que sea capaz de escribir los N primeros números de la sucesión de fibonacci.
1. Input cantidad de veces

lastNum guardado

'''

N = int(input("Introduce la cantidad de veces: "))
resultado= 0;
num0=0
num1=1
contador=0
listFibonacci=[0]

while N>contador:

    resultado = num0+num1
    #print(resultado)
    listFibonacci.append(resultado)
    num0=num1
    num1=resultado

    contador+=1

print(listFibonacci)