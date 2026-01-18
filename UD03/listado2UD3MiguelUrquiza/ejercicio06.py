import random

def calcular_martin_gala(cantidadDinero,apuesta,probabilidadGanar,objetivo_dinero)-> bool:
    ganado=False
    apuesta__actual=apuesta
    resultado =False
    while(objetivo_dinero !=cantidadDinero and cantidadDinero>apuesta__actual):
        ganado = False
        while(not ganado and cantidadDinero >apuesta__actual):
            cantidadDinero -= apuesta__actual
            print('Apuesta Actual: ',apuesta__actual)
            num_ganador = random.randint(0,100)
            if num_ganador <=probabilidadGanar:
                ganado = True
                cantidadDinero+=apuesta__actual*2
                apuesta__actual = apuesta
            else:
                apuesta__actual*=2
            print('Num Ganador',num_ganador) 
            print('Dinero: ',cantidadDinero)
            print('-------------------------------------------')
    
    
    if objetivo_dinero == cantidadDinero:
        resultado = True
    return resultado


if calcular_martin_gala(100,10,48,1000):
    print(f'Enhorabuena has ganado')
else:
    print(f'Has perdido')
    