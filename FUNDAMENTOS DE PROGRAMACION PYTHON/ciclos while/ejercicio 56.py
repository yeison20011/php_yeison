def factorial (m):
    acumulado = 1
    for i in range (1,m+1):
        acumulado = acumulado * i
    return (acumulado)        
def combinatoria (m,n):
    if (m >= n):
        total = (factorial (m)) / ((factorial (n) * (factorial (m-n))))
        return (total)
    else: 
        return (0)
    
if __name__ == "__main__":
    m = int(input("ingrese un valor positivo para M: "))
    n = int(input("ingrese un valor positivo para N: "))
        
    while (m < 0 or n < 0):
        m = int(input("ingrese un valor positivo para M: "))
        n = int(input("ingrese un valor positivo para N: "))
    todo = combinatoria (m,n)
    print("el total es: ",todo)
        
        
                 
            
    
    