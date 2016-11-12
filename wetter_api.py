import requests
import pprint
import json
import datetime

key = "1c362da74ba5df2969451af029bffbe5"
basis = "http://api.openweathermap.org/data/2.5/forecast?"
land = "XA-DE"
stadt = "Mannheim"
datum = "2016-11-15 15:00:00"

def wettervorhersage():
    ergebnis = {}
    wedaten = basis + "q=" +land + "," + stadt + "&mode=json" + "&APPID=" + key
    r = requests.get(wedaten)
    antwort = r.json()
    for wvhsage in antwort["list"]:
        if wvhsage["dt_txt"] == datum:
            ergebnis["beschreibung"] = wvhsage["weather"][0]["description"]
            ergebnis["temp"] = int(wvhsage["main"]["temp"]) - 273.15
            ergebnis["stadt"] = stadt

    with open('wetter.json', 'w') as wetterjson:
        json.dump(ergebnis, wetterjson)

wettervorhersage()