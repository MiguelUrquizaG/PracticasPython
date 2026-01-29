from __future__ import annotations

class Yogur():
    calorias = 120.5
    referencia = 100.0
    def __init__(self,sabor:str,marca:str,trocitos:bool):
        self.sabor = sabor
        self.marca = marca
        self.trocitos = trocitos
    
    def __eq__(self, yogur:"Yogur",tamanyo,porcentaje,proteinas):
        return self.calcular_calorias(tamanyo,porcentaje,proteinas) == yogur.calcular_calorias(tamanyo,porcentaje,proteinas)
        
    def calcular_calorias(self,tamanyo:float,porcentaje:float,proteinas:float):
        return (tamanyo*self.calorias)/self.referencia


class Yogur_Desnatado(Yogur):
    def __init__(self, sabor, marca, trocitos):
        super().__init__(sabor, marca, trocitos)

    def calcular_calorias(self, tamanyo,porcentaje,proteinas):
        base = 100
        total = super().calcular_calorias(tamanyo,porcentaje,proteinas)
        total -= (total*porcentaje)/base
        return total

class Postres_Proteinas(Yogur):
    def __init__(self, sabor, marca, trocitos):
        super().__init__(sabor, marca, trocitos)

    def calcular_calorias(self, tamanyo,porcentaje,proteinas)->float:
        return super().calcular_calorias(tamanyo,porcentaje,proteinas) + proteinas
    
    
class GestorYogures():
    def __init__(self):
        pass
    def calcular_calorias_yogur(self,yogur:Yogur,tamanyo:float,porcentaje:float,proteinas:float)->float:
        return yogur.calcular_calorias(tamanyo,porcentaje,proteinas)
    def calcular_lista_yogures(self,yogures:list[Yogur],tamanyo:float,porcentaje:float,proteinas:float) ->float:
        total = 0.0
        for yogur in yogures:
            total+=yogur.calcular_calorias(tamanyo,porcentaje,proteinas)
        return total
    def calcular_tipo(self,yogures:list[Yogur],tipo:str,tamanyo:float,porcentaje:float,proteinas:float)->float:
        total =0.0
        tipoSeleccionad =''
        if tipo == 'yogur':
            tipoSeleccionad = Yogur
        elif tipo == 'desnatado':
            tipoSeleccionad = Yogur_Desnatado
        else:
            tipoSeleccionad = Postres_Proteinas
            
        for yogur in yogures:
            if isinstance(yogur,tipoSeleccionad):
                total += yogur.calcular_calorias(tamanyo,porcentaje,proteinas)
        return total
        

def decorador_tamanyo(func):
    def wrapper(*args,**kwargs):
        valor_peso = kwargs.get('tamanyo')
        valor_min = kwargs.get('min')
        if(valor_peso<valor_min):
            return f'El peso es menor que el de un Petit'
        return func(*args,**kwargs)
    return wrapper

def decorar_tipo(func):
    def wrapper(*args,**kwargs):
        if kwargs.get('tipo')==Postres_Proteinas:
            return f'Esto es un postre proteinas'
        return func(*args,**kwargs)
    return wrapper

@decorador_tamanyo   
def validar_tamanyo(min:float,tamanyo:float):
    return f'El tamaño de tu yogur es: {tamanyo}'

@decorar_tipo
def tipo_yogur(tipo):
    return f'Es un Yogur'

yogur = Yogur('Caramelo','Danone',False)
yogu2 = Yogur('Migas','Pepito',False)
yogur_desnatado = Yogur_Desnatado('Papas','PAscual',True)
postre_proteinas = Postres_Proteinas('Pan','Danacol',False)
gestor_Yogures = GestorYogures()

lista_yogures = [yogur,yogur_desnatado,postre_proteinas]

print(yogur.calcular_calorias(100,30,100))
print(yogur_desnatado.calcular_calorias(100,30,30))
print(postre_proteinas.calcular_calorias(100,30,30))

print(f'Gestor Yogures 1 solo yogur: {gestor_Yogures.calcular_calorias_yogur(postre_proteinas,100,30,100)}')

print(f'Gestor Yogures multiples: {gestor_Yogures.calcular_lista_yogures(lista_yogures,100,30,30)}')

print(f'Gestor Yogures tipo: {gestor_Yogures.calcular_tipo(lista_yogures,'proteinas',100,30,30)}')

print(f'Prueba Wrapper: {validar_tamanyo(min=2,tamanyo=5)}')

print(f'Prueba Wrapper tipo: {tipo_yogur(tipo=Yogur_Desnatado)}')

print(f'Prueba Equals:{yogur.__eq__(yogu2,100,20,50)}')