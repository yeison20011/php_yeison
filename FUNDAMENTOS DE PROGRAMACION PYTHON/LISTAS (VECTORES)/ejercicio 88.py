def nuevo (lista):
    nueva = []
    for i in range (len (lista)):
        nueva.append (0)
        for j in range (i + 1):
            if (i % 2 == 0):
                nueva [i] += lista [j]
            else:    
                nueva [i] += (lista [j] * ((-1)**j))
    return (nueva)        

lista = [1,3,5,7,9]
print (nuevo (lista))
            
        
        
        