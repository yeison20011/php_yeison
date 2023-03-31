def buscaMenor (lista):
    men = 0
    for i in range (1, len(lista)):
        if (lista[i] < lista[men]):
            men = i
    return (lista [men])

def buscaMayor (lista):
    men = 0
    for i in range (1,len(lista)):
        if (lista[i] > lista [men]):
            men = i
    return (lista [men])

def total (lista):
    x = buscaMayor (lista)
    y = buscaMenor (lista)
    lista.remove(y)
    return (lista)
    
lista = [3.5, 2.3, 7.4, 1.2]
tot = total (lista)
print (tot)                       