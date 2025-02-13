#!/usr/bin/env python3

# Author ID: cthomas49

import subprocess


def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
    output = p.communicate()
    
    return output[0].decode('utf-8').strip()

print(free_space())

