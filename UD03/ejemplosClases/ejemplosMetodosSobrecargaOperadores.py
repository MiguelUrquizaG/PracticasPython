#En el caso hipotetico en el que a un droide en vez de sumarle otro le sumemos un número directamente podemos hacer que se sume su energía
from __future__ import annotations

# class Droid:
#     def __init__(self,name:str,power:int):
#         self.name = name
#         self.power = power
#     def __add__(self,other:Droid|int)->Droid:
#         if isinstance(other , Droid):
#             new_name = self.name + ' '+other.name
#             new_power = self.power + other.power
#         elif isinstance(other,int):
#             new_name = self.name
#             new_power = self.power + other
#         return Droid(new_name,new_power)
    

# droid1 = Droid('R2D2',100)
# droid2 = Droid('C3PO',200)

# droid1 = droid1 + 100

# print(droid1.power)

#En el caso de igualar (==) que no asignar (=) como interactuaria con una cadena pues debemos definirmo también

# class Droid:
#     def __init__(self,name:str,power:int):
#         self.name = name
#         self.power = power
#     def __eq__(self, other:Droid|object)->bool:
#         if isinstance(other,Droid):
#             return self.name == other.name
#         return False
    

# droid1 = Droid('R2D2',100)

# print(droid1 == droid1)

#Uno de los métood mágicos más utilizados es str, ya que define como se va a imprimir un objeto. Es decir actúa como un toString.

# class Droid:
#     def __init__(self,name:str,serial_number:str):
#         self.name = name
#         self.serial_number=serial_number
#     def __str__(self)->str:
#         return f'This robot named: {self.name} has the serial number: {self.serial_number}'
    

# droid1 = Droid('R2D2','A213123BZ')

# print(droid1)

#En ausencia del __str__ se utilizará por defecto el __repr__ , la diferencia es que el primero es más para mostrarlo al usuario y el segundo al desarrollador.
#El método __repr__ se activa automáticamente en 2 ocasiones:
#   -Cuando no existe el __str__ e intentamos encontrar la representación del objeto en cadena mediante str() o print()
#   -Cuando en el interprete interactivo de Python (la consola) pedimos el valor del objeto, es decir ponemos el nombre de la variable directamente.

class Droid:
    def __init__(self,name:str):
        self.name = name
    def __repr__(self) -> str:
        return f"[Droid] '{self.name}' @ {hex(id(self))}"




droid1 = Droid('R2D2')
print(droid1)    