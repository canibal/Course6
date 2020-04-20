#!/usr/bin/env python3
"""Change the image."""

import os
from PIL import Image

directory = os.path.join(os.getcwd(), "supplier-data/images/")
file_list = [f for f in os.listdir(directory) if f.endswith('.tiff')]
for file in file_list:
    im = Image.open(directory + file)
    fixed = im.resize((600, 400))
    fixed.convert("RGB").save(directory + os.path.splitext(file)[0] + '.jpeg', "jpeg")
    print("converted " + file)
