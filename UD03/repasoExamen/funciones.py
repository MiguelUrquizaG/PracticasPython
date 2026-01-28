#FUNCIONES
#--------------------------------
#Invocar una función
def say_hello():
    print('Holaaa')

say_hello()

#--------------------------------
#Retornar valor

def retornar_valor():
    return 1

print(retornar_valor())

#--------------------------------
#Retornando múltiples valores
def retornar_multiples_valores():
    return 0,4

a , b=retornar_multiples_valores()
print(a)
print(b)

#--------------------------------
#Parámetros y argumentos
def sqrt(value):
    return value **(1/2)

print(sqrt(4))

def _min(a,b):
    if(a<b):
        return a
    return b

print(min(8,5))
#--------------------------------
#Argumentos posicionales
def build_cpu(vendor,num_cores,freq=2.0):
    return dict(
        vendor = vendor,
        num_cores = num_cores,
        freq = freq
    )


print(build_cpu('Asus',5,200))

#--------------------------------
#Argumentos nominales
print(build_cpu(freq=20,vendor='Nvidia',num_cores=2))
#--------------------------------
#Argumentos posicionales y nominales
print(build_cpu('Rogue',freq=222,num_cores=1))
#--------------------------------
#Argumentos mutables e inmutables.
valores = [2,3,4]
def square (values):
    lista = values
    for i in range(len(lista)):
        lista[i] = lista[i]**2
    
    return lista

print(square(values=valores))

#--------------------------------
#Parámetros por defecto
print(build_cpu('Prueba',2))

