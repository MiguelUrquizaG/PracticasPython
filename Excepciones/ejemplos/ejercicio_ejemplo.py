def get_int():
    isValido=False
    while(not isValido):
        try:
            numero = int(input('Introduzca un número: '))
        except ValueError:
            print('Ha habido un problema con el número introducido.')
        else:
            isValido = True
            print(f'El resultado es {numero}') 
        

get_int()