def calcular_hipoteca(dineroPedido,anyos):
    interes = 0.03
    meses = anyos*12
    interes_mensual = interes/12
    
    cuota = (dineroPedido/meses) + dineroPedido*interes_mensual
    
    
    deuda = dineroPedido
    cantIntereses=0.0
    
    for mes in range(meses):
        interes_mes = deuda * interes_mensual
        amortizacion = cuota - interes_mes
        deuda -= amortizacion
        cantIntereses += interes_mes
        
    if(deuda<0):
        deuda = 0
    return cuota, cantIntereses, deuda


cuota, cantIntereses,deuda = calcular_hipoteca(100000,20)

print(f'Cuota: {cuota}, Intereses: {cantIntereses}, Deuda:{deuda}')
    