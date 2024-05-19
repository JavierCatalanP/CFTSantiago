ruta = "compra"

def archivo(funcion_parametro):
    def funcion_ejecutar(**kwargs):
        # Abre el archivo fuera de la función ejecutora para mantener su estado entre llamadas
        with open(ruta, "a+") as ar:
            return funcion_parametro(ar, **kwargs)  # Pasa directamente el objeto de archivo abierto
    return funcion_ejecutar

@archivo
def Agregar_Compra(obj_ar, **kwargs):  # Asegúrate de recibir el objeto de archivo como primer argumento
    nom_producto = kwargs["nom_producto"]
    cantidad = kwargs["cant"]
    precio_unitario = kwargs["prec_unit"]
    total = kwargs["cant"] * kwargs["prec_unit"]  # Calcula el total correctamente
    fila = "{},{},{},{}\n".format(nom_producto, cantidad, precio_unitario, total)
    obj_ar.write(fila)  # Escribe directamente usando el objeto de archivo pasado

# Ejemplo de uso
data = {"nom_producto": "Hojas", "cant": 100, "prec_unit": 1}
Agregar_Compra(**data)
