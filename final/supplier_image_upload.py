#!/usr/bin/env python3

import os
import requests

url = "http://localhost/upload/"
for file in os.listdir("/home/" + os.getenviron('USER') + "/supplier-data/images/"):
    with open(file, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
