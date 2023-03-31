def descomponer (numero):
    contador = 0
    while (numero > 0):
        numero = numero // 10
        contador = contador + 1
    return (contador)

def potencia (k,h):
    pot = h**k
    return (pot)

def sumapotencias (numero):
    x = descomponer (numero)
    y = 0
    z = 0
    suma = 0
    while (z < x):
        y = numero % 10
        suma = suma + potencia (x , y)
        numero = numero // 10
        z = z + 1
    return (suma)

def ejercicio58 (numero):
    respuesta = 0
    if (sumapotencias (numero) == numero):
        respuesta = int (numero)
    else:
        respuesta = int (0)
    return (respuesta)

def parejanumeros (num1, num2):
    primer = 0
    if (num1 <= num2):
        c = num1
        primer = ejercicio58 (c)
        return (primer)
    else:
        return (primer)    


def restar (primer, ultimo):
    anterior = 0
    primeranterior =[]
    while (primer <= ultimo):
        primer += 1
        aux = parejanumeros (primer, ultimo)
        
        
        if ( aux >= anterior):
            if (aux > 0):
                primeranterior = primeranterior + [aux]

                respuesta = primeranterior

        else:
            respuesta = primeranterior
    return (respuesta)    

def rta(primeranterior):
    x1=[]
    x1=primeranterior[1]-primeranterior[0]
    x2=primeranterior[2]-primeranterior[0]
    x3=primeranterior[2]-primeranterior[1]
    if(x1<x2 and x1<x3):
        return([primeranterior[0]]+[primeranterior[1]])
    if(x2<x1 and x2<x3):
        return([primeranterior[0]]+[primeranterior[2]])
    if(x3<x2 and x3<x1):
        return([primeranterior[1]]+[primeranterior[2]])
                
 
def restar2 (primer, ultimo):
    anterior = 0
    while (primer <= ultimo):
        aux = parejanumeros (primer, ultimo)
        if (aux >= anterior):
            primer +=1 
            if (aux > 0):
                return (aux)
        else:
            primer += 1
            respuesta = anterior    
    return (respuesta)

def restadefinitiva (primer, ultimo):
    for i in range (primer, ultimo + 1):
        x = restar2 (i, ultimo)
        z = i
        if (x > primer):
            respuesta = x 
            if (x > i):
                respuesta1 = x
            else:
                if (x < ultimo):
                    respuesta2 = x 
                resta = respuesta - respuesta1
                resta1 = respuesta - respuesta2
                resta2 = respuesta1 - respuesta2
        if (resta > resta1 and resta > resta2):
            total = resta
        else:
            if (resta1 > resta and resta1 > resta2):
                total = resta1 
            else:
                total = resta2 
    return (total)                         
            
                           
                
                    

if __name__ == "__main__":
    primer = int(input("ingrese desde donde empieza el rango: "))
    ultimo = int(input("ingrese hasta donde termina el rango: "))
    total = restar (primer,ultimo)
    print (rta(total))            