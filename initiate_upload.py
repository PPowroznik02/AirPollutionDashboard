from urllib.request import urlopen
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import json
import csv
from arcgis.gis import GIS
from arcgis.features import GeoAccessor, FeatureLayer

# polaczenie sie do arcgis online
f = open('logowanie.json')
logowanie = json.load(f)
gis = GIS("http://www.arcgis.com", logowanie["login"], logowanie["haslo"])

csv_file_path = r"dane_z_sensorow.csv"

# podanie nazwy hostowanej warstwy w arcgis online
feature_layer_name = "stan_powietrza"


try:
    # odczytanie pliku csv
    csv_item = gis.content.add({}, csv_file_path)
    # stworzenie feature layer
    csv_feature_layer = csv_item.publish()

    # zmiana nazwy hostowanej warstwy
    csv_feature_layer.update({'title': feature_layer_name})

    print(f"Successfully uploaded and published")

except Exception as e:
    print(f"Error uploading CSV data: {e}")
