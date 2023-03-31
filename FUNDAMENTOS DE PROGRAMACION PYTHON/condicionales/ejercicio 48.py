def ejercicio_48 (tiposervicio,hora,tipoproducto,tonelada):
    if (tiposervicio ==1):
        if (tipoproducto == 1):
            if (tonelada < 10):
                total = 10000 * tonelada
            else:
                if (tonelada >= 10):
                    total = 7000 * tonelada
        else:
            if (tipoproducto == 2):
                if (tonelada < 10 ):
                    total = 50000 * tonelada
                else:
                    if (tonelada >= 10):
                        total = 50000 + (5000 * (tonelada - 10))
    else:
        if (tiposervicio == 2):
            if (hora > 2):
                total = 2000 * hora
    return (total)

if __name__ == "__main__":
    x = int(input("ingrese el tipo de servicio: "))
    y = int(input("ingrese las horas consumidas: "))
    z = int(input("ingrese el tipo de producto: "))
    i = int(input("ingrese las toneladas de carga: "))
    totalpagar = ejercicio_48(x,y,z,i)
    print("el total a pagar es: ",totalpagar)
    
                                        
                
                                    
                