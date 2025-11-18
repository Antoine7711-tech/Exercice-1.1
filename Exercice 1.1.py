#importer csv
import pandas as pd

df = pd.read_csv("netflix_titles.csv")

print(df)

#----------------------------
#importer json
import json as js

# Chemin vers le fichier JSON
file_path = "covid_19.json"

# Lecture du fichier JSON
with open(file_path, "r", encoding="utf-8") as file:
    data = js.load(file)

# Affichage des données importées
print(data)

#----------------------------
#importer xml
print("-------------------------")
import xml.etree.ElementTree as ET
# Chemin vers le fichier XML
file_path = "clinical_trials.xml"
# Lecture et analyse du fichier XML
tree = ET.parse(file_path)
root = tree.getroot()

# Affichage de la racine du fichier XML
print(f"Racine : {root.tag}")

# Exemple : Parcourir les éléments enfants
for child in root:
    print(f"Tag : {child.tag}, Attributs : {child.attrib}")

#----------------------------
#importer html
print("-------------------------")

# Chemin vers le fichier HTML
file_pathh = "lsm.html"
from bs4 import BeautifulSoup

# Lecture du fichier HTML
with open(file_pathh, "r", encoding="utf-8") as file:
    html_content = file.read()

# Affichage du contenu HTML
print(html_content)


# Analyse du contenu HTML
soup = BeautifulSoup(html_content, "html.parser")

# Affichage du contenu formaté
print(soup.prettify())