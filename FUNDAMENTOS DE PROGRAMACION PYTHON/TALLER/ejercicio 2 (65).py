def ndigitos (numero):
    contador = 0 
    while (numero > 0):
        numero = numero // 10
        contador += 1
    return (contador)

def cuadradonumero (numero):
    potencia = numero ** 2 
    return (potencia)

def acumuladoNumero (numero):
    x = 0
    sumapotencia = 0
    while (numero > 0):
        x = numero % 10
        sumapotencia += cuadradonumero (x)
        numero = numero // 10
    return (sumapotencia) 

def sumanumerofeliz (numero):
    contador = 2
    x = 0
    x = acumuladoNumero (numero)
    