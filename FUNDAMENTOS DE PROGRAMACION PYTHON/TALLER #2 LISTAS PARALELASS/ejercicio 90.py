def buscador (lista, numero):
    lista2  = []
    for i in range (len(lista)):
        if (lista[i] == numero):
            lista2.append (i)
    return (lista2)
lista = [2,54,34,2,45,76,2,45,6,2]
x = int(input("ingrese el valor a buscar: "))
print (buscador(lista, x))
        