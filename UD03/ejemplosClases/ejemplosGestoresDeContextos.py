#Un gestor de contexto permite realizar una serie de acciones a la entrada y la salida del bloque de código.
#Se utilizan dos métodos:
#   - __enter__ Acciones que se llevan a cabo al entrar en el bloque
#   - __exit__ Acciones que se llevan a caboal salir del bloque.
#Para utilizar el contexto debemos utilizar with loquesea.

from time import time

class Timer:
    def __enter__(self):
        self.start = time()
    def __exit__(self,exc_type,exc_value,exc_traceback):
        self.end = time()
        exec_time =  self.end - self.start
        print(f'El tiempo de ejecución fue: {exec_time}')

with Timer():
    for _ in range(2_000_000):
        x =2**20


class Droid:
    def __init__(self,name:str):
        self.name = name
        self.covered_distance = 0
    
    def move_up(self,steps:int)->None:
        self.covered_distance +=steps
        print(f'Moving {steps} steps')

#Preguntar porque esto no va si no uso init.
class FrozenDroid():
    def __init__(self,name:str):
        self.name = name

    def __enter__(self):
        self.droid = Droid(self.name)
        return self.droid
    def __exit__(self,*err):
        self.droid.covered_distance = 0


with FrozenDroid("R2D2") as droid:
    droid.move_up(10)
    droid.move_up(50)
    droid.move_up(-10)
    print(droid.covered_distance)
    