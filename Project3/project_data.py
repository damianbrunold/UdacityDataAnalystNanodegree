#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
import project_audit
"""
This transforms the osm file for the project from xml to json ready to
be imported in mongodb.

It is slightly adapted from the solution for lesson 6 (see data.py)
"""

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

def shape_element(element):
    node = {}
    if element.tag == "node" or element.tag == "way" :
        if element.tag == "node":
            node["type"] = "node"
        else:
            node["type"] = "way"
        for name in element.attrib:
            if name in CREATED:
                if not "created" in node:
                    node["created"] = {}
                node["created"][name] = element.attrib[name]
            elif name == "lat":
                if not "pos" in node:
                    node["pos"] = [0, 0]
                node["pos"][0] = float(element.attrib[name])
            elif name == "lon":
                if not "pos" in node:
                    node["pos"] = [0, 0]
                node["pos"][1] = float(element.attrib[name])
            else:
                node[name] = element.attrib[name]
        for tag in element.iter("tag"):
            if not "k" in tag.attrib: 
                continue
            k = tag.attrib["k"]
            if problemchars.search(k): continue
            if k.startswith("addr:") and k.count(":") == 1:
                if not "address" in node:
                    node["address"] = {}
                key = k[len("addr:"):]
                if k == "addr:street":
                    node["address"][key] = project_audit.update_name(tag.attrib["v"], project_audit.mapping)
                else:
                    node["address"][key] = tag.attrib["v"]
            if not k.startswith("addr:") and k.count(":") == 1:
                node[k.replace(":", "_")] = tag.attrib["v"]
        if element.tag == "way":
            for nd in element.iter("nd"):
                if not "node_refs" in node:
                    node["node_refs"] = []
                node["node_refs"].append(nd.attrib["ref"])
        return node
    else:
        return None

def process_map(file_in, file_out, pretty = False):
    with open(file_out, "w", encoding="utf-8") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")

if __name__ == "__main__":
    process_map('map.osm.xml', "map.osm.json", False)
