def suma_divi (num):
     suma = 0
     i = 1
     while (i < num):
          if (num % i == 0):
               suma = suma + i
          i = i + 1
     return (suma)

def ejercicio_54 (num):
     return (num == suma_divi (num))

if __name__ == "__main__":
     num = int(input("digite un numero: "))
     resultado = ejercicio_54 (num)
     print("la funcion devolvio: ",resultado)
     
               