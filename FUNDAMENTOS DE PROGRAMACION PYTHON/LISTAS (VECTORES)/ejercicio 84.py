def intercalado (numero1, numero2):
    lista = []
    for i in range (len(numero1)):
        lista.append (numero1 [i])
        lista.append (numero2 [i])
        
    return (lista)    

lista1 = [1,3,5,7,9]
lista2 = [2,4,6,8,0]

print (intercalado (lista1, lista2))