#!/usr/bin/env python3
import json

def jsonpydic():
    with open('models/engine/file.json',  'r') as f:
        data = json.load(f)

    return data
