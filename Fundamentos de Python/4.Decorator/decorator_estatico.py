#def saludo():
  #  print("Hola")
    
#objetoS = saludo #Estoy convertiendo la función en un objeto llamado "objetoS"

#objetoS()

def funcion_principal(funcion_parametro):
    print("Dentro de funcion principal")
    
    def funcion_ejecutar():
        print("Dentro de funcion ejecutar")
        funcion_parametro()
        
    return funcion_ejecutar #Hasta aqui es un Decorator, nos puede servir para cuando tengamos que ejecutar muchas funciones 25
    
def saludo():
    print("Hola")
    
def pregunta():
    print("Como estas?")
    
respuesta = funcion_principal(pregunta)
respuesta()

