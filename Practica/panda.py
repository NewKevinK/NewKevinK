# IF - ELIF - ELSE (decisiones)
edad = 20
if edad < 18:
    print("Menor de edad")
elif edad < 65:
    print("Adulto")
else:
    print("Adulto mayor")

# FOR LOOP (Repetir)
for i in [1, 2, 3, 4, 5]:
    print(i)

# WHILE (mientras sea cierto)
contador = 0
while contador < 3:
    print(contador)
    contador += 1


def calcular_promedio(numeros):
    """Esta función calcula el promedio"""
    return sum(numeros) / len(numeros)

# Úsala
resultado = calcular_promedio([10, 20, 30])
print(resultado)  # Imprime 20


import numpy as np
arreglo = np.array([1, 2, 3, 4, 5])
print(arreglo.mean())  # Promedio: 3.00


import pandas as pd
# Crear DataFrame (tabla de datos)
df = pd.DataFrame({
    'nombre': ['Ana', 'Luis', 'María'],
    'edad': [25, 30, 22],
    'gasto': [500, 750, 300]
})

print(df.head())  # Ver primeras filas
print(df['edad'].mean())  # Promedio de edad


import matplotlib.pyplot as plt
import seaborn as sns
# Gráfico de barras simple
df['gasto'].plot(kind='bar')
plt.title("Gasto por cliente")
plt.show()