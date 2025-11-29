'''
Implementa generar_password(base="1234", repeticiones=3) que devuelva una contraseña formada
por la cadena base repetida el número de veces indicado y seguida de "!" al final.
Ejemplo: generar_password("abc", 2) → "abcabc!".
'''

base = input('Introduzca la base de su contraseña: ')
repeticiones = int(input('Introduzca el número de veces que quieres que se repita: '))

def generar_password(base_contrenia,rep):
    password_formada = base_contrenia*rep + "!"
    return password_formada


print(generar_password(base,repeticiones))