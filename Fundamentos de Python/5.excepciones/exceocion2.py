try:
    archivo = open("Fundamentos de Python/5.excepciones/prueba.txt")
except Exception as error:
    print("Error al abrir archivo:", error)
else:
    print("Archivo abierto, continua...")
finally:
    print("Procedimiento final, Nos vemos...")
    
    