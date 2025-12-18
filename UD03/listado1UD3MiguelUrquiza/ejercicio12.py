'''
Escribe una función contador_likes(*likes_por_dia) que reciba un número variable de enteros (likes
de cada día) y devuelva: (Si no lo sabes, busca qué significa el asterisco como parte del parámetro de
una función en Python)
- El total de likes.
- La media de likes.
- El día con más likes (posición empezando en 1).

1,2,3,3
'''

def contador_like(*likes_por_dia):
    total = sum(likes_por_dia)
    media = total/len(likes_por_dia)
    cantMaxLikes = max(likes_por_dia)

    vecesCantMax = likes_por_dia.count(cantMaxLikes)

    diasLike=[]

    if vecesCantMax>1:
        for num in likes_por_dia:
            if num == cantMaxLikes:
                if diasLike:
                    diasLike.append(likes_por_dia.index(num))


    return total,media,diasLike



print(contador_like(1,2,3,3))