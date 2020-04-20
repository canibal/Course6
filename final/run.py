#! /usr/bin/env python3

import os
import requests

data_dir = ('supplier-data/descriptions/')
file_list = os.listdir(data_dir)

def post_request(p):
    response = requests.post("http://35.223.215.137/fruits/", json=p)
    code = response.status_code
    body = response.text
    print("The request returned code {}.".format(code), body)

def create_dicts(files):
    description_d = {}
    fd = []
    for f in files:
        description = os.path.join(data_dir, f)
        with open(description, 'r') as file:
            key_list = ['name', 'weight', 'description', 'image_name']
            val_list = []
            fil = file.readlines()
            for line in fil:
                if 'lbs' in line:
                    line = line.split(' ')
                    line = int(line[0])
                    val_list.append(line)
                else:
                    val_list.append(line.strip())
            val_list.append(os.path.splitext(f)[0] + '.jpeg')
            print(val_list)
            z = zip(key_list, val_list)
            f_d = dict(z)
            post_request(f_d)

        #feedback_d = dict(list(enumerate(fd)))
    #return feedback_d

if __name__=="__main__":
    create_dicts(file_list)
