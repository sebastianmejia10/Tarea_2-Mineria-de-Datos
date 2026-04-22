import pandas as pd
import sqlite3

datos = pd.read_csv("omega_bruto.csv")

#indices con NaN

indices = datos[datos.isna().any(axis=1)].index.tolist()

#Datos limpios

datos_limpios = datos.drop(indices)

#Creacion de base de datos 

conexion = sqlite3.connect("arqueologia.db")
datos_limpios.to_sql("estrellas", conexion, if_exists="replace", index=False)
conexion.close()