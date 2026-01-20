class Droid:
    def __init__(self,enemigos_matados:float,distancia_recorrida:float):
        self.enemigos_matados = enemigos_matados
        self.distancia_recorrida = distancia_recorrida
        pass
    def sumar_enemigos_matados(self,cantidad:float):
        self.enemigos_matados+=cantidad
        return self.enemigos_matados
    
    def calcular_distancia_recorrida(self,distancia:float):
        self.distancia_recorrida+=distancia
        return self.distancia_recorrida

class ProtocolDroid(Droid):
    def __init__(self, enemigos_matados, distancia_recorrida):
        super().__init__(enemigos_matados, distancia_recorrida)
    def sumar_enemigos_matados(self, cantidad,multiplicador:float):
        super().sumar_enemigos_matados(cantidad) * multiplicador
        self.enemigos_matados *= multiplicador
        return self.enemigos_matados
    def calcular_distancia_recorrida(self, distancia,retroceso:float):
        super().calcular_distancia_recorrida(distancia)
        self.distancia_recorrida -= retroceso
        return self.distancia_recorrida 
    
class AstromechDroid(Droid):
    def __init__(self, enemigos_matados, distancia_recorrida):
        super().__init__(enemigos_matados, distancia_recorrida)
    def sumar_enemigos_matados(self, cantidad):
        self.enemigos_matados = 0
        return self.enemigos_matados
    def calcular_distancia_recorrida(self, distancia):
        return super().calcular_distancia_recorrida(distancia)