def create_json_articulos():
    _id = input("Codigo del Articulo")
    nombre_articulo = input("Nombre articulo: ")
    precio = input("Precio articulo: ")
    categoria = input("Categoria del articulo: ")

    articulos = {

        "_id": _id,
        "nombre_articulo": nombre_articulo,
        "precio": precio,
        "categoria": categoria
    }
    return articulos


def create_json_update():
    print("Menu de opciones")
    print("1. Modificar todos los datos del documento")
    print("2. Modificar un elemento del documento")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        _id = input("Codigo del Articulo")
        nombre_articulo = input("Nombre articulo: ")
        precio = input("Precio articulo: ")
        categoria = input("Categoria del articulo: ")

        articulos = {
            "_id": _id,
            "nombre_articulo": nombre_articulo,
            "precio": precio,
            "categoria": categoria
        }
        return articulos

    elif opcion == "2":
        indice = input("Ingrese el indice: ")
        valor = input("Ingrese el valor a modificar:  ")
        articulos = {indice: valor}
        return articulos
    else:
        print("Dato ingresado no valido")