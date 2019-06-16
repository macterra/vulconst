#!/usr/bin/env python

from bigfloat import *

VulcanBinary = ""

def GenerateBinary(S, W, R):
    global VulcanBinary

    if R == 0:
        VulcanBinary = VulcanBinary + S
    else:
        GenerateBinary(S + "0", W, R-1)
        GenerateBinary(S + "1", W, R-1)

for i in range(1,9):
    GenerateBinary("", i, i)

print '.' + VulcanBinary
print len(VulcanBinary)

with precision(2000):
    VulcanDecimal = BigFloat(0)
    b = BigFloat(1)

    for c in VulcanBinary:
        b = b/2.
        if c == '1':
            VulcanDecimal = VulcanDecimal+b

print VulcanDecimal
