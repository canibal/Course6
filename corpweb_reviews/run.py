#! /usr/bin/env python3

import os
import requests
import json

data_dir = ('data/feedback/')
file_list = os.listdir(data_dir)

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
            fd.append(f_d)
        feedback_d = dict(list(enumerate(fd)))
    return feedback_d



if __name__=="__main__":
    print(create_dicts(file_list))
