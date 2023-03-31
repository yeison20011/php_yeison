def ejercicio_47 (tipoPlan, minutos, mensajes):
    if (tipoPlan < 3):   
        
        if (tipoPlan == 1):
            totalpagar = 80000
            if (minutos > 100):
                totalpagar = totalpagar + (855 * (minutos - 100))
                if (mensajes > 10):
                    totalpagar = totalpagar + (370 * (mensajes - 10))
        else:
            if (tipoPlan == 2):
                totalpagar = 120000
                if (minutos > 135):
                    totalpagar = totalpagar + (855 * (minutos - 135))
                    if (mensajes > 20):
                        totalpagar = totalpagar + (370 * (mensajes - 20))
        if (tipoPlan == 3):
            totalpagar = 180000
            if (minutos > 425):
                totalpagar = totalpagar + (855 * (minutos - 425))                            
                if (mensajes > 30):
                    totalpagar = totalpagar + (370 * (mensajes - 30))
           
        return (totalpagar)           

if __name__ == "__main__":
    tipoPlan = int(input("ingrese el tipo de plan de telefonia: "))
    minutos = int(input("ingrese la cantidad de minutos consumidos durante el mes: "))
    mensajes = int(input("ingrese la cantidad de minutos consumidos durante el mes: ")) 
    total = ejercicio_47(tipoPlan,minutos,mensajes)
    print("el total a pagar es: ",total)