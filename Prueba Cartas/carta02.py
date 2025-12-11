palabras = ['palabra','prueba','acabar','final']

def acabadas_vocal(listPalabra):
    vocales = ('a','e','i','o','u')
    base = 100.0
    cantPalabras =0
    for palabra in palabras:
        if palabra.endswith(vocales):
            cantPalabras +=1
    return (cantPalabras*base)/len(palabras)
    

print(acabadas_vocal(palabras))