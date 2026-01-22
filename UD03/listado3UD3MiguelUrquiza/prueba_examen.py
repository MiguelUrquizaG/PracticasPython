class Vehiculo:
    def __init__(self,coste_mantenimiento_anual:float):
        self.coste_mantenimiento_actual = coste_mantenimiento_anual
    def calcular_coste_anual(self):
        return self.coste_mantenimiento_actual
    

class Vehiculo_Electrico(Vehiculo):
    def __init__(self, coste_mantenimiento_anual,coste_kWh:float,cantidad_kWh:float):
        self.coste_kWh = coste_kWh
        self.cantidad_kWh = cantidad_kWh
        super().__init__(coste_mantenimiento_anual)
    def calcular_coste_anual(self):
        coste_mantenimiento =super().calcular_coste_anual()
        return coste_mantenimiento + (self.coste_kWh * self.cantidad_kWh)

class Vehiculo_Hibrido(Vehiculo_Electrico,Vehiculo):
    def __init__(self, coste_mantenimiento_anual, coste_kWh, cantidad_kWh):
        super().__init__(coste_mantenimiento_anual, coste_kWh, cantidad_kWh)
    def calcular_coste_anual(self,precio_litro:float,cantidad_litro:float):
        coste_electrico = super().calcular_coste_anual()
        return coste_electrico + (precio_litro * cantidad_litro)


class Parque_Vehicular:
    def __init__(self,lista_vehiculos:list):
        self.lista_vehiculos = lista_vehiculos
    def calcular_coste_total_parque(self,precio_litro:float,cantidad_litro:float):
        total = 0.0
        for vehiculo in self.lista_vehiculos:
            if isinstance(vehiculo,Vehiculo_Hibrido):
                total+= vehiculo.calcular_coste_anual(precio_litro,cantidad_litro)
            elif isinstance(vehiculo,Vehiculo_Electrico):
                total += vehiculo.calcular_coste_anual()
            elif isinstance(vehiculo,Vehiculo):
                total += vehiculo.calcular_coste_anual()
        return total
    def calcular_coste_vehiculos_hibridos(self,precio_litro:float,cantidad_litros:float):
        total = 0.0
        for vehiculo in self.lista_vehiculos:
            if isinstance(vehiculo,Vehiculo_Hibrido):
                total += vehiculo.calcular_coste_anual(10,10)
        return total
    def aplicar_descuento(self,tope:float,descuento:float,precio_litro:float,cantidad_litros:float):
        total = 0.0
        base = 100.0
        for vehiculo in self.lista_vehiculos:
            if isinstance(vehiculo,Vehiculo_Hibrido):
                total+=vehiculo.calcular_coste_anual(precio_litro,cantidad_litros)
            elif isinstance(vehiculo,Vehiculo_Electrico):
                total+=vehiculo.calcular_coste_anual()
            elif isinstance(vehiculo,Vehiculo):
                total+=vehiculo.calcular_coste_anual()
        if total > tope:
            total = total - (total*descuento)/base
        return total

v1 = Vehiculo(100)
v2 = Vehiculo_Electrico(100,10,10)
v3 = Vehiculo_Hibrido(100,10,10)

lista = [v1,v2,v3]

parque = Parque_Vehicular(lista)

print(f'Total: {parque.calcular_coste_total_parque(10,10)}')
print(f'Total: {parque.calcular_coste_vehiculos_hibridos(10,10)}')
print(f'Total: {parque.aplicar_descuento(10,10,10,10)}')
