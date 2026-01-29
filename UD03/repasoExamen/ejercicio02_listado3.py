

class Animal:
    
    def __init__(self,coste_diario:float):
        self.coste_diario=coste_diario
    
    
    def decorador_precio(func):
        def wrapper(*args,**kwargs):
            coste_total = func(*args,*kwargs)
            if coste_total <0:
                print(f'Es menor que 0')
                return coste_total
            print('Todo correcto')
            return coste_total
        return wrapper
    @decorador_precio
    def calcular_coste(self,dias_anyo=365,coste_comida_especial=100,coste_insectos=10)->float:
        return self.coste_diario * dias_anyo
            
    def __eq__(self, value:"Animal"):
        return self.calcular_coste() == value.calcular_coste()
        
            
    

class Oso(Animal):
    def __init__(self, coste_diario,cant_comidas:int):
        self.cant_comidas=cant_comidas
        super().__init__(coste_diario)
    def calcular_coste(self, dias_anyo,coste_comida_especial,coste_insectos):
        
        coste_extra = (round((dias_anyo/7))*self.cant_comidas)*coste_comida_especial
        return super().calcular_coste(dias_anyo,coste_comida_especial,coste_insectos) + coste_extra
    
class Serpiente(Animal):
    def __init__(self, coste_diario,cant_insectos:int):
        self.cant_insectos = cant_insectos
        super().__init__(coste_diario)
    def calcular_coste(self, dias_anyo, coste_comida_especial,coste_insectos):
        
        coste_insectos_dia = self.cant_insectos * coste_insectos
        
        dias_semanas = (dias_anyo/7)*2
        
        return coste_insectos_dia * dias_semanas
    
    
class Zoo:
    def __init__(self,lista_animales:list[Animal]):
        self.lista_animales=lista_animales
    def coste_serie_animales(self,dicccionario_animales:dict[Animal,int],dias_anyo:int,coste_comida_especial:float,coste_insectos:float)->float:
        total = 0.0
        for animal,cantidad in dicccionario_animales.items():
            total += animal.calcular_coste(dias_anyo,coste_comida_especial,coste_insectos)*cantidad
        return total
    def calcular_descuento(self,cantidad_minima:float,descuento:float,dias_anyo:int,coste_comida_especial:float,coste_insectos:float)->float:
        total = 0.0
        descuento_otorgado =0.0
        for animal in self.lista_animales:
            total += animal.calcular_coste(dias_anyo,coste_comida_especial,coste_insectos)
        
        if total > cantidad_minima:
            descuento_otorgado = (total*descuento)/100
        
        return descuento_otorgado
    def calcular_gasto_osos(self,dias_anyo:int,coste_comida_especial:float,coste_insectos:float)->float:
        total_osos = 0.0
        for animal in self.lista_animales:
            if isinstance(animal,Oso):
                total_osos += animal.calcular_coste(dias_anyo,coste_comida_especial,coste_insectos)
        
        return total_osos
    
class gestor_contexto:
    def __enter__(self):
        print('Empezando')
    def __exit__(self,*err):
        print('Saliendo..')
        

animal = Animal(100)
animal_2 = Animal(100)

animal2 = Oso(100,2)

lista_animales = [animal]

zoo =Zoo(lista_animales)



print(f'{zoo.calcular_descuento(2,30,365,20,10)}')
print(f'{zoo.calcular_gasto_osos(365,100,10)}')

print(f'{animal.calcular_coste(365,100,100)}')

with gestor_contexto() as gestor:
    print('Bueanas')
    
    

print(animal == animal_2)