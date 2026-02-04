class Pedido:
    def __init__(self,coste_pedido:float):
        self.coste_pedido=coste_pedido
    def calcular_coste(self,coste_extra_urgente:float,coste_impuestos:float)->float:
        return self.coste_pedido
    
class PedidoUrgente(Pedido):
    def __init__(self, coste_pedido):
        super().__init__(coste_pedido)
    def calcular_coste(self,coste_extra_urgente,coste_impuestos)-> float:
        return super().calcular_coste(coste_extra_urgente,coste_impuestos)

class PedidoInternacional(Pedido):
    def __init__(self, coste_pedido):
        super().__init__(coste_pedido)
    def calcular_coste(self, coste_extra_urgente,coste_impuestos)->float:
        return super().calcular_coste(coste_extra_urgente,coste_impuestos)+coste_impuestos
    

class EstadisticasPedido():
    def __init__(self,lista_pedidos:list[Pedido]):
        self.lista_pedidos = lista_pedidos
    def calcular_media_pedidos(self,coste_extra_urgente:float,coste_impuestos:float):
        media=0.0
        for pedido in self.lista_pedidos:
            media +=pedido.calcular_coste(coste_extra_urgente,coste_impuestos)
        return media/len(self.lista_pedidos)
    

pedido =Pedido(100)
pedidoInternacional = PedidoInternacional(100)
PedidoUrgente = PedidoUrgente(100)

lista_pedidos = [pedido,pedidoInternacional,PedidoUrgente]

estadisticas = EstadisticasPedido(lista_pedidos)

print(f'La media del pedido es: {round(estadisticas.calcular_media_pedidos(10,20),2)}')