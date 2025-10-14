text =[]
isTexto=True

print("Bienvenido al programa que permite escribir números hasta que se indique y después lo imprime")

while isTexto:
    textoInput = int(input("Introduzca una palabra: "))
    if textoInput != 0:
        text.append(textoInput)
    else:
        isTexto = False

print(text)

print("Gracias por usar el programa")