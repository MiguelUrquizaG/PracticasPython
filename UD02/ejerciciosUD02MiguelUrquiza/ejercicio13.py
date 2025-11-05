'''
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen
posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
'''
import string

print("Bienvenido este programa genera una lista con el abecedario y elimina las letras en posiciones múltiplos de 3.")

abecedario=list(string.ascii_uppercase)
abecedario2 =list(string.ascii_uppercase)
abecedario.insert(abecedario.index('N')+1,'Ñ')
abecedario2.insert(abecedario2.index('N')+1,'Ñ')
print(abecedario)

#Forma humana
for i, letra in enumerate(abecedario):
    if (i+1)%3 ==0:
        del abecedario[i]

print(abecedario)

#Forma del lado oscuro
for i, letra in enumerate(abecedario2):
    if i%3 ==0:
        del abecedario2[i]

print(abecedario2)

print("Gracias por usar.")