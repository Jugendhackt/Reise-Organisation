import requests
import json
import pprint

basis = "http://transport.opendata.ch/v1/locations"
bahnhof = input("Von welchem Bahnhof willst du die Koordinaten haben?")
re = basis + "?query=" + bahnhof
r = requests.get(re)

antwort = r.json()
#pprint.pprint(antwort["stations"])
bahnhoefe  = []
for bahnhof in antwort["stations"]:
    bahnhoefe.append(bahnhof["name"])

print(bahnhoefe)

basis2 = "http://transport.opendata.ch/v1/conections"
