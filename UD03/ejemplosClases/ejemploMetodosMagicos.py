#Un método mágico como su nombre indica es aquel que parece que hace por arte de mágia,
#pero que en realidad está definido de alguna forma para que se ejecute así.

#En este primer ejemplo definimos mediante __eq__ que dos androides son iguales si coinciden en nombre.
#Independientemente del número de serie.
#Este import es obligatorio para poder usar el tipo Droid en el __eq__
from __future__ import annotations

'''
class Droid:
    def __init__(self,name:str,serial_number:int):
        self.name = name
        self.serial_number = serial_number
    def __eq__(self,droid:Droid)->bool:
        return self.name == droid.name

droid1 = Droid('C-3PO',2)
droid2 = Droid('R2-D2',11341312)


print(droid1.__eq__(droid2))
'''
#Los métodos mágicos no solo son operadores de comparación o matemáticos.

#En el siguiente ejemplo sumamos dos droides. Es decir el nombre de esta "fusión" es la suma de los dos.
#Y el poder de ambos se sumaría.

class Droid:
    def __init__(self,name:str,power:int):
        self.name = name
        self.power = power
    
    def __add__(self,other:Droid)->Droid:
        new_name = self.name + '-' + other.name
        new_power = self.power + other.power
        return Droid(new_name,new_power)

#Es obligatorio devolver un ojeto de la clase con la que se está trabajando.
#En verdad estos métodos están "sobrecargados" para que funcionen con la clase que las utilice de la forma que la utilice.
droid1 = Droid('C3PO',45)
droid2 = Droid('R2D2',91)

droid3 = droid1 + droid2

print(f'Fusion droid: \n{droid3.name} with power {droid3.power}')
