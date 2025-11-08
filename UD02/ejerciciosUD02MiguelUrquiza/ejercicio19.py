'''
19. Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4
sucursales. Informar:
• Las cantidades totales de cada articulo.
• La cantidad de artículos en la sucursal 2.
• La cantidad del articulo 3 en la sucursal 1.
• La recaudación total de cada sucursal.
• La recaudación total de la empresa.
• La sucursal de mayor recaudación.
'''
import random

nombresArtículos=['Patatas','Pan','Agua','Arroz','Pistachos']
nombreEmpresas=['Mercadona','Aldi','Día','Jamón']
preciosProductos=[]
cantProductos =5
cantEmpresas=4
ventasEmpresas=[]
cantTotalArticulos=[0]*cantProductos
cantProductosEmpresa2=0
cantProductos3Empresa1=0
recaudacionSucursales =[0]*cantEmpresas
recaudacionTotal=0

for i in range(0,cantProductos):
    preciosProductos.append(float(input(f'Introduce el precio del producto nº{i+1}: ')))

for i in range(0,cantEmpresas):
    ventasEmpresas.append([0]*cantProductos)
    for j in range(cantProductos):
        #ventasEmpresas[i][j]=int(input(f'Introduce la cantidad de {nombresArtículos[j]} que se han vendido en {nombreEmpresas[i]}: '))
        ventasEmpresas[i][j] = round(random.randint(0,100),2)



#Cantidades totales de cada articulo
for i in range(0,cantEmpresas):
    for j in range(cantProductos):
        cantTotalArticulos[j] += ventasEmpresas[i][j]

for producto,cantidad in zip(nombresArtículos,cantTotalArticulos):
    print(f'Se han vendido {cantidad} {producto}')


#La cantidad de artículos en la sucursal 2.
for i in range(0,cantEmpresas):
    for j in range(cantProductos):
        if i == 1:
            cantProductosEmpresa2+= ventasEmpresas[i][j]

print(f'La sucursal 2 ha vendido: {cantProductosEmpresa2} productos.')

#La cantidad del articulo 3 en la sucursal 1
print(ventasEmpresas[0][4])

#Recaudación de cada sucursal
for i in range(0,cantEmpresas):
    for j in range(cantProductos):
        recaudacionSucursales[i]+=ventasEmpresas[i][j] * preciosProductos[j]

print(recaudacionSucursales)

#La recaudación total de la empresa.
print(f'La recaudación total es: {sum(recaudacionSucursales)}')

#Sucursal mayor recaudación
print(f'La sucursal con mayor recaudación es: {nombreEmpresas[recaudacionSucursales.index(max(recaudacionSucursales))]} con {max(recaudacionSucursales)}€')