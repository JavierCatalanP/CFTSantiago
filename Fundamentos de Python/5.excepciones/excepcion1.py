a = input("Ingresa el valor de A: ")
b = input("Ingresa el valor de B: ")


try:
    resultado = int(a) / int(b)
    print(resultado)    

except ValueError:
    print("a/b no son numericos, o a y b no son numericos")

except ZeroDivisionError:
    print("Lo siento, no puedes dividir por cero")

except Exception as error:
    print(type(error))
    print("Lo siento, hubo un erorr: ", error )
    
print("Fuera del bloke try-except")