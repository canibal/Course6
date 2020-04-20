#!/usr/bin/env python3

import os
import requests

url = "http://localhost/upload/"
file_list = [f for f in os.listdir("supplier-data/images/") if f.endswith('.jpeg')]
for file in file_list:
    with open(os.path.join('supplier-data/images/', file), 'rb') as opened:
        r = requests.post(url, files={'file': opened})
