'''Tenemos una lista de Edades  y una lista de Nombres las cuáles han sido asesinadas
 en la noche de Halloween y estamos intentando realizar ciertos cálculos estadísticos. Ambas listas tienen que ser del mismo tamaño obligatoriamente,
 ya que vamos a trabajar con ambas listas.
 - 1. Lo primero que queremos calcular si la edad media es superior a 18.
 - 2. Repasar ambas listas y si la persona tiene menos de 18 años añadirle al nombre (Menor de Edad)
 - 3. Encontrar las personas que tengan mas de 5 caracteres
 - 4. Calcular si la edad de los menores de 18 suman mas que la edad del mas mayor.
 - 5. Mostrar la edad y el nombre de la persona buscandola por nombre'''


import random

edades = [22,16,43,10,63]
nombres =["Miguel","Andrea","Raquel","Nerea","Juanma"]

#Caso 1
media=0
suma=0
topeMedia=18


for edad in edades:
    suma+=edad
    
media = suma/len(edades)

if media > topeMedia:
    print(f'La media de edad de los fallecidos es mayor a 18, la media es: {media}')
else:
    print(f'La media de edad de los fallecidos es menor a 18, la media es: {media}')


#caso2
topeEdad=18
textoCadena =' (Menor Edad)'
for edad, nombre in zip(edades,nombres):
    if edad < 18:
        textoCadena.join(nombre) 

for edad, nombre in zip(edades,nombres):
    print(nombre, edad)


#caso3
maxLetras =5
for nombre in nombres:
    if len(nombre )> maxLetras:
        print (nombre + ", tiene mas de 5 letras")

#caso4