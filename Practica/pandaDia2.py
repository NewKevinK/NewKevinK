import pandas as pd
import mysql.connector

#Se debe crear una dataframe (Simulando importar datos desde SQL)
datos = {
    'nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Elena'],
    'edad': [25, 30, 22, 35, 28],
    'gasto': [500, 750, 300, 900, 600],
    'ciudad': ['CDMX', 'GDL', 'CDMX', 'MTY', 'GDL']

}

df = pd.DataFrame(datos)

print("1. PRIMERAS FILAS:")
print(df.head(3))

print("\n2. ESTADÍSTICAS RÁPIDAS:")
print(df.describe())  # <- ESTO ES ORO PURO

print("\n3. FILTRAR (muy importante):")
mayores_600 = df[df['gasto'] > 600]
print(mayores_600)

print("\n4. AGRUPAR (clave para el curso):")
gasto_ciudad = df.groupby('ciudad')['gasto'].mean()
print(gasto_ciudad)