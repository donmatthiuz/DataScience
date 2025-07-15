import pyreadr
import pandas as pd

# Cargar el archivo .RData
resultados = pyreadr.read_r('nacXanioMes.RData')


# Extraer el DataFrame
df = resultados['nacXanioMes']

# Convertir 'Anio' a entero
df['Anio'] = pd.to_numeric(df['Anio'], errors='coerce')
df = df.dropna(subset=['Anio'])
df['Anio'] = df['Anio'].astype(int)

# Mostrar último año disponible
ultimo_anio = df['Anio'].max()
print("Último año disponible:", ultimo_anio)

# Dividir en conjuntos de entrenamiento y prueba
df_train = df[(df['Anio'] >= 2009) & (df['Anio'] <= 2019)]
df_test  = df[(df['Anio'] >= 2020) & (df['Anio'] <= 2022)]

# Mostrar tamaños
print("Tamaño del conjunto de entrenamiento:", len(df_train))
print("Tamaño del conjunto de prueba:", len(df_test))

