'''
Escriba un programa que pida dos números (m y n) y que escriba n segmentos de m estrellas
separados por m espacios, como muestran los ejemplos siguientes:
Escriba el tamaño del segmento: 4
Escriba el número de segmentos: 3
* * * *  * * * *  * * * * 
'''

m = int(input('Introduzca un número: '))
n = int(input('Introduzca otro número: '))

def segments (num1,num2):
    for _ in range(n):
            print('*\t'*m,end="\t")
            print(" "*m,end="\t")

segments(m,n)