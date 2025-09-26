'''
Mostrar el precio final (con IVA) de un producto con un valor de 100 euros, suponiendo que el IVA es el
21%.
'''
print("Bienvenido, a mi programa el cuál calculará")
precioProducto=float(input("Introduzca el precio de su producto: "));
iva=21.;
base=100;

precioIva= precioProducto +(precioProducto*iva/base);
print(precioIva,'€')

imprimible = f'El precio final con IVA es: {precioIva}€'

print(imprimible)