def ejercicio_46 (minutos,segundos):
    if (segundos > 30 and segundos < 60):
        minutos = minutos + 1
    else :
        if (segundos <= 30):
            minutos = minutos
    if (minutos > 0 and minutos <=5):
        tpagar = minutos * 300
    else:
        if (minutos > 5 and minutos <=10):
            total = minutos * 200
        else:
            if (minutos > 10):
                total = 1500 + (100 *(minutos - 10))
    if (total >= 1600):
        total = total * 0.9
    return (total)                        
    
if __name__ == "__main__":
    
    x = int(input("ingrese la cantidad de minutos consumidos: "))
    y = int(input("ingrese la cantidad de segundos gastados: "))
    respuesta = ejercicio_46 (x,y)
    print("el total a pagar es: ",respuesta)                
                
        