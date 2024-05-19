def decorador(funcion_parametro):
    def funcion_ejecutar(a, b):
        a = int(a)
        b = int(b)
        return funcion_parametro(a, b)
    
    return funcion_ejecutar

@decorador
def suma(a, b):
    c = a + b
    return c

@decorador
def resta(a, b):
    c = a - b
    return c

resultado = resta(10, 2)
print(resultado)