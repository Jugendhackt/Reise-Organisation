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

def von_nach():
    hinfahrt = "20.11.2016"
    zuhause = "Karlsruhe"
    urlaub = "Mannheim"
    rueckfahrt = "22.11.2016"

    hinverbindung = anfrage(zuhause, urlaub, hinfahrt)
    rueckverbindung = anfrage(urlaub, zuhause, rueckfahrt)
    gesamtpreis = int(hinverbindung["preis"]) + int(rueckverbindung["preis"])
    del hinverbindung["preis"]
    del rueckverbindung["preis"]
    antwort = {}
    antwort["zuhause"] = zuhause
    antwort["urlaub"] = urlaub
    antwort["hin"] = hinverbindung
    antwort["rueck"] = rueckverbindung
    antwort["preis"] = gesamtpreis

    return antwort






def anfrage(zuhause, urlaub, fahrt):
    fahrt = fahrt.split(".")
    #uhrzeit = input("Um wieviel uhr moechtest du fahren?(HH:MM)")
    uhrzeit = "02:00"
    fahrt = fahrt[2] + "-" + fahrt[1] + "-" + fahrt[0]


    basis2 = "http://transport.opendata.ch/v1/connections"
    #zuhause = input("Abfahrtsbahnhof")
    #urlaub = input("Ankunftsbahnhof")
    anfrage = basis2 + "?from=" + zuhause + "&to=" + urlaub + "&time=" + uhrzeit + "&date=" + fahrt
    r = requests.get(anfrage)
    antwort = r.json()
    alle_verbindungen = []
    for verbindung in antwort["connections"]:
        #pprint.pprint(verbindung)
        einzel= {}
        abfahrt = datetime.fromtimestamp(int(verbindung["from"]["departureTimestamp"]))
        einzel["abfahrtzeit"] = abfahrt.strftime("%Y-%m-%d %H:%M:%S")
        ankunft = datetime.fromtimestamp(int(verbindung["to"]["arrivalTimestamp"]))
        einzel["ankunftszeit"] = ankunft.strftime("%Y-%m-%d %H:%M:%S")
        einzel["umstiege"] = verbindung["transfers"]
        einzel["zugart"] = verbindung["products"]
        zeit = ankunft - abfahrt
        zeit = zeit.total_seconds()
        einzel["reisezeit"] = zeit / 60
        einzel["preis"] = einzel["reisezeit"] * 0.5
        alle_verbindungen.append(einzel)

    zeit2 = 100000
    for verbindung in alle_verbindungen:
        if verbindung["reisezeit"] < zeit2:
            zeit2 = verbindung["reisezeit"]
            schnellste = verbindung
    return schnellste

def anJson():
    fahrplan = von_nach()
    fahrplan = json.dumps(fahrplan)
    return fahrplan