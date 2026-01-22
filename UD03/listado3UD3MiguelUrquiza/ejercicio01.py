#120.5 cal x 100ml  Metodo calcular calorías segun tamaño
#Los yogures desnatados tienen un 30% menosde calorías.
#Postres de proteína mismas calorías que uno normal más parte proteica.
#Crear método para calcular calorías de un yogur y otro para calcular un conjunto de yogures.
#Otro que calcule solo las calorías aportadas por uno de los tipos.


class Yogur:
    def __init__(self,calorias:float,sabor:str,marca:str,trocitos:bool):
        
        self.calorias = calorias
        self.sabor = sabor
        self.marca = marca
        self.trocitos = trocitos
    def calcular_calorias(self,cantidad:float):
        valorEstandar = 100.0
        return cantidad*(self.calorias/valorEstandar)
    
    
class YogurDesnatado(Yogur):
    def __init__(self, calorias, sabor, marca, trocitos,porcentaje:float,calorias_desnatadas:float):
        self.porcentaje = porcentaje
        self.calorias_desnatadas = calorias_desnatadas
        super().__init__(calorias, sabor, marca, trocitos)
    def  calcular_calorias(self,cantidad,porcentaje):
     base = 100.0
     self.calorias_desnatadas =  super().calcular_calorias(cantidad) - super().calcular_calorias(cantidad)*self.porcentaje/base
     return self.calorias_desnatadas
    

class PostresProteinas(Yogur):
    def __init__(self, calorias, sabor, marca, trocitos,cantidad_proteica:float,calorias_proteicas:float):
        self.cantidad_proteica = cantidad_proteica
        self.calorias_proteicas  = calorias_proteicas
        super().__init__(calorias, sabor, marca, trocitos)
    def calcular_calorias(self, cantidad):
        self.calorias_proteicas = super().calcular_calorias(cantidad) +self.cantidad_proteica
        return self.calorias_proteicas

yogur = Yogur(120.5,'Plátano','Danone',True)
yogurDesnatado = YogurDesnatado(120.5,'Freasa','Pascual',False,30,0)
postreProteico = PostresProteinas(120.5,'Pera','Pascual',False,100,0)


class CalculadoraYogures:
    def __init__(self,yogur:Yogur):
        self.yogur = yogur
        pass
    def calcular_caloria_yogur(self,cantidad,):
        #mirar subclass
        if isinstance(YogurDesnatado):
            return self.yogur.calcular_calorias(cantidad)
        elif isinstance(PostresProteinas):
            return self.calcular_caloria_yogur(cantidad)
        elif isinstance(Yogur):
            return self.calcular_caloria_yogur(cantidad)
print(f'El resultado es: {yogur.calcular_calorias(100)}')
print(f'Las calorías desnatadas son {yogurDesnatado.calcular_calorias(100)}')
print(f'El postre de proteínas tiene {postreProteico.calcular_calorias(100)}')
