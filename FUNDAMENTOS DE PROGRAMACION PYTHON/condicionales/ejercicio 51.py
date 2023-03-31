import string


def ejercicio_51 (clase, destino, tviaje, npasajes):
    if (clase == "primera"):
        if (destino == "miami"):
            total = 1300000 * npasajes
        else:
            if (destino == "madrid"):
                total = 2700000 * npasajes    
    if (clase == "segunda"):
        if (destino == "miami"):
            total = 2700000 * npasajes
        else:
            if (destino == "madrid"):
                total = 2500000 * npasajes    
    if (clase == "tercera"):
        if (destino == "miami"):
            total = 1100000 * npasajes
        else:
            if(destino == "madrid"):
                total = 2320000 * npasajes
    if (tviaje == "negocios"):
        total = total
    if (tviaje == "turistico"):
        total = total * 0.9525
    if (tviaje == "familiar"):
        if (npasajes >= 3 and npasajes <= 5):
            total = total * 0.974
        else:
            if (npasajes >= 6 and npasajes <= 10):
                total = total * 0.9462
        if (npasajes >= 11):
            total = total * 0.9276
    return (total) 

if __name__ == "__main__":
    x = input("ingrese la clase en la que desea viajar: ")
    y = input("ingrese el destino del viaje: ")
    z = input("ingrese el tipo de viaje (negocios, familiar, turistico): ")
    i = int(input("ingrese la cantidad de pasajes que desea adquirir: "))
    todo = ejercicio_51 (x,y,z,i)
    print("el total del viaje es: ",todo)           

