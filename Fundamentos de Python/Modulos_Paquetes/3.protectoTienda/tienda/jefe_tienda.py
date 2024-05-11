from pack_tienda.libro import Libro
from pack_tienda.pelicula import Pelicula
from pack_tienda.stock_lista import Listar_Stock

print("____________Bienvenido Admin Tienda____________")
while True: 
    print("")
    print("1. Agregar una pelicula")
    print("2. Listar pelicula")
    print("3. Agregar un Libro")
    print("4. Listar Libros")
    print("5. Ver productos con poco stock")
    print("6. Salir")
    opcion = input("Que quieres hacer?: (1-6)").strip()
    print("")
    p = Pelicula()
    l = Libro()
    if int(opcion) == 1:
        print("____________Datos de la Pelicula____________")
        nom = input("Nombre de la Pelicula: ").strip().capitalize()
        dur = input("Duración: ").strip()
        stock = int(input("Stock: ").strip())
        p.Agregar_Pelicula(nom, dur, stock)
    elif int(opcion) == 2:
        lista = p.Listar_Peliculas()
        print("____________Las Peliculas son:____________")
        print(lista)
    if int(opcion) == 3:
        print("____________Datos del Libro____________")
        nom = input("Nombre del libro: ").strip().capitalize()
        hojas = int(input("Hoja: ").strip())
        stock = int(input("Stock: ").strip())
        l.Agregar_Libro(nom, hojas, stock)
    elif int(opcion) == 4:
        lista = l.Listar_Libros()
        print("____________Los Libros son:____________")
        print(lista)
    elif int(opcion) == 5:
        stock = int(input("Cantidad a evaluar: ").strip())
        lista = Listar_Stock(stock, p, l) 
        print("___Productos con stock menor que "+str(stock)+"___")
        print(lista)
    elif int(opcion) == 6:
        break
    else:
        print("____________Opción Invalidad, favor vuelve a intentar____________")