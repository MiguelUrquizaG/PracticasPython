'''
Queremos desarrollar un pequeño programa que ayude a un técnico meteorológico (mi amigo Nico es
meteorólogo) a analizar las temperaturas registradas durante una semana en su estación de trabajo.
- Rellenar la lista con temperaturas generadas de forma aleatoria entre dos límites leídos por teclado. Pueden
  tener decimales.
- A partir de esa lista, el programa debe:
- Mostrar todas las temperaturas introducidas.
- Calcular y mostrar la temperatura media.
- Mostrar la temperatura máxima y mínima junto con el día en que ocurrieron.
- Ordena la lista de mayor a menor temperatura.
- Mostrar cuántos días tuvieron temperaturas por encima de la media.
- Crear una nueva lista solo con las temperaturas superiores a la media.
'''

import random

numTemperaturas = 7
maxTemperaturas = float(input("Introduzca la temperatura máxima a generar: "))
minTemperaturas = float(input("Introduzca la temperatura mínima a generar: "))
contador =0

listaTemperaturas =[]
listaDias = ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
temperaturaMedia=0.0

for temperatura in range (0,numTemperaturas):
    listaTemperaturas.append(round(random.uniform(minTemperaturas,maxTemperaturas),2))

#Mostrar Todas temperaturas
print(listaTemperaturas)

#Temperatura media
temperaturaMedia = round(sum(listaTemperaturas)/len(listaTemperaturas),2)
print(temperaturaMedia)

#Mostrar la temperatura máxima y mínima junto con el día en que ocurrieron.
maxTemp = max(listaTemperaturas)
diaMaxTemp = listaDias[listaTemperaturas.index(maxTemp)]
print(f'El día con mayor temperatura fue un {diaMaxTemp} que marcó {maxTemp}ºC')

minTemp = min(listaTemperaturas)
diaMinTemp = listaDias[listaTemperaturas.index(minTemp)]
print(f'El día con menor temperatura fue un {diaMinTemp} que marcó {minTemp}ºC')

#Ordenar Lista de mayor a menor
listaTemperaturas.sort(reverse=True)
print(listaTemperaturas)

#Mostrar cuántos días tuvieron temperaturas por encima de la media
#Mi método
for temp in listaTemperaturas:
    if temp>temperaturaMedia:
        contador+=1
    else:
        break
print(contador)

'''contador = sum(1 for temp in listaTemperaturas if temp > temperaturaMedia)
print(contador)
'''
#Crear nueva lista con temperaturas superiores a la media
listaTemperaturasSuperioresMedia=[]

for temp in listaTemperaturas:
    if temp>temperaturaMedia:
        listaTemperaturasSuperioresMedia.append(temp)
    else:
        break

print(listaTemperaturasSuperioresMedia)