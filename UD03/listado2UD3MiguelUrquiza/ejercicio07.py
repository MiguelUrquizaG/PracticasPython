import numpy

def calcular_cara_cruz(dinero_inicial,num_apuestas,prob_ganar,retorno_ganar,retorno_perder):
    for _ in range(num_apuestas):
        num_ganador = numpy.random.randint(0,100)
        if num_ganador <= prob_ganar:
            dinero_inicial +=retorno_ganar
        else: 
            dinero_inicial-=retorno_perder
    return dinero_inicial  

def calcular_cara_cruz_evol(dinero_inicial,num_apuestas,prob_ganar,retorno_ganar,retorno_perder):
    listaDinero=[]
    for _ in range(num_apuestas):
        num_ganador = numpy.random.rand()
        if num_ganador < prob_ganar:
            dinero_inicial +=retorno_ganar
        else: 
            dinero_inicial-=retorno_perder
        listaDinero.append(dinero_inicial)
    return listaDinero

print(calcular_cara_cruz_evol(100,5,0.5,5,5))