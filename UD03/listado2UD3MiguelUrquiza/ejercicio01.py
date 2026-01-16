

precios = {20:10,4:3,1:5}

def aplicar_descuento(valor,descuento):

    descuento = valor*descuento/100

    precio = valor-descuento

    return precio

def aplicar_Iva(valor,iva):
    aumento = valor*iva/100

    precio = valor + aumento

    return precio

def calcular(precios:dict,metodo):
    total = 0.0
    for precio,porcentaje in precios.items():
       total += metodo(precio,porcentaje)

    return total


print(calcular(precios,aplicar_Iva))