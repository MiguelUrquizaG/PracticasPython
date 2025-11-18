'''
Un equipo de baloncesto necesita poder guardar los triples que encestan por partido.
Para ello debes hacer lo siguiente.

1.Generar aleatorios y guardar 10 aleatorios. 
2.Añadir algun triple
3.Ver Canastas
4.Limpiar archivo
5.Añadir un número que se diga x veces que se diga.
'''
import random

triples = open('triples.txt','w')
aleatorios=[]

#Ejercicio 2
for numero in range(10):
    aleatorios.append(str(random.randint(0,12)))

for i,numero in enumerate(aleatorios):
    triples.write(numero +'\n')

triples.close()

triples = open('triples.txt','r')

print(triples.readlines())
triples.close()

#Añadir triple

triples = open('triples.txt','a')
cantTriple = input('Escriba la cantidad de triples que desea guardar: ')
triples.write(cantTriple + '\n')
triples.close()

#Ver Triples
triples = open('triples.txt','r')
print(triples.readlines())

#Limpiar Archivo
triples = open('triples.txt','w')
triples.write('')
triples.close()

triples = open('triples.txt','r')
print(triples.readlines())
triples.close()
#Añadir un número que se diga x veces que se diga.
numeroAnyadir = input('Introduzca la cantidad de canastas que desea añadir: ')
cantAnyadir = int(input('Introduzca cuántas veces quieres que se añada: '))
triples = open('triples.txt','a')
for numero in range(cantAnyadir):
    triples.write(numeroAnyadir+'\n')


triples.close()
