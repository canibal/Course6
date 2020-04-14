#! /usr/bin/env python3

import os
import requests

data_dir = ('data/feedback/')
file_list = os.listdir(data_dir)

def post_request(p):
    response = requests.post("http://<corpweb-external-IP>/feedback/", json=p)
    code = response.status_code
    body = response.text
    print(f"The request returned code {code}." \
          f"{body}")

def create_dicts(files):
    feedback_d = {}
    fd = []
    for f in files:
        feedback = os.path.join(data_dir, f)
        with open(feedback, 'r') as fi:
            key_list = ['title', 'name', 'date', 'feedback']
            val_list = []
            for line in fi.readlines():
                val_list.append(line.strip())
            z = zip(key_list, val_list)
            f_d = dict(z)
            post_request(f_d)
        #feedback_d = dict(list(enumerate(fd)))
    #return feedback_d

if __name__=="__main__":
    create_dicts(file_list))
