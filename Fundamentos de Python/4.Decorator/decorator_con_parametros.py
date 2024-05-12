#def saludo():
  #  print("Hola")
    
#objetoS = saludo #Estoy convertiendo la función en un objeto llamado "objetoS"

#objet"""oS()
"""
def funcion_principal(funcion_parametro):
    print("Dentro de funcion principal")
    
    def funcion_ejecutar():
        print("Dentro de funcion ejecutar")
        funcion_parametro()
        
    return funcion_ejecutar #Hasta aqui es un Decorator, nos puede servir para cuando tengamos que ejecutar muchas funciones 25
    
def saludo(nombre):
    print("Hola", nombre)
    
def pregunta(nombre):
    print("Como estas?", nombre)
    
saludo("Javier")
pregunta("Javier")
"""    
#respuesta = funcion_principal(pregunta)
#respuesta()

#def saludo():
  #  print("Hola")
    
#objetoS = saludo #Estoy convertiendo la función en un objeto llamado "objetoS"

#objetoS()

def funcion_principal(funcion_parametro):
    print("Dentro de funcion principal")
    
    def funcion_ejecutar(nom):
        print("Dentro de funcion ejecutar")
        return funcion_parametro(nom)
        
    return funcion_ejecutar #Hasta aqui es un Decorator, nos puede servir para cuando tengamos que ejecutar muchas funciones 25
    
def saludo(nombre):
    print("Hola", nombre)
    
def pregunta(nombre):
    print("Como estas?", nombre)
 
respuesta = funcion_principal(pregunta)
respuesta("Javier")
