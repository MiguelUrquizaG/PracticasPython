'''
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre
0 y 10). A continuación, debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
'''
notas=[]
contador=0
maxVeces=5

notasMaximas=[]
cantNotasMaximas=0

while(contador<maxVeces):
    notaAnyadida=float(input("Introduzca una de sus notas: "))
    if notaAnyadida<0 or notaAnyadida>10:
        print("Introduzca otro número válido")
        continue
    notas.append(notaAnyadida)
    contador+=1

listaInvertida = sorted(notas,reverse=True)
print(listaInvertida)
numMax = listaInvertida[0]
for nota in notas:
    if nota == numMax:
        cantNotasMaximas+=1
    
print(f'La nota máxima es: {numMax} y se repite {cantNotasMaximas} veces')


print(notas)