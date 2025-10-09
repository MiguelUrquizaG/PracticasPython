print("Bienvenido, este programa muestra el tipo de cada uno de los elementos de una lista")

list = [12,True,'wdasjda',(3-2.323),{"class":'V'}]

for i in range(len(list)):
    print(f'{list[i]} es {type(list[i])}')

print("Gracias por usar el programa.")