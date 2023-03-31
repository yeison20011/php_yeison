def invertir (lista):
    lista = []
    for i in range (len (lista)-1, -1, -1):
        lista.append (lista[i])
    return (lista)
    
def impares (lista):
    listaimpar = []
    if (len(lista)%2 == 0):
        for i in range (len(lista) -2, -1, -2):
            listaimpar.append (lista[i])
        return (listaimpar)        
    else: 
        for k in range (len(lista)-1, -1, -2 ):
            listaimpar.append (lista[k])
        return (listaimpar)    
    
lista = [45,34,87,23,54,76,30]
x = invertir (lista)
print (x)
y = impares (lista)
print (y)



   
        