numPartidos = 15
cantEquiposPartido=2
equipos=[]
resultados=[]
equipo=''
temporada=[] #Habría otro for encima del primero el cual haría una temporada entera 
#la cual generaria 34 listas y dentro de esas listas se haría otra lista eon los equipos y resultados
import random

print('Este programa permite gestionar los resultados de los resultados de los partidos de fútbol.')

for i in range(0,numPartidos):
    equipos.append(['',''])
    resultados.append([0,0])
    for j in range(0,2):
        if j ==0:
            equipo = input('Introduce el nombre del equipo local del partido: ')
            equipos[i][j]=equipo
            #resultado = int(input('Introduce los goles del equipo local: '))
            resultado = random.randint(0,10)
            resultados[i][j] = resultado
        else:
            equipo = input('Introduce el nombre del equipo visitante del partido: ')
            equipos[i][j]=equipo
            #resultado = int(input('Introduce los goles del equipo visitante: '))
            resultado = random.randint(0,10)
            resultados[i][j]=resultado

print('RESULTADOS')
for i in range(numPartidos):
    print(f'PARTIDO: {i}')
    for j in range(cantEquiposPartido):
        if j ==0:
            print(equipos[i][j],resultados[i][j],' vs', end=" ")
            
        else:
            print(resultados[i][j],equipos[i][j])
        

print('Gracias por utilizar el programa.')