#!/usr/bin/env python3

import os
import re
from PIL import Image

directory = os.path.join(os.getcwd(), "supplier-data/images/")
file_list = [f for f in os.listdir(directory)) if not f.startswith('.')]
for file in file_list:
    im = Image.open(directory + file)
    fixed = im.resize((600, 400))
    fixed.convert("RGB").save(directory + file, "jpeg")
    print("converted " + file)
