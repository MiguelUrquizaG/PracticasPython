
lista = [1,2,5,6,7,8]

def pares(listado:list):
    paresList = []
    for num in lista:
        if num%2==0:
            paresList.append(num)
    return sum(paresList)


print(pares(lista))