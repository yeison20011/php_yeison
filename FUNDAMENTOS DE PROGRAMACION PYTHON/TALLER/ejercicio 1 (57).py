def divisores (numero):
    contador = 1
    suma = 0
    while (numero > contador):
        if (numero % contador != 0):
            contador = contador + 1
        else:
            suma = suma + contador
            contador = contador + 1    
    return (suma)

def ejercicio57 (numero1, numero2):
    numeroaux = numero2
    while (numero1 < numero2):
        
        for i in range  (numero1, numeroaux + 1):
        
                if ((divisores (i) == numeroaux and (divisores (numeroaux) == i)) == True):
                    print ("los numeros parejas desde el rango ", numero1 , " hasta", numero2, " son: " + i,numeroaux)
                    
    numero2 -= 1            
                    
        
        
if __name__ == "__main__":
    x = int(input("ingrese el primer digito de donde empieza el rango: "))
    y = int(input("ingrese el segundo digito hasta donde termina el rango: "))
    contador = ejercicio57 (x, y)
    

        