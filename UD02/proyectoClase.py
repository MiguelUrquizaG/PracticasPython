provincias =['Almería','Cádiz','Córdoba','Granada','Huelva','Jaén','Málaga','Sevilla']
print(f'Lista {provincias}')
print("-------------------------------------------------------------------------------------------------------------")
provincias.remove('Córdoba')

print(f'Lista borrando provincia sin costa {provincias}')
print("-------------------------------------------------------------------------------------------------------------")
provincias.sort()
print(f'Lista ordenada alfabéticamente {provincias}')
print("-------------------------------------------------------------------------------------------------------------")
provincias.insert(0,'Granada')
print(f'Lista tras agregar nuestra favorita {provincias}')
print("-------------------------------------------------------------------------------------------------------------")
provincias[3:5] = []
print(f'Lista tras eliminar las dos del centro {provincias}')
print("-------------------------------------------------------------------------------------------------------------")
lista=['Granada']*2
provincias = lista + provincias
print(f'Lista tras eliminar las dos del centro {provincias}')
print("-------------------------------------------------------------------------------------------------------------") 
numero =0
for provincia in provincias:
    
    if provincias.count(provincia) >numero:
        numero = provincias.count(provincia)

print(f'Número de veces que se repite la ciudad más escrita {numero}')
print("-------------------------------------------------------------------------------------------------------------") 
del provincias[numero]
print(f'Lista tras eliminar la provincia con índice igual a la cantidad de veces que se repite la ciudad con mas repeticiones {provincias}')
print("-------------------------------------------------------------------------------------------------------------") 
provincias.reverse()
print(f'Lista tras invertirla {provincias}')
print("-------------------------------------------------------------------------------------------------------------") 
provincias[5:7]=[]
print(f'Lista tras borrar las dos ultimas {provincias}')