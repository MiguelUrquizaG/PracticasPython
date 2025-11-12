'''
18. De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros
que conducen cada día de la semana.
Para guardar esta información se van a utilizar dos arreglos:
• Nombre: Lista para guardar los nombres de los conductores.
• kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor.
Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.
'''
import random

nombreConductores=[]
kms=[]
max=0.0
min=0.0
nombre =''
total_kms=[]
suma=0
cantDiasSemana=7

while nombre!='0':
    print("Pulse 0 para parar.")
    nombre = input("Introduzca el nombre del conductor: ")
    if nombre!='0':
        nombreConductores.append(nombre)

max = float(input("Introduce el valor máximo de kms: "))
min = float(input("Introduce el valor mínimo de kms: "))
#Se puede poner como int para que redondee
for i in range(0,len(nombreConductores)):
    kms.append([0]*cantDiasSemana)
    for j in range(cantDiasSemana):
        kms[i][j] = round(random.uniform(min,max),2)


print(kms[0])

for i in range(0,len(kms)):
    suma=0
    for j in range(len(kms[i])):
        suma+=kms[i][j]
    
    total_kms.append(round(suma,2))

print(total_kms)

for nombre,kilometros in zip(nombreConductores,total_kms):
    print(f'El conductor {nombre} ha realizado {kilometros}')

print("Gracias por utilizar el programa")