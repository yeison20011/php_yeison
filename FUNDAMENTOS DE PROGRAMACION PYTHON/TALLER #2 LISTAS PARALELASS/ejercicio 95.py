def matricula (edad, zona):
    lista = []
    for i in range (len(zona)):
        if (zona[i] == 1):
            valor = 1000000
            if (edad[i] < 18):
                valor = 1000000 * 0.30
            lista.append (valor)
        else:
            if (zona[i] == 2):
                valor = 500000
                if (edad[i] < 18):
                    valor = 500000 * 0.30
                lista.append (valor)
    return (lista)                        
                 

codigo = [100,101,102,103,104,105]
edad = [23, 18, 34, 16, 28,17]
zona = [1,1,2,1,2,1]

total = matricula (edad, zona)
print (codigo)
print (edad)
print (zona)
print (total)