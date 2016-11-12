import requests
import json
import pprint
from datetime import *
import math

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

def von_nach(zuhause, urlaub):
    #hinfahrt = input("an welchem hinfahrt moechtest du fahren? (DD.MM.YYYY)")
    hinfahrt = "20.11.2016"
    hinfahrt = hinfahrt.split(".")
    for d in hinfahrt:
        d = int(d)
    #uhrzeit = input("Um wieviel uhr moechtest du fahren?(HH:MM)")
    uhrzeit = "10:00"
    hinfahrt = hinfahrt[2] + "-" + hinfahrt[1] + "-" + hinfahrt[0]


    basis2 = "http://transport.opendata.ch/v1/connections"
    #zuhause = input("Abfahrtsbahnhof")
    #urlaub = input("Ankunftsbahnhof")
    anfrage = basis2 + "?from=" + zuhause + "&to=" + urlaub + "&time=" + uhrzeit + "&date=" + hinfahrt
    print(anfrage)
    r = requests.get(anfrage)
    antwort = r.json()
    alle_verbindungen = []
    for verbindung in antwort["connections"]:
        #pprint.pprint(verbindung)
        einzel= {}
        einzel["abfahrtzeit"] = datetime.fromtimestamp(int(verbindung["from"]["departureTimestamp"]))
        einzel["abfahrtsort"] = verbindung["from"]["station"]["name"]
        einzel["ankunftszeit"] = datetime.fromtimestamp(int(verbindung["to"]["arrivalTimestamp"]))
        einzel["ankunftsort"] = verbindung["to"]["station"]["name"]
        einzel["umstiege"] = verbindung["transfers"]
        einzel["zugart"] = verbindung["products"]
        zeit = einzel["ankunftszeit"] - einzel["abfahrtzeit"]
        zeit = zeit.total_seconds()
        einzel["reisezeit"] = zeit / 60
        einzel["preis"] = einzel["reisezeit"] * 0.5
        alle_verbindungen.append(einzel)


    for verbindung in alle_verbindungen:
        if verbindung["reisezeit"] < 100000:
            zeit = verbindung["reisezeit"]
            schnellste = verbindung
    pprint.pprint(schnellste)

von_nach()
