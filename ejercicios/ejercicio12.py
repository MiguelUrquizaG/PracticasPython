import random

print("Bienvenido al programa")
print("En este programa tendrás que intentar adivinar el número. Tienes 3 intentos")

numAleatorio = random.randint(1,10) 
print(numAleatorio)
contador =0
acertado = False

while contador <3 and not acertado:
    print(f'Te quedan --> {3-contador} intentos')
    numerAdivinar = int(input("Introduce el valor que crees que es: "))
    
    if(numAleatorio is numerAdivinar):
        acertado =True
    contador += 1

if acertado:
    print(f'Enhorabuena has acertado el número era el: {numAleatorio}')
else:
    print(f'No has podido adivinarlo el número era el: {numAleatorio}')

