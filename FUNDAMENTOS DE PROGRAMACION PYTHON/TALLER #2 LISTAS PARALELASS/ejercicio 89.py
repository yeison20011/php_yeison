def promedio (lista):
    lista2 = []
    suma = 0
    for i in range (len(lista)):
        suma = suma + lista [i]
    suma = suma / len(lista)
    
    for j in range (len(lista)):
        if (lista[j] > suma):
            lista2.append (lista[j])
    return (lista2)

lista = [2,5,687,34,56,5,4,65,231,877]
print (promedio(lista))
        

    