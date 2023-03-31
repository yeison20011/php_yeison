#YEISON ANDRES LOPEZ LOZANO
#1002362234

# EJERCICIO DE NUMERO KAPREKAR

def descomponer (numero):
    x = numero % 10
    y = numero // 10
    z = y % 10
    c = y // 10
    j = c % 10
    v = c // 10
    return (x,z,j,v)

def descomposicionMayor (numero):
    suma = 0
    
    x,z,j,v = descomponer (numero)
        
    if (x >= z and x >= j and x >= v): 
        suma = suma + (x * 1000)
        if (z >= j and z >= v):
            suma = suma + (z * 100)
            if (j >= v):
                suma = suma + (j * 10) + v
                return (suma)
            else:
                suma = suma + (v * 10) + j
                return (suma)
        else:
            if (j >= z and j >= v):
                suma = suma + (j * 100)
                if (z >= v):
                    suma = suma + (z * 10) + v
                    return (suma)
                else:
                    suma = suma + (v * 10) + z
                    return (suma)          
            else:
                if (v >= z and v >= j):
                    suma = suma + (v * 100)
                    if (z >= j):
                        suma = suma + (z * 10) + j
                        return (suma)
                    else:
                        suma = suma + (j * 10) + z                        
                        return (suma)
    else:               
        if (z >= x and z >= j and z >= v):
            suma = suma + (z * 1000)
            if (x >= j and x >= v):
                suma = suma + (x * 100)
                if (j >= v):
                    suma = suma + (j * 10) + v
                    return (suma)
                else:
                    suma = suma + (v * 10) + j
                    return (suma)
            else:
                if (j >= x and j >= v):
                    suma = suma + (j * 100)
                    if (x >= v):
                        suma = suma + (x * 10) + v
                        return (suma)
                    else:
                        suma = suma + (v * 10) + x
                        return (suma)                
                else:
                    if (v >= x and v >= j):
                        suma = suma + (v * 100)
                        if (x >= j):
                            suma = suma + (x * 10) + j
                            return (suma)
                        else:
                            suma = suma + (j * 10) + x
                            return (suma)  
        else:
            if (j >= x and j >= z and j >= v):
                suma = suma + (j * 1000)
                if (x >= z and x >= v):
                    suma = suma + (x * 100)
                    if (z >= v):
                        suma = suma + (z * 10) + v
                        return (suma)
                    else:
                        suma = suma + (v * 10) + z
                        return (suma)
                else:
                    if (z >= x and z >= v):
                        suma = suma + (z * 100)
                        if (x >= v):
                            suma = suma + (x * 10) + v
                            return (suma)
                        else:
                            suma = suma + (v * 10) + x
                            return (suma)                
                    else:
                        if (v >= x and v >= z):
                            suma = suma + (v * 100)
                            if (x >= z):
                                suma = suma + (x * 10) + z
                                return (suma)
                            else:
                                suma = suma + (z * 10) + x
                                return (suma)  
            else:
                if (v >= x and v >= j and v >= z):
                    suma = suma + (v * 1000)
                    if (x >= j and x >= z):
                        suma = suma + (x * 100)
                        if (j >= z):
                            suma = suma + (j * 10) + z
                            return (suma)
                        else:
                            suma = suma + (z * 10) + j
                            return (suma)
                    else:
                        if (j >= x and j >= z):
                            suma = suma + (j * 100)
                            if (x >= z):
                                suma = suma + (x * 10) + z
                                return (suma)
                            else:
                                suma = suma + (z * 10) + x
                                return (suma)                
                        else:
                            if (z >= x and z >= j):
                                suma = suma + (z * 100)
                                if (x >= j):
                                    suma = suma + (x * 10) + j
                                    return (suma)
                                else:
                                    suma = suma + (j * 10) + x 
                                    return (suma)                  
                                
