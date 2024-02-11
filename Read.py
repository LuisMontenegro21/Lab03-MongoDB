import pandas as pd
from pymongo import MongoClient, InsertOne

# Leer el archivo usando pandas
dataframe = pd.read_csv('your_file.csv')

# Realizar la coneccion a Mongo
client = MongoClient('string_de_coneccion')
db = client['cliente']
collection = db['nombre_base']

# Preparar las oepraciones bulk write 
operations = [InsertOne(row.to_dict()) for index, row in df.iterrows()]

# Ejecutar bulk write
collection.bulk_write(operations)
