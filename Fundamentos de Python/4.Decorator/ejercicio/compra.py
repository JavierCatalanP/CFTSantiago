ruta = "ejercicioDecotator"

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

#Ejemplo de uso
data = {"nom_producto": "Hojas", "cant": 10, "prec_unit": 35}
Agregar_Compra(**data)

@archivo
def Listar_Productos(obj_ar):
    obj_ar.seek(0, 0)
    print(obj_ar.read())
Listar_Productos()

@archivo
def Obtener_Productos(obj_ar):
    obj_ar.seek(0, 0)
    return obj_ar.readlines()

resultado = Obtener_Productos()
print(resultado)

def Total_Ventas():
    total_ventas = 0
    for producto in  Obtener_Productos():
        producto = producto.strip("\n")
        total_producto = producto.split(",")[3]
        total_ventas = total_ventas + int(total_producto)
        
    print("El total de ventas del día es: " + str(total_ventas))

Total_Ventas()

def Total_Productos_Vendidos():
    total_cantidad = 0
    for producto in  Obtener_Productos():
        producto = producto.strip("\n")
        cantidad_producto = producto.split(",")[1]
        total_cantidad = total_cantidad + int(cantidad_producto)
        
    print("Se vendieron " +str(total_cantidad)+ " Productos")
    
Total_Productos_Vendidos()