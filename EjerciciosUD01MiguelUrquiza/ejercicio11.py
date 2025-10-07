'''
Escribe un programa que pida primero un número entero y después pida números enteros hasta que la suma
de los números introducidos coincida con el número inicial. El programa termina escribiendo la lista de
números.
'''
import time

print("Bienvenido al programa")

numInicial = int(input("Introduce el número a alcanzar: "))
sumaNumeros=0;
listaNums =[]
#numAnyadido= int(input("Introduce un número: "))

while sumaNumeros is not numInicial:
    numAnyadido = int(input("Introduce un número: "))
    sumaNumeros +=numAnyadido 

    #Hay que obligar a llegar al número

    if sumaNumeros > numInicial:
        print("Has superado el número original")
        print("Te redirijo al inicio")
        sumaNumeros-=numAnyadido
        print("Valor actual de suma --> ",sumaNumeros)
        
        #break
    else:
        listaNums.append(numAnyadido)

print("--------------------------------------------------------")
if sumaNumeros is numInicial:
    print(f'Has alcanzado el objetivo')
    print(f'El listado de números es: {listaNums}')
    print(f'El número a alcanzar era {numInicial}')

'''else:
    print(f'Superaste el número inicial {numInicial}.')
    print(f'El resultado de la suma tus números ha sido --> {sumaNumeros}')
    print(f'La lista es {listaNums}')
    '''