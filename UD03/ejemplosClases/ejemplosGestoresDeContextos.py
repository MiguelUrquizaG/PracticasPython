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
    for _ in range(1_000_000_000):
        x =2**20
