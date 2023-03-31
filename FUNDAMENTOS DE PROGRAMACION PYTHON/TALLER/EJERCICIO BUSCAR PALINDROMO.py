def numeroCifras (numero):
    contador = 0
    while (numero > 0):
        numero = numero // 10
        contador += 1
    return (contador)

def reorden (numero):
    if (numeroCifras (numero) == 2):
        x = numero % 10
        x1 = numero // 10
        reordenado = (x * 10) + x1 
        return (reordenado)    
    else:
        if (numeroCifras (numero) == 3):
            x = numero % 10
            x1 = numero // 10
            y = x1 % 10
            y1 = x1 // 10
            reordenado = (x * 100) + (y * 10) + y1
            return (reordenado)
        else:
            if (numeroCifras (numero) == 4):
                x = numero % 10
                x1 = numero // 10
                y = x1 % 10
                y1 = x1 // 10
                z = y1 % 10
                z1 = y1 // 10
                reordenado = (x * 1000) + (y * 100) + (z * 10) + z1
                return (reordenado)
            else:
                if (numeroCifras (numero) == 5):
                    uno = numero % 10
                    uno1 = numero // 10
                    dos = uno1 % 10
                    dos1 = uno1 // 10
                    tres = dos1 % 10
                    tres1 = dos1 // 10
                    cuatro = tres1 % 10
                    cuatro1 = tres1 // 10
                    reordenado = (uno * 10000) + (dos * 1000) + (tres * 100) + (cuatro * 10) + cuatro1
                    return (reordenado)
                
def buscador (numero):
    aux = reorden (numero)
    if (numero == aux):
        return (numero)
    
def palindromo (numero):
    if (buscador (numero) == numero):
        return (True)
    else:
        return (False)
    
def buscaPalindromo ():
    contador = 0
    suma = ""
    for i in range (100, 500 + 1):
        if (contador <= 20):
            if (palindromo (i) == True):
                contador += 1    
                suma = suma + str (i)
                suma = suma + "-"
        else:
            return (suma)
            
                
if __name__ == "__main__":
    total = buscaPalindromo ()
    print ( "los primeros 20 numeros Palindromos de tres cifras en adelnate son: \n",total)                                    
                    