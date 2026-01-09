import numpy as np
import pandas as pd
import mysql.connector
import sys
import io

conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",      # Reemplaza con tu usuario (quizás 'root')
    password="usbw", # Reemplaza con tu contraseña
    port=3307,        # Puerto por defecto de MySQL
    database="curso_datos"        # Base de datos de sistema, seguro que existe
)
# Configurar la salida para soportar Unicode en Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print("✅ Conexión exitosa:", conexion.is_connected())
query = "SELECT * FROM ventas;"
df_ventas = pd.read_sql(query, conexion)


# Ya deberías tener df_ventas cargado desde MySQL
print("Cantidad total de productos vendidos:", df_ventas['cantidad'].sum())
print("Precio promedio:", df_ventas['precio'].mean())
print("Precio más caro:", df_ventas['precio'].max())
print("Precio más barato:", df_ventas['precio'].min())

# Desviación estándar (medida de dispersión)
print("\nDesviación estándar de precios:", df_ventas['precio'].std())

# Mediana (valor del medio)
print("Mediana de cantidades:", df_ventas['cantidad'].median())


#dia 4
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar para que se vea bien
plt.style.use('default')
sns.set_palette("viridis")

# Gráfico 1: Barras de ventas por producto
plt.figure(figsize=(8, 5))
df_ventas.groupby('producto')['cantidad'].sum().plot(kind='bar')
plt.title('Unidades Vendidas por Producto')
plt.ylabel('Cantidad')
plt.tight_layout()
plt.show()

# Gráfico 2: Dispersión (scatter) cantidad vs precio
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df_ventas, x='cantidad', y='precio', size='cantidad')
plt.title('Relación: Cantidad vs Precio')
plt.show()


conexion.close()