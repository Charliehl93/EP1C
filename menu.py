import pymongo

from crud import *
from funciones import *

while True:
    print("Examen Practico 1")
    print("Menu de opciones")
    print("1. Ver todos los articulos")
    print("2. Buscar un articulo por categoria")
    print("3. Agregar un articulo")
    print("4. Modificar un articulo")
    print("5. Eliminar un articulo")
    print("6. Salir del sistema")
    opcion = input("Ingrese un opcion: ")
    if opcion == "1":
        ver_articulos()
    elif opcion == "2":
        categoria = input("Ingrese la categoria del producto que desea buscar: ")
        ver_articulos(categoria)
    elif opcion == "3":
        articulos = create_json_articulos()
        crear_articulos(articulos)
    elif opcion == "4":
        id = int(input("Ingrese el codigo a modificar: "))
        articulos = create_json_update()
        modificar_articulos(id, articulos)
    elif opcion == "5":
        articulos = int(input("Ingrese el ID que desea eliminar: "))
        eliminar_articulos(articulos)
    else:
        print("opcion no valida");
