import pandas as pd

# Cargar el dataset
df = pd.read_csv("data/market.csv")

# Mostrar las primeras filas
print("Primeras filas del dataset:")
print(df.head())

# Información general
print("\nInformación del dataset:")
print(df.info())

# Valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Filas duplicadas
print("\nFilas duplicadas:")
print(df.duplicated().sum())

# Eliminar duplicados
df = df.drop_duplicates()

# Eliminar filas con valores nulos
df = df.dropna()

# Guardar el dataset limpio
df.to_csv("data/market_limpio.csv", index=False)

print("\nLimpieza completada correctamente.")
