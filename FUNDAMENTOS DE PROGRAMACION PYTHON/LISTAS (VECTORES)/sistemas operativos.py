def invertir_mayor_menor (lista):
    for i in range (len(lista)):
        for j in range (len(lista)-1, i, -1):
            if (lista[i] < lista[j]):
                x = lista[i]
                lista[i] = lista[j]
                lista[j] = x
    return (lista)

def invertir_menor_mayor (lista):
    for i in range (len(lista)):
        for j in range (len(lista)-1, i, -1):
            if (lista[i] > lista[j]):
                x = lista[j]
                lista[j] = lista[i]
                lista[i] = x
    return (lista)            

def eliminar_elemento (lista, num):
    for i in range (len(lista)):
        if (lista[i] == num):
            for j in range (i + 1, len(lista)):
                lista[i] = lista [j]
                i +=  1
    return (lista)     

def eliminar_elemento_v2 (lista, num):
    
    print (lista.remove(num)) 

      

if __name__ == "__main__":
    lista = [2,6,4,3,9,5]
    """x = invertir_mayor_menor (lista)
    print (x)
                
    y = invertir_menor_mayor (lista)
    print(y)
   """             
    z = eliminar_elemento_v2 (lista, 4)
    print (z)
                