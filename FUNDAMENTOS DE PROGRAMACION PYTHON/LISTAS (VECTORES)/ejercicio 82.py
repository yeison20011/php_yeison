def ejercicio_82_primos (lista):
    nueva = []
    for i in range (len(lista)):
        if (primos(lista[i]) == True):
            nueva.append(lista[i])
    return (nueva)

def ejercicio_82_perfectos (lista):
    nueva1 = []
    for i in range (len(lista)):
        if (perfectos(lista[i] == True)):
            nueva1.append(lista[i])
    return (nueva1)

def primos (numero):
    for i in range (2,numero):
        if (numero % i == 0):
            return (False)
    return (True)

def perfectos (numero):
    suma = 0
    for i in range (1, numero):
        if (numero % i == 0):
            suma += 1
    if (suma == numero):
        return (True) 
    else:
        return (False)           
                        
    
lista = [6,7,28,4,88,13]
x = ejercicio_82_perfectos (lista)
y = ejercicio_82_primos (lista)
print (x)
print (y)    