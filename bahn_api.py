import requests
import json
import pprint
from datetime import *

def bahnhofsInfo():
    basis = "http://transport.opendata.ch/v1/locations"
    bahnhof = input("Von welchem Bahnhof willst du die Koordinaten haben?")
    re = basis + "?query=" + bahnhof
    r = requests.get(re)

    antwort = r.json()
    #pprint.pprint(antwort["stations"])
    bahnhoefe  = []
    for bahnhof in antwort["stations"]:
        bahnhoefe.append(bahnhof["name"])
    return bahnhoefe

def von_nach():
    #datum = input("an welchem datum moechtest du fahren? (DD.MM.YYYY)")
    datum = "20.11.2016"
    datum = datum.split(".")
    for d in datum:
        d = int(d)
    #uhrzeit = input("Um wieviel uhr moechtest du fahren?(HH:MM)")
    uhrzeit = "20:32"
    datum = datum[2] + "-" + datum[1] + "-" + datum[0]


    basis2 = "http://transport.opendata.ch/v1/connections"
    #von = input("Abfahrtsbahnhof")
    #nach = input("Ankunftsbahnhof")
    von = "Mannheim"
    nach = "Karlsruhe"
    anfrage = basis2 + "?from=" + von + "&to=" + nach + "&time=" + uhrzeit + "&date=" + datum
    print(anfrage)
    r = requests.get(anfrage)
    antwort = r.json()
    alle_verbindungen = []
    for verbindung in antwort["connections"]:
        einzel= {}
        einzel["abfahrtzeit"] = datetime.fromtimestamp(int(verbindung["from"]["departureTimestamp"]))
        einzel["abfahrtsort"] = verbindung["from"]["station"]["name"]
        einzel["ankunftszeit"] = datetime.fromtimestamp(int(verbindung["to"]["arrivalTimestamp"]))
        einzel["ankunftsort"] = verbindung["to"]["station"]["name"]
        alle_verbindungen.append(einzel)

    pprint.pprint(alle_verbindungen)
    #print(alle_verbindungen)

von_nach()
