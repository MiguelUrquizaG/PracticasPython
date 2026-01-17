inmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]




def busqueda_inmuebles(listaInmuebles,precio):
    lista_filtrada=[]
    resultado = 0.0
    for inmueble in listaInmuebles:
        resultado = calculo(inmueble)
        if(resultado <= precio):
            inmueble['precio'] = resultado
            lista_filtrada.append(inmueble)
    
        
    
    return lista_filtrada
        



def calculo(inmueble):
    precio = 0.0
    multiplicadorMetros = 1000
    multiplicadorHab = 5000
    multiplicadorGaraje = 15000
    mutiplicadorZonaB = 1.5
    
    if(inmueble['zona'] == 'A' and  inmueble['garaje']):
        antiguedad = 2026 - inmueble['año']
        precio = (inmueble['metros'] * multiplicadorMetros + inmueble['habitaciones']*multiplicadorHab+inmueble['garaje']*multiplicadorGaraje) * (1-antiguedad/100) 
    elif(inmueble['zona'] == 'A' and  not inmueble['garaje']):
        antiguedad = 2026 - inmueble['año']
        precio = (inmueble['metros'] * multiplicadorMetros + inmueble['habitaciones']*multiplicadorHab) * (1-antiguedad/100)
    elif(inmueble['zona'] == 'B' and inmueble['garaje']):
        antiguedad = 2026 - inmueble['año']
        precio = (inmueble['metros'] * multiplicadorMetros + inmueble['habitaciones']*multiplicadorHab+inmueble['garaje']*multiplicadorGaraje) * (1-antiguedad/100) * mutiplicadorZonaB
    else:
        antiguedad = 2026 - inmueble['año']
        precio = (inmueble['metros'] * multiplicadorMetros + inmueble['habitaciones']*multiplicadorHab) * (1-antiguedad/100) * mutiplicadorZonaB
    return precio





print(busqueda_inmuebles(inmuebles,90000))