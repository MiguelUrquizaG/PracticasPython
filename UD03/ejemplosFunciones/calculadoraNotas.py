notas = {'6.1':[8.5,10],'6.2':[8.75],'6.3':[10]}

def calcular_media(diccionarioNotas:dict):
    mediaTotal =0
    media1=0
    media2=0
    media3=0

    for criterio,nota in notas.items():
        for notaIndividual in nota:
            media += notaIndividual
    
    return media


print(calcular_media(notas))
print(type(notas.values()))
