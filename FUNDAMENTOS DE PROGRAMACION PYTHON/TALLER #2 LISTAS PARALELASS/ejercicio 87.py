def concatenar (lista1, lista2):
    lista3= []
    for i in range (len(lista1)):
        lista3.append (lista1[i])
    for j in range (len(lista2)):
        lista3.append (lista2[j])
    return (lista3)

def lista44 (lista3):
    lista4 = []
    for i in range (len(lista3)):
        if (numperf(lista3[i]) == lista3[i]):
            lista4.append (lista3[i])
    return (lista4)            
        
def numperf (numero):
     suma = 0
     i = 1
     while (i < numero):
          if (numero % i == 0):
               suma = suma + i
          i = i + 1
     return (suma)             
 

lista1 = [4,6,12,28,60,5]
lista2 = [2,45,496]
    
x = concatenar (lista1, lista2)
print (x)
    
y = lista44 (x)
print (y)
       