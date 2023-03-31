'''lista = [1,2,3,4,5,6,7,8,9,10]
contador = 0
while (contador <= 9):
    lista [contador] += 100
    contador += 1
print (lista)

for i in range (len(lista)):  #len() es para recorrer la lista sin saber el tamano de la lista
    lista [i] += 30
print (lista)    
        
        
# crear lista vacia y pedir el tamano desde teclado
lista = []
x = int(input("ingrese el tamano de la lista: "))
for i in range (x):
    lista.append(int(input("ingrese el valor a ingresar en la lista: "))) #pide un valor diferente para cada posicion
    
    '''

'''lista2 = []
for i in range (len(lista) - 1, -1 , -1): #primer valor es desde donde empieza el rango
    lista2.append(lista[i])               #segundo valor es hasta donde llega el rango
print (lista2)                            #tercer valor es para que vaya de cuanto en cuanto, en este caso que vaya de para atras
                                          #el append es para agregar valores a la lista del ultimo agregado
   '''                 
                    
# CLASE 10 JUNIO

#ejercicio 78
'''''
def ejercicio78 (lista, valor):
    contador = 0
    for i in range (len(lista)):
        if (lista[i] == valor):
            contador += 1
    return (contador) 
x = int(input("ingrese el valor a buscar: "))
lista = [1,54,2,65,32, 2,43, 2, 76,2]
print("el numero de veces que aparece el" , x , "es:" , ejercicio78(lista,x))
'''
'''def ejercicio79 (lista, valor, Nreemplazo):
    for i in range (len(lista)):
        if (lista[i] == valor):
            lista[i] = Nreemplazo
    return (lista)         
x = int(input("ingrese el valor a buscar: "))
y = int(input("ingrese el valor a reemplazar: "))
lista = [1,54,2,65,32, 2,43, 2, 76,2]
print(ejercicio79(lista,x, y))
'''
'''
def ejercicio80_NumeroEspejo (numero):
    espejo = 0
    while (numero > 0):
        dig = numero % 10
        numero = numero // 10
        espejo = espejo * 10 + dig
    return (espejo)    

def ejercicio_80 (lista):
    lista2 = []
    for i in range (len(lista)):
        lista2.append(ejercicio80_NumeroEspejo(lista[i]))
    return (lista2)    


lista = [546,54657,24534,63543,33432, 234,45463, 762, 766,2889]
invertida = ejercicio_80(lista)
print (lista)
print (invertida)
'''
def esta_en_la_lista (lista, valor):
    for i in range (len(lista)):
        if (lista[i] == valor):
            return (True)
    return (False) 
    
def construir_conjunto (valor):
    listanueva = [] 
    for i in range (len(valor)):
        if (esta_en_la_lista(listanueva, valor [i]) == False):
            listanueva.append(valor[i])
    return (listanueva)              

def union_conjuntos (x, y):
    nueva = []
    for i in range (len(x)):
        nueva.append(x[i])
    for i in range (len(y)):
        nueva.append(y[i])
    nueva = construir_conjunto(nueva)
    return (nueva)
def interseccion (x,y):
    nueva = []
    for i in range (len(x)):
        if (esta_en_la_lista(y , x[i])):
            nueva.append(x[i])
    return (nueva)        
           
            
    
lista = [34,546,34,354,546,23,12,5465,67,12]
lista2 = [4, 34, 23, 878, 3535, 12]
conjunto = construir_conjunto (lista)
conjunto2 = construir_conjunto (lista2) 
x = union_conjuntos(conjunto, conjunto2)
y = interseccion (conjunto, conjunto2)
print (conjunto)
print (conjunto2)
print (x)   
print (y)        