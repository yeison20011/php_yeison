from re import I


def numerador (x,k):
    g = 2 * k
    potencia = (x - 1)**g
    return (potencia)

def signo (k):
    return ((-1)**(k))

def factorial (n):
    acumulado = 1
    for i in range (1, n+1):  #el in significa que aumente de 1 en 1
                            #lo que esta dentro del parentesis quiere decir que empiece en 1 y termine hasta n
        acumulado = i * acumulado
    return (acumulado)
#el factorial tambien se hace con un while

def denominador (k):
    return (factorial(k-1))

def ejercicio_53_sumatoria (x,r):
    k = 1
    suma = 0
    while (k <= r):
        suma += ((signo(k)*(numerador(x,k))/denominador(k)))
        k+=1
    return (suma)

if __name__ == "__main__":
    x = float(input("digite un numero x: "))
    r = int(input("digite el numero de terminos a usar en la sumatoria r: "))
    respuesta = ejercicio_53_sumatoria(x,r)
    print("la sumatoria es: ",respuesta)            
            
            
