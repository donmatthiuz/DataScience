import os
import requests
from bs4 import BeautifulSoup

url = "https://portal.sat.gob.gt/portal/alza-e-importacion-vehiculos/"

os.makedirs("datos", exist_ok=True)

meses_validos = ["enero", "febrero", "marzo", "abril", "mayo"]

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("a", class_="wpfd_downloadlink")

for link in links:
    href = link.get("href", "")
    title = link.get("title", "").lower()

    if href.endswith(".zip") and "alza" not in title:
        if "2024" in title or (
            "2025" in title and any(mes in title for mes in meses_validos)
        ):
            filename = href.split("/")[-1]
            filepath = os.path.join("datos", filename)

            print(f"Descargando: {filename}")
            file_response = requests.get(href)

            with open(filepath, "wb") as f:
                f.write(file_response.content)

            print(f"Guardado en: {filepath}")
