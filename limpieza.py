import zipfile
import pandas as pd
import os

carpeta = 'datos'


archivos_zip = [f for f in os.listdir(carpeta) if f.lower().endswith('.zip')]

if not archivos_zip:
    raise Exception("No se encontraron archivos ZIP en la carpeta datos")

nombre_zip = archivos_zip[0]
ruta_zip = os.path.join(carpeta, nombre_zip)

print(f"Archivo ZIP seleccionado: {ruta_zip}")

with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
    archivos = zip_ref.namelist()
    archivo_txt = next((f for f in archivos if f.endswith('.txt')), None)
    if archivo_txt is None:
        raise Exception("No se encontró archivo .txt dentro del ZIP")
    with zip_ref.open(archivo_txt) as file:
        df = pd.read_csv(file, encoding='latin-1', sep='|')

nombre_csv = archivo_txt.replace('.txt', '.csv')
ruta_csv = os.path.join(carpeta, nombre_csv)
df.to_csv(ruta_csv, index=False)

print(f"Archivo CSV guardado en: {ruta_csv}")
