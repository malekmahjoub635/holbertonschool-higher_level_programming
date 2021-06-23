#!/usr/bin/python3
"""
JSON
"""
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file” """
    with open(filename, encoding="utf-8") as s:
        return json.load(s)
