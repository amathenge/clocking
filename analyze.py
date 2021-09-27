#!/usr/bin/env python

import os

f = open("ACRES 18062021.txt", "r")
a = []

for line in f:
    line = line.strip()
    if 'FFFFFFFF' in line:
        line = line.split()
        if line[1] not in a:
            a.append(line[1])

print('Results')
for item in a:
    print(item)

f.close()