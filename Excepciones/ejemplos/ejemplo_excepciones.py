def intdiv(a:int,b:int)-> int:
    return a//b

# print(f'{intdiv(3,0)}')
#Ejemplo con try catch

def intdiv2(a:int,b:int)->int:
    try:
        return a//b
    except:
        print('No se puede dividir entre 0.')

print(f'{intdiv2(3,0)}')

#Aunque no sea obligatorio se recomienda indicar el tipo de excepción
#Se hace igual que en java de más específico a más general.

#Ejemplo de multi catch

def intdiv3(a:int,b:int)->int:
    try:
        return a//b
    except (TypeError,ZeroDivisionError):
        print('Comprueba los números, algunos causan error.')
    else:
        print(f'El resultado es')
    # except Exception:
    #     print('Algo ha ido mal.')
    #Mirar porque no se puede acceder al else.

intdiv3(3,0)


def intdiv4(nums:list)->int:
    try:
        r=nums[3]
    except IndexError:
        print('Error con el indice')
    else:
        print(f'Your wishes are my command {r}')
    finally:
        print('Have a good day')


nums = [3,2,1]

intdiv4(nums)

def _sum(a:int,b:int)->int:
    if isinstance(a,int)and isinstance(b,int):
        return a+b
    raise TypeError('Los números tienen que ser enteros.')

print(_sum(3,'s'))

#Las aserciones es una herramienta en la que si en programa no se cumple lo que quiero me avisa.