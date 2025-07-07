import os
import zipfile
import pandas as pd
import shutil

carpeta_datos = "datos"
carpeta_temporal = os.path.join(carpeta_datos, "temporal")

for nombre_archivo in os.listdir(carpeta_datos):
    if nombre_archivo.endswith(".zip"):
        ruta_zip = os.path.join(carpeta_datos, nombre_archivo)

        with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
            zip_ref.extractall(carpeta_temporal)

            for nombre_extraido in zip_ref.namelist():
                if nombre_extraido.endswith(".txt"):
                    ruta_txt = os.path.join(carpeta_temporal, nombre_extraido)

                    df = pd.read_csv(ruta_txt, sep="|", engine='python')

                    print(f"\nArchivo procesado: {nombre_archivo}")
                    print(df.head())


        if os.path.exists(carpeta_temporal):
            shutil.rmtree(carpeta_temporal)
