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
print("Caso 1")
print("-----------------------------------------------------")
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

print("-----------------------------------------------------")
#caso2
print("Caso 2")
print("-----------------------------------------------------")
topeEdad=18
textoCadena =' (Menor Edad)'
for i,(edad, nombre) in  enumerate(zip(edades,nombres)):
    if edad < 18:
        nombre = nombre + textoCadena
        nombres[i] = nombre
        print(nombre)

for edad, nombre in zip(edades,nombres) :
    print(nombre, edad)

print("-----------------------------------------------------")
#caso3
print("Caso 3")
print("-----------------------------------------------------")
maxLetras =5
for nombre in nombres:
    if len(nombre )> maxLetras:
        print (nombre + ", tiene mas de 5 letras")
print("-----------------------------------------------------")
#caso4
print("Caso 4")
print("-----------------------------------------------------")
sumaEdades=0
for edad in edades:
    if edad <18:
        sumaEdades+=edad

if sumaEdades > max(edades):
    print("La suma de la edad de los menores es mayor que la del mas mayor")
    print(f'Suma edades menores {sumaEdades}')
    print(f'Edad más mayor: {max(edades)}')
elif sumaEdades <max(edades):
    print("La suma de la edad de los menores es menor que la del mas mayor")
    print(f'Suma edades menores {sumaEdades}')
    print(f'Edad más mayor: {max(edades)}')
else:
    print("Son iguales")
    print(f'Suma edades menores {sumaEdades}')
    print(f'Edad más mayor: {max(edades)}')

print("-----------------------------------------------------")
#caso 5
print("Caso 5")
print("-----------------------------------------------------")
nombreBuscado = input("Introduzca el nombre del que quiere saber la edad: ")

for nombre, edad in zip(nombres,edades):
    if nombreBuscado == nombre:
        print(f'El nombre es: {nombre}')
        print(f'Su edad es: {edad}')
        break