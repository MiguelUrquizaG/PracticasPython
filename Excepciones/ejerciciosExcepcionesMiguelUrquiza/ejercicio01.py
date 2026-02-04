class coste_pedido_menor_cero(Exception):
    def __init__(self, message):
        super().__init__(message)
class lista_vacia(Exception):
    def __init__(self, message):
        super().__init__(message)
class coste_extra_mayor_diez(Exception):
    def __init__(self, message):
        super().__init__(message)

try:

    class Pedido:
        def __init__(self,coste_pedido:float):
            if coste_pedido<0:
                raise coste_pedido_menor_cero('EL coste del pedido no puede ser menor que 0')
            self.coste_pedido=coste_pedido
        def calcular_coste(self,coste_extra_urgente:float,coste_impuestos:float)->float:
            return self.coste_pedido
        
    class PedidoUrgente(Pedido):
        def __init__(self, coste_pedido):
            super().__init__(coste_pedido)
        def calcular_coste(self,coste_extra_urgente,coste_impuestos)-> float:
            if coste_extra_urgente >10:
                raise coste_extra_mayor_diez('EL coste extra no puede ser mayor que 10')
            return super().calcular_coste(coste_extra_urgente,coste_impuestos)

    class PedidoInternacional(Pedido):
        def __init__(self, coste_pedido):
            super().__init__(coste_pedido)
        def calcular_coste(self, coste_extra_urgente,coste_impuestos)->float:
            return super().calcular_coste(coste_extra_urgente,coste_impuestos)+coste_impuestos
        

    class EstadisticasPedido():
        def __init__(self,lista_pedidos:list[Pedido]):
            if len(lista_pedidos)<=0:
                raise lista_vacia('La lista implementada no puede estar vacía')
            self.lista_pedidos = lista_pedidos
        def calcular_media_pedidos(self,coste_extra_urgente:float,coste_impuestos:float):
            media=0.0
            for pedido in self.lista_pedidos:
                media +=pedido.calcular_coste(coste_extra_urgente,coste_impuestos)
            return media/len(self.lista_pedidos)
        
    
    pedido =Pedido(100)
    pedidoInternacional = PedidoInternacional(100)
    pedidoUrgente = PedidoUrgente(100)

    lista_pedidos = [pedido,pedidoInternacional,pedidoUrgente]

    estadisticas = EstadisticasPedido(lista_pedidos)

    print(f'La media del pedido es: {round(estadisticas.calcular_media_pedidos(10,20),2)}')
except coste_pedido_menor_cero as e:
    print(e)
except coste_extra_mayor_diez as e:
    print(e)
except lista_vacia as e:
    print(e)
except TypeError as e:
    print('El tipo de parámetro intoducido es incorrecto.')
