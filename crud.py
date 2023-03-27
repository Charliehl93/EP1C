from conexion import collection
import json


def ver_articulos(categoria=None):
    if categoria is not None:
        query = {"categoria": categoria}
        document = collection.find_one(query)
        print(document)
    else:
        documents = collection.find()
        for document in documents:
            print(document)


def crear_articulos(json_articulos):
    result = collection.insert_one(json_articulos)
    print(result.inserted_id)


def modificar_articulos(id, json_articulos_update):
    query = {"_id": id}
    new_values = {"$set": json_articulos_update}
    result = collection.update_one(query,new_values)
    print(result.modified_count)

def eliminar_articulos(nombre_articulo=None):
    if nombre_articulo is not None:
        query = {"nombre_articulo": nombre_articulo}
        document = collection.delete_one(query)
        print(document.deleted_count)
    else:
        documents = collection.find()
        for document in documents:
            print(document)