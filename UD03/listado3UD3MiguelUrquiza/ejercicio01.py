#120.5 cal x 100ml  Metodo calcular calorías segun tamaño
#Los yogures desnatados tienen un 30% menosde calorías.
#Postres de proteína mismas calorías que uno normal más parte proteica.
#Crear método para calcular calorías de un yogur y otro para calcular un conjunto de yogures.
#Otro que calcule solo las calorías aportadas por uno de los tipos.


class Yogur:
    def __init__(self,calorias:float,sabor:str,marca:str,trocitos:bool,cantidad:float):
        
        self.calorias = calorias
        self.sabor = sabor
        self.marca = marca
        self.trocitos = trocitos
        self.cantidad = cantidad
    def calcular_calorias(self):
        valorEstandar = 100.0
        return self.cantidad*(self.calorias/valorEstandar)
    
    
class YogurDesnatado(Yogur):
    def __init__(self, calorias, sabor, marca, trocitos,cantidad,porcentaje:float,calorias_desnatadas:float):
        self.porcentaje = porcentaje
        self.calorias_desnatadas = calorias_desnatadas
        super().__init__(calorias, sabor, marca, trocitos,cantidad)
    def  calcular_calorias(self):
        base = 100.0
        self.calorias_desnatadas =  super().calcular_calorias() - super().calcular_calorias()*self.porcentaje/base
        return self.calorias_desnatadas
    

class PostresProteinas(Yogur):
    def __init__(self, calorias, sabor, marca, trocitos,cantidad,cantidad_proteica:float,calorias_proteicas:float):
        self.cantidad_proteica = cantidad_proteica
        self.calorias_proteicas  = calorias_proteicas
        super().__init__(calorias, sabor, marca, trocitos,cantidad)
    def calcular_calorias(self):
        self.calorias_proteicas = super().calcular_calorias() +self.cantidad_proteica
        return self.calorias_proteicas

yogur = Yogur(120.5,'Plátano','Danone',True,100)
yogurDesnatado = YogurDesnatado(120.5,'Freasa','Pascual',False,100,30,0)
postreProteico = PostresProteinas(120.5,'Pera','Pascual',False,100,100,0)


class CalculadoraYogures:
    def __init__(self,yogur:Yogur):
        self.yogur = yogur
    def calcular_caloria_yogur(self,cantidad,):
        #mirar subclass
        if isinstance(yogurDesnatado,YogurDesnatado):
            return self.yogur.calcular_calorias(cantidad)
        elif isinstance(postreProteico,PostresProteinas):
            return self.calcular_caloria_yogur()
        elif isinstance(yogur,Yogur):
            return self.calcular_caloria_yogur(cantidad)
print(f'El resultado es: {yogur.calcular_calorias(100)}')
print(f'Las calorías desnatadas son {yogurDesnatado.calcular_calorias(100)}')
print(f'El postre de proteínas tiene {postreProteico.calcular_calorias(100)}')
