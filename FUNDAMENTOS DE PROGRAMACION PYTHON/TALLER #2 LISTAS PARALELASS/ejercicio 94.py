def descendente (lista1, lista2):
    anterior = 0
    anterior2 = 0
    for i in range (len(lista1)):
        for j in range (len(lista1)-1, i, -1):
            if (lista1[i] < lista1[j]):
                anterior = lista1[i]
                anterior2 = lista2[i]
                lista1[i] = lista1[j]
                lista2[i] = lista2[j]
                lista1[j] = anterior
                lista2[j] = anterior2
    return (lista1, lista2)    
              

lista1 = [16,13,77,45,87,35,40]
lista2 = [23,43,65,76,98,28,90]  

x,y = descendente (lista1, lista2)

print (x)
print (y)
            
    