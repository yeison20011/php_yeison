def ventas_maxima (uno):
    anterior = 0
    for i in range (len (uno)):
        if (uno [i] > anterior):
            anterior = uno [i]
    return (anterior)
    
def totales (ventas):
    suma = 0
    for i in range (len (ventas)):
        suma += ventas [i]
    return (suma, suma / 12)        
    
lista = [1000, 2000, 5000, 3000, 540000, 24343, 22343, 43545, 45454,5565, 23121, 2324]
x = ventas_maxima (lista)
z, d = totales (lista)
print ("mes en el que se vendio mas: ", x)
print ("la suma de todos los meses", z)
print ("el promedio de venta de todos los meses es: ", d)
            