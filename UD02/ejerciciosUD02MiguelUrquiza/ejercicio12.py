'''
Escriba un programa que permita crear una lista de palabras y que, a continuación, ordene la lista por
orden alfabético.
'''
print("Bienvenido este programa te permite crear una lista de palabras y la ordena en orden alfabético")

listaPalabras=[]
valor=""

while valor!="0":
    print("Pulse 0 para parar")
    valor=input("Introduzca la palabra que desee guardar: ")
    if valor!="0":
        listaPalabras.append(valor)

listaPalabras.sort()
print(listaPalabras)

print("Gracias por usar el programa.")