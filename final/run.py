#! /usr/bin/env python3

import os
import requests

data_dir = ('supplier-data/descriptions/')
file_list = os.listdir(data_dir)

def post_request(p):
    response = requests.post("http://<external-IP>/fruits/", json=p)
    code = response.status_code
    body = response.text
    print(f"The request returned code {code}." \
          f"{body}")

def create_dicts(files):
    description_d = {}
    fd = []
    for f in files:
        description = os.path.join(data_dir, f)
        with open(description, 'r') as fil:
            key_list = ['name', 'weight', 'description']
            val_list = []
            fil = file.readlines()
            for line in fil:
                if 'lbs' in line:
                    line = line.split(' ')
                    line = int(line[0])
                    val_list.append(line)
                else:
                    val_list.append(line.strip())
            z = zip(key_list, val_list)
            f_d = dict(z)
            post_request(f_d)

        #feedback_d = dict(list(enumerate(fd)))
    #return feedback_d

if __name__=="__main__":
    create_dicts(file_list)
