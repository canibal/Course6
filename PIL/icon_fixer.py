#!/usr/bin/env python3

import os
import re
from PIL import Image

file_list = [f for f in os.listdir(os.path.join(os.getcwd(), "images/")) if not f.startswith('.')]
for file in file_list:
    im = Image.open("images/" + file)
    fill_color = (255,255,255)
    im = im.convert("RGBA")
    if 'black' in str(file):
        if im.mode in ('RGBA', 'LA'):
            background = Image.new(im.mode[:-1], im.size, fill_color)
            background.paste(im, im.split()[-1]) # omit transparency
            im = background
    fixed = im.rotate(-90).resize((128, 128))
    fixed.convert("RGB").save("./opt/icons/" + file, "jpeg")
    print("converted " + file)
