class Animales:
    def __init__(self):
        pass
    def calcular_coste_anual(self,cant_dinero_dia:float,dias_anyo:float):
        return cant_dinero_dia * dias_anyo
    

class Oso(Animales):
    def __init__(self):
        super().__init__()
    def calcular_coste_anual(self,cant_dinero_dia, dias_anyo,dias_semana:int,cant_veces_semana_comida_especial:int,coste_comida_especial:float):
        cant_semanas = dias_anyo/dias_semana
        
        cant_dias_comida_especial = cant_semanas *cant_veces_semana_comida_especial
        
        resultado = super().calcular_coste_anual(cant_dinero_dia,dias_anyo) + (cant_dias_comida_especial*coste_comida_especial)
        
        return round(resultado,2)
    
class Serpiente(Animales):
    def __init__(self):
        super().__init__()
    def calcular_coste_anual(self,cant_dinero_dia, dias_anyo,cant_insectos:int,coste_insecto:float,dias_semana:int,cant_veces_semana_comida_especial:int):
        
        
        cant_semanas = dias_anyo/dias_semana
        cant_dias_comida_especial = cant_semanas * cant_veces_semana_comida_especial
        
        precio_comida_especial = cant_insectos * coste_insecto
        
        resultado = cant_dias_comida_especial * precio_comida_especial
        
        return round(resultado,2)
    


class Zoo:
    def __init__(self,list_animales:list[Animales]):
        self.list_animales = list_animales
        
    def calcular_coste_serie_animales(self,cantidad_animales:int,cantidad_osos:int,cantidad_serpientes:int,animal:Animales,oso:Oso,serpiente:Serpiente,cant_dinero_dia:float,dias_anyo:int,dias_semana:int,cant_insectos:int,coste_insecto:float,cant_veces_comida_especial:int,coste_comida_especial:float):
        totalOso=   (oso.calcular_coste_anual(cant_dinero_dia,dias_anyo,dias_semana,cant_veces_comida_especial,coste_comida_especial))*cantidad_osos
        totalSerpiente = (serpiente.calcular_coste_anual(cant_dinero_dia,dias_anyo,cant_insectos,coste_insecto,dias_semana,cant_veces_comida_especial)) * cantidad_serpientes
        totalAnimales= animal.calcular_coste_anual(cant_dinero_dia,dias_anyo) * cantidad_animales
        
        return totalAnimales,totalOso, totalSerpiente

    def calcular_descuento_suministradora(self,limite:float,cant_descuento:float,cant_dinero_dia:float,dias_anyo:int,dias_semana:int,cant_insectos:int,coste_insecto:float,cant_veces_comida_especial:int,coste_comida_especial:float):
        base = 100.0
        total =0.0
        descuento =0.0
        for animal in self.list_animales:
            if isinstance(animal,Oso):
                total += animal.calcular_coste_anual(cant_dinero_dia,dias_anyo,dias_anyo,cant_veces_comida_especial,coste_comida_especial)
            elif isinstance(animal,Serpiente):
                total += animal.calcular_coste_anual(cant_dinero_dia,dias_anyo,cant_insectos,coste_insecto,dias_semana,cant_veces_comida_especial)
            elif isinstance(animal,Animales):
                total += animal.calcular_coste_anual(cant_dinero_dia,dias_anyo)
        
        if total > limite:
            descuento = round((total * cant_descuento)/base,2)
            

        total_descontado = total-descuento 
        
        
            
        return descuento,total,total_descontado
    
    def calcular_gastos_oso(self,cant_dinero_dia:float,dias_anyo:int,dias_semana:int,cant_veces_semana_comida_especial:int,coste_comida_especial:float):
        total = 0.0
        for animal in self.list_animales:
            if isinstance(animal,Oso):
                total += animal.calcular_coste_anual(cant_dinero_dia,dias_anyo,dias_semana,cant_veces_semana_comida_especial,coste_comida_especial)
                
        return total
        

serpiente = Serpiente()
oso = Oso()
oso2 = Oso()
animal = Animales()

lista = [serpiente,oso,oso2]

zoo = Zoo(lista)

lista = [zoo.calcular_coste_serie_animales(1,1,1,animal,oso,serpiente,10,365,7,10,1,2,10)]


for resultado in lista:
        print(f'{resultado}')
    
    
    
print(f'Descuento es: {zoo.calcular_descuento_suministradora(10,20,100,365,7,10,1,2,10)}')

print(f'Precio osos {zoo.calcular_gastos_oso(10,365,7,2,10)}')