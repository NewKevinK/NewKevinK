import pandas as pd
import mysql.connector
import sys
import io

# 1. Conéctate a tu MySQL
conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",      # Reemplaza con tu usuario (quizás 'root')
    password="usbw", # Reemplaza con tu contraseña
    port=3307,        # Puerto por defecto de MySQL
    database="curso_datos"        # Base de datos de sistema, seguro que existe
)
# Configurar la salida para soportar Unicode en Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 2. Verifica la conexión
print("✅ Conexión exitosa:", conexion.is_connected())

# Cambia "database="mysql" por "database="curso_datos"
query = "SELECT * FROM ventas;"
df_ventas = pd.read_sql(query, conexion)
print(df_ventas)
print("\nPrecio promedio:", df_ventas['precio'].mean())

# 4. Cierra la conexión
conexion.close()