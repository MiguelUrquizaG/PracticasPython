import random
import math

#Primera
# def numero_mas_repetido(tiradas,max,min):
    
#     listaNums=[]
#     maxNum =min-1
#     listNumMax=[]
    
#     for _ in range(0,tiradas):
#         listaNums.append(random.randint(min,max))
    
#     print(listaNums)
#     for nums in listaNums:
#         if(listaNums.count(nums)>maxNum):
#             listNumMax=[]
#             listNumMax.append(nums)
#             maxNum = listaNums.count(nums)
#         elif(listaNums.count(nums) == maxNum and nums not in listNumMax ):
#             listNumMax.append(nums)
    
#     return listNumMax


# print(numero_mas_repetido(10,10,1))

#Segunda
# def sumatorio_nums_aleatorios(tiradas,min,max):
#     resultado = 0.0
#     for _ in range(0,tiradas):
#         resultado += random.randint(min,max)
#     return resultado

# print(sumatorio_nums_aleatorios(10,1,10))


#Tercera

# def calcular_porcentaje_numero(numero,tiradas,min,max, cantidadEstadistica):
#     listaNums = []
#     cantRepeticiones = 0

    
#     probabilidad = 0.0
    
#     for _ in range(0,tiradas):
#         listaNums.append(random.randint(min,max))
        
#     cantRepeticiones = listaNums.count(numero)
#     porcentaje = cantRepeticiones * tiradas
    
#     print(listaNums)
#     probabilidad = porcentaje*cantidadEstadistica/100
    
#     return probabilidad
    
    

# print(calcular_porcentaje_numero(5,10,1,6,80))

#Cuarta
def calcular_elevado_numero(num,tiradas,min,max):
    listNums = []
    resultado = 0.0
    for _ in range(0,tiradas):
        listNums.append(random.randint(min,max))
    
    print(listNums) 
    resultado = math.pow(num,listNums.count(num))
    return resultado

print(calcular_elevado_numero(5,10,1,6))