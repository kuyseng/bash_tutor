#!/usr/bin/python

import sys

def sum(a,b):
    return a + b

a = int(sys.argv[1])
b = int(sys.argv[2])
result = sum(a,b)

print('{} + {} = {}'.format(a, b, result))
