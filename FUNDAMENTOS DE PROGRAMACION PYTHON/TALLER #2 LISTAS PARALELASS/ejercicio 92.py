def reordenados (lista1 , lista2):
    lista3 = [] 
    if (len(lista1) >= len(lista2)):
        if (lista1 [0] <= lista2 [0]):
            for i in range (len(lista1)):
                lista3.append (lista1[i])
                if (i < len(lista2)):
                    lista3.append (lista2[i])
            return (lista3)
        else:
            for a in range (len(lista1)):
                if (a < len(lista2)):
                    lista3.append (lista2[a])
                    lista3.append (lista1[a]) 
                else:
                    lista3.append (lista1[a])  
            return (lista3)    
    else:
        if (lista2[0] <= lista1[0]):
            for j in range (len(lista2)):
                lista3.append (lista2[j])
                if (j < len(lista1)):
                    lista3.append (lista1[j])
            return (lista3)             
        else:
            for k in range (len(lista2)):
                if (k < len(lista1)):
                    lista3.append (lista1 [k])
                    lista3.append ((lista2[k]))
                else:
                    lista3.append ((lista2[k]))
            return (lista3)    
                
lista = [1,3,5,7,9,11, 13]
lista2 = [2,4,6,8,10,12]
print (reordenados (lista, lista2))