def descomposicionMenor (numero):
    suma = 0
    
    x,z,j,v = descomponer (numero)
        
    if (x <= z and x <= j and x <= v): 
        suma = suma + (x * 1000)
        if (z <= j and z <= v):
            suma = suma + (z * 100)
            if (j <= v):
                suma = suma + (j * 10) + v
                return (suma)
            else:
                suma = suma + (v * 10) + j
                return (suma)
        else:
            if (j <= z and j <= v):
                suma = suma + (j * 100)
                if (z <= v):
                    suma = suma + (z * 10) + v
                    return (suma)
                else:
                    suma = suma + (v * 10) + z
                    return (suma)          
            else:
                if (v <= z and v <= j):
                    suma = suma + (v * 100)
                    if (z <= j):
                        suma = suma + (z * 10) + j
                        return (suma)
                    else:
                        suma = suma + (j * 10) + z                        
                        return (suma)
    else:               
        if (z <= x and z <= j and z <= v):
            suma = suma + (z * 1000)
            if (x <= j and x <= v):
                suma = suma + (x * 100)
                if (j <= v):
                    suma = suma + (j * 10) + v
                    return (suma)
                else:
                    suma = suma + (v * 10) + j
                    return (suma)
            else:
                if (j <= x and j <= v):
                    suma = suma + (j * 100)
                    if (x <= v):
                        suma = suma + (x * 10) + v
                        return (suma)
                    else:
                        suma = suma + (v * 10) + x
                        return (suma)                
                else:
                    if (v <= x and v <= j):
                        suma = suma + (v * 100)
                        if (x <= j):
                            suma = suma + (x * 10) + j
                            return (suma)
                        else:
                            suma = suma + (j * 10) + x
                            return (suma)  
        else:
            if (j <= x and j <= z and j <= v):
                suma = suma + (j * 1000)
                if (x <= z and x <= v):
                    suma = suma + (x * 100)
                    if (z <= v):
                        suma = suma + (z * 10) + v
                        return (suma)
                    else:
                        suma = suma + (v * 10) + z
                        return (suma)
                else:
                    if (z <= x and z <= v):
                        suma = suma + (z * 100)
                        if (x <= v):
                            suma = suma + (x * 10) + v
                            return (suma)
                        else:
                            suma = suma + (v * 10) + x
                            return (suma)                
                    else:
                        if (v <= x and v <= z):
                            suma = suma + (v * 100)
                            if (x <= z):
                                suma = suma + (x * 10) + z
                                return (suma)
                            else:
                                suma = suma + (z * 10) + x
                                return (suma)  
            else:
                if (v <= x and v <= j and v <= z):
                    suma = suma + (v * 1000)
                    if (x <= j and x <= z):
                        suma = suma + (x * 100)
                        if (j <= z):
                            suma = suma + (j * 10) + z
                            return (suma)
                        else:
                            suma = suma + (z * 10) + j
                            return (suma)
                    else:
                        if (j <= x and j <= z):
                            suma = suma + (j * 100)
                            if (x <= z):
                                suma = suma + (x * 10) + z
                                return (suma)
                            else:
                                suma = suma + (z * 10) + x
                                return (suma)                
                        else:
                            if (z <= x and z <= j):
                                suma = suma + (z * 100)
                                if (x <= j):
                                    suma = suma + (x * 10) + j
                                    return (suma)
                                else:
                                    suma = suma + (j * 10) + x 
                                    return (suma)                                               
                                
def restaNumeros (numero):
    resta = numero
    contador = 0
    while (resta != 6174): 
        contador = contador + 1
        resta = descomposicionMayor (resta) - descomposicionMenor (resta)
        if (resta == 6174):
            return (contador)
        else:
            x = numeroCifras (resta)
            if (x == 4):
                resta = resta
            else:
                if (x == 3):
                    resta = resta * 10
                else:
                    if (x == 2):
                        resta = resta * 100
                    else:
                        if (x == 1):
                            resta = resta * 1000    
def numeroCifras (numero):
    
    contador = 0
    while (numero != 0):
        numero = numero // 10
        contador += 1
    return (contador)    
        
        
if __name__ == "__main__":
    x = int(input("ingrese el numero a inspeccionar: "))
    y = restaNumeros (x)
    print("Se tuvo que realizar ", y , " veces la operacion de Kaprekar para obtener el resultado 6174.")        
                
                                        
                                      