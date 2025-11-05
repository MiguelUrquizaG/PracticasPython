'''
Determine si una cadena de texto dada es un isograma, es decir, no se repite ninguna letra.
'''
palabra= input("Introduzca la palabra: ")
isIsograma=True
listado=list(palabra)

for i in listado:
    if listado.count(i)>1:
        isIsograma=False
        break

if isIsograma:
    print("Soy un isogramaaaa")
else:
    print("No soy un isogramaaaaaaa") 