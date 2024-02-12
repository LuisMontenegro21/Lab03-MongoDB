# Gabriel García 21351
# Luis Pedro Montenegro 21669
# Sebastian Juarez 21471

import pandas as pd
from pymongo import MongoClient, InsertOne

# Leer el archivo usando pandas
dataframe = pd.read_csv('data/movies.csv', encoding='latin1')

# Realizar la coneccion a Mongo
client = MongoClient('mongodb+srv://SebasJuarez:Hola1@lab3.irjc8jp.mongodb.net/')
db = client['Lab3']
collection = db['movies']

# Preparar las oepraciones bulk write 
operations = [InsertOne(row.to_dict()) for index, row in dataframe.iterrows()]

# Ejecutar bulk write
collection.bulk_write(operations)

# Consulta para calculo de ROI (Solo utilizada para generar nuevos datos dentro de la base de datos)
# for movie in collection.find():
#     ROI = ((movie["revenue"] - movie["budget"]) / (movie["budget"]+1)) * 100
#     collection.update_one(
#         {"_id": movie["_id"]},
#         {"$set": {"ROI": ROI}}
#     )

# print("ROI calculado y actualizado para todas las películas.")