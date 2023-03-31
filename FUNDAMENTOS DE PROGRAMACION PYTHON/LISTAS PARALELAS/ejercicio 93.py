def subir_sueldo (grupo, sueldos):
    
    acumulador = 0
    numero_empleados = 0
    for i in range (len (sueldos)):
        if (grupo [i] == 1):
            sueldos [i] += 250
            acumulador += sueldos [i]
            numero_empleados += 1
        else: 
            sueldos += 150    
    return (acumulador / numero_empleados)

def cambio_grupo (grupo, salario, promedio):
    for i in range (len (grupo)):
        if (grupo [i] == 1 and salario [i] > promedio):
            grupo [i] = 2
            
            
cedula = [100, 101, 102, 103, 104]
grupo = [1,2,2,1,1]

salario = [1000, 2000, 1500, 3000, 1200]

promedio = subir_sueldo (grupo, salario)
cambio_grupo (grupo, salario, promedio)

print (grupo) 
print (salario)
           
                    