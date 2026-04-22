import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from pathlib import Path

output_dir = Path('graficas')
output_dir.mkdir(exist_ok=True)

#Conexion a la base de datos

conexion = sqlite3.connect('arqueologia.db')

#Consulta SQL para obtener los datos

query = "SELECT * FROM estrellas;"
datos = pd.read_sql_query(query, conexion)

#Cierre de la conexion

conexion.close()

#Grafica 1

plt.figure(figsize=(10, 10))

plt.scatter(datos["pmRA"], datos["pmDE"],s = (datos["Gmag"].max() - datos["Gmag"])**2, alpha=0.2)

plt.xlim(-24, 24)
plt.ylim(-14, 14)

plt.title('Cumulo de estrellas Omega Centauri (Cone Search 0.5 grados)')
plt.xlabel('Movimiento Propio En Ascensión Recta (Grados)')
plt.ylabel('Movimiento Propio En Declinación (Grados)')
plt.gca().invert_xaxis()
plt.savefig(output_dir / 'grafica1.png')

#Consulta SQL para obtener los datos de la grafica 2

query2 = "SELECT * FROM estrellas WHERE pmDE BETWEEN -11 AND -4 AND pmRA BETWEEN -9 AND 1;"
conexion = sqlite3.connect('arqueologia.db')
datos2 = pd.read_sql_query(query2, conexion)
conexion.close()

#Grafica 2

datos2["color"] = (datos2["BPmag"] - datos2["RPmag"])

fig, ax = plt.subplots(figsize=(10, 8))

scatter = ax.scatter(datos2['color'], datos2['Gmag'], 
                     c=datos2['Gmag'], cmap='viridis', 
                     s=5, alpha=0.7)

ax.invert_yaxis()

ax.set_xlabel('Índice de Color (BP - RP)', fontsize=12)
ax.set_ylabel('Magnitud G (mag)', fontsize=12)
ax.set_title('Diagrama Color-Magnitud (Omega Centauri)', fontsize=14)

cbar = plt.colorbar(scatter)
cbar.set_label('Magnitud G')

plt.tight_layout()
plt.savefig(output_dir / 'grafica2.png')


