#from pelicula import Pelicula
#from libro import Libro

#p = Pelicula()
#l = Libro()

#p.Agregar_Pelicula("Tarzan", "1:25:03", 15)
#p.Agregar_Pelicula("The Good Doctor", "1:25:03", 6)
#p.Agregar_Pelicula("Jobs", "1:55:53", 10)
#p.Agregar_Pelicula("ET", "2:25:07", 1)

#l.Agregar_Libro("Libro Tarzan", 103, 14)
#l.Agregar_Libro("Libro The Good Doctor", 103, 5)
#l.Agregar_Libro("Libro Jobs", 153, 9)
#l.Agregar_Libro("Libro ET", 257, 2)


def Listar_Stock(numero_stock, obj_p, obj_l):
    lista_productos = []
    nueva_lista = []
    
    for pel in obj_p.Listar_Peliculas():
        lista_productos.append(pel)
        
    for lib in obj_l.Listar_Libros():
        lista_productos.append(lib)
        
    for producto in lista_productos:
        if numero_stock >= producto["Stock"]:
            nueva_lista.append(producto)
    
    return nueva_lista

#print(Listar_Stock(2))
