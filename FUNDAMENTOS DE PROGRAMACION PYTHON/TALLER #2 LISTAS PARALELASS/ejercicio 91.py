def ordenado (lista):
    anterior = 0
    for i in range (1, len(lista)):
        if (anterior > lista[i]):
            return (False)
        else:
            anterior = i
    return (True)        
    

lista = [1,2,3,4,5,6,3]
print (ordenado (lista))
    