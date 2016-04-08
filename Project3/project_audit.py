"""
This code audits and cleans the streets in the osm file used for the project.

It is slightly adapted from the solution for lesson 6 (see audit.py)
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "map.osm.xml"

expected = ["strasse", "weg", "gasse", "feld", "halde", 
            "gässli", "gass", "-Strasse", "-Weg", "platz", 
            "rain", "hof", "garten", "park", "matt", "weid",
            "berg", "grund", "acker", "höhe", "blick", "bach"]

mapping = { "Vorstdt": "Vorstadt",
            "Steinhauserstrassse": "Steinhauserstrasse",
            "St.Oswalds-Gasse": "St. Oswalds-Gasse",
            "Campus GrüentalUnset": "Campus Grüental",
            "Eintrachtsrasse": "Eintrachtstrasse",
            "Zur Weid Rossau": "Zur Weid",
            "Altschlossstrasse;Reidholzstrasse": "Altschlossstrasse",
            "Bahnhofsplatz": "Bahnhofplatz",
            "Bärenacher-Strasse": "Bärenacherstrasse",
            "Chrisimatt": "Chriesimatt",
            "General-Guisan Strasse": "General-Guisan-Strasse",
            "Kapperlerhöhe": "Kappelerhöhe",
            "Saentisrain": "Säntisrain",
            "Schellenmatstrasse": "Schellenmattstrasse",
            "Schnellenmattstrasse": "Schellenmattstrasse",
            "Tellen-Strasse": "Tellenstrasse",
            "Tuergass": "Türgass"
            }

def audit_street_type(street_types, street_name):
    valid = False
    for e in expected:
        if street_name.endswith(e):
            valid = True
            break
    if not valid:
        street_types.add(street_name)

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def streets(osmfile):
    streets = set([])
    for event, elem in ET.iterparse(osmfile, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    streets.add(tag.attrib['v'])
    return sorted(streets)

def update_name(name, mapping):
    for key, value in mapping.items():
        if name.endswith(key):
            return name[0:len(name)-len(key)] + value
    return name

def update_names():
    ss = streets(OSMFILE)
    for name in ss:
        better_name = update_name(name, mapping)
        if better_name != name:
            print(name, "=>", better_name)

if __name__ == '__main__':
    update_names()
