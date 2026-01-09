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

