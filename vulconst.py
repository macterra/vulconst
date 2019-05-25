#!/usr/bin/env python

from bigfloat import *

VN = ""

def om(S, W, R):
    global VN

    if R == 0:
        VN = VN + S
    else:
        om(S + "0", W, R-1)
        om(S + "1", W, R-1)

for i in range(1,9):
    om("", i, i)

print '.' + VN

with precision(2000):
    V = BigFloat(0)
    b = BigFloat(1)

    for c in VN:
        b = b/2.
        if c == '1':
            V = V+b

print V
