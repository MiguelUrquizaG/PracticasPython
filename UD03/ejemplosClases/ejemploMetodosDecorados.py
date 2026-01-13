#Un método decorador es aquel que recibe un método como parámetro.
# Y devuelve otro método.
#El siguiente ejemplo creamos un decorador para saber quien ha hecho que.

class Droid:
    @staticmethod
    def audit(method):
        def wrapper(self,*args,**kwargs):
            print(f'Droid {self.name} running {method.__name__}')
            return method(self,*args,**kwargs)
        return wrapper
    def __init__(self, name:str):
        self.name = name
        self.pos = [0,0]
    
    @audit
    def move(self,x:int,y:int):
        self.pos[0]+=x
        self.pos[1]+=1
    @audit
    def reset(self):
        self.pos = [0,0]
    
droid = Droid('R2-D2')

droid.move(1,1)
droid.reset()

#El audit lo que hace es que cada vez que se ejecuta un método recibe los parámetros necesarios de este
#Te imprime el nombre del método que se está ejecutando y lo ejecuta.
#El @audit sirve para que cuando se utilice uno de los métodos que lo tenga se ejecuten con sus parámetros.

