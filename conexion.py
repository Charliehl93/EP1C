import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017")
base = cliente["examen1"]
collection = base["articulos"]