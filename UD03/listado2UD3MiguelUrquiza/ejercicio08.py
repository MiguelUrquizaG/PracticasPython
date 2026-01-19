import math

class Figura:
    def calcular_area(self):
        pass
    def calcular_perimetro(self):
        pass
    def calcular_factor_escala(self):
        pass


class Rectangulo(Figura):
    def __init__(self,largo:float,ancho:float):
        self.largo = largo
        self.ancho = ancho
        super().__init__()
    def calcular_area(self):
        return round(self.largo * self.ancho,2) 
    def calcular_perimetro(self):
        return 2*(self.largo+self.ancho)
    def calcular_factor_escala(self,largo:float):
        return largo/self.largo
    def __str__(self):
        return f'Soy un Rectangulo'
    
class Circulo (Figura):
    def __init__(self,radio:float):
        self.radio = radio
        super().__init__()
    def calcular_area(self):
        return round(math.pi * math.pow(self.radio,2),2)
    def calcular_perimetro(self):
        return 2*math.pi*self.radio
    def calcular_factor_escala(self,radio:float):
        return radio/self.radio
    def __str__(self):
        return f'Soy un Circulo'

class Triangulo(Figura):
    def __init__(self,base:float,lado2:float,lado3:float,altura:float):
        self.base = base
        self.lado2 = lado2
        self.lado3 = lado3
        self.altura = altura
        super().__init__()
    
    def calcular_area(self):
        return round((self.base * self.altura)/2,2)
    def calcular_perimetro(self):
        return self.base + self.lado2 + self.lado3
    def calcular_factor_escala(self,lado:float):
        return lado/self.base
    def __str__(self):
        return f'Soy un triangulo'
    
    

circulo = Circulo(10.0)
rectangulo = Rectangulo(100.0,100.0)
triangulo = Triangulo(10.0,3.0,5.0,8.0)

circulo2 = Circulo(5.0)
rectangulo2 = Rectangulo(5.0,5.0)
triangulo2 = Triangulo(5.0,6.0,2.0,4.0)

lista={circulo,rectangulo,triangulo,circulo2,rectangulo2,triangulo2}
sumaAreasCirculo=0.0
sumaAreasRectangulo=0.0
sumaAreasTriangulo=0.0
for figura in lista:
    if isinstance(figura,Circulo):
        sumaAreasCirculo+= figura.calcular_area()
    elif isinstance(figura,Rectangulo):
        sumaAreasRectangulo += figura.calcular_area()
    elif isinstance (figura,Triangulo):
        sumaAreasTriangulo+=figura.calcular_area()


print(f'Circulo: {round(sumaAreasCirculo,2)} | Rectángulo: {sumaAreasRectangulo} | Triángulo: {sumaAreasTriangulo}')

sumaPerimetroCirculo=0.0
sumaPerimetroRectangulo=0.0
sumaPerimetroTriangulo=0.0
for figura in lista:
    if isinstance(figura,Circulo):
        sumaPerimetroCirculo+= figura.calcular_perimetro()
    elif isinstance(figura,Rectangulo):
        sumaPerimetroRectangulo += figura.calcular_perimetro()
    elif isinstance (figura,Triangulo):
        sumaPerimetroTriangulo+=figura.calcular_perimetro()


print(f'Circulo: {round(sumaPerimetroCirculo,2)} | Rectángulo: {sumaPerimetroRectangulo} | Triángulo: {sumaPerimetroTriangulo}')

mayorArea = 0.0
for figura in lista:
    figuraMayorArea=None
    if figura.calcular_area()>mayorArea:
        mayorArea = figura.calcular_area()
        figuraMayorArea = figura




print(f'La figura con mayor área es: {figuraMayorArea}, valor {mayorArea}')