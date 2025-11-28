'''
Implementa una función modo_avion(texto, activar=True) que reciba una cadena y un booleano.
- Si activar es True, devuelve la cadena "[MODO AVIÓN] " seguida del texto.
- Si activar es False, devuelve solo el texto original.
'''

isModoAvion=True
mensaje = input('Introduzca su mensaje: ')


def modo_avion(texto, activar):
    if activar:
        return "[MODO AVIÓN] " +texto
    else:
        return texto

print(modo_avion(mensaje,isModoAvion))