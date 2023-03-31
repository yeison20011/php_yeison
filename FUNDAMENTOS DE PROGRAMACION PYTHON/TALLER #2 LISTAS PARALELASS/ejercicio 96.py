def indice_masa_corporal (peso, estatura):
    lista = []
    for i in range (len(peso)):
        masa = peso[i] / (estatura[i]**2)
        lista.append (masa)
    return (lista)

def sobrepeso (masa, edad, estatura, documento):
    
    edad1 = []
    edad2 = []
    edad3 = []
    estatura1 = []
    estatura2 = []
    estatura3 = []
    documento1 = []
    documento2 = []
    documento3 = []
    desnutrido = []
    normal = []
    gordo = []
  
    for i in range (len(masa)):
        if (masa[i] < 21):
            desnutrido.append (masa[i])
            edad1.append (edad[i])
            estatura1.append (estatura [i])
            documento1.append (documento [i])
        else:
            if (masa[i] >= 21 and masa[i] <= 25):
                normal.append (masa[i])
                edad2.append (edad[i])
                estatura2.append (estatura [i])
                documento2.append (documento [i])
            else:
                if (masa[i] > 25):
                    gordo.append (masa[i])
                    edad3.append (edad[i])
                    estatura3.append (estatura [i])
                    documento3.append (documento [i])
    
    print(gordo)
    print (desnutrido)
    print (normal)
    

def edades (edad, masa, estatura, documento):
    anterior = 0
    anterior2 = edad[0]
    suma = 0
    masa1 = masa
    masa2 = masa
    estatura1 = estatura
    estatura2 = estatura
    documento1 = documento
    documento2 = documento 
    for i in range (1, len(edad)):
        suma = suma + edad[i]
        if (anterior < edad[i]):
            anterior = edad[i]
            masa1 = masa [i]
            estatura1 = estatura [i]
            documento1 = documento [i]
            
        if (anterior2 > edad[i]):
            anterior2 = edad[i]
            masa2 = masa [i]
            estatura2 = estatura [i]
            documento2 = documento [i]

    print (estatura1, masa1, documento1)
    print (masa2, estatura2, documento2)         
      

documento = [101, 102, 103, 104, 105, 106]
edad = [43,32,76,90,65,34]
estatura = [1.76, 1.80, 1.65, 1.58, 1.76, 1.87]
peso = [89, 76, 43, 78, 90, 126]
     
x = indice_masa_corporal (peso, estatura)    
print (x)

sobrepeso (x, edad, estatura, documento)

edades (edad, peso, estatura, documento)

             
            
                        
                      