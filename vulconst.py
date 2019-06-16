#!/usr/bin/env python

from bigfloat import *

def GenerateBinary(B, S, W, R):
    if R == 0:
        B = B + S
    else:
        B = GenerateBinary(B, S + "0", W, R-1)
        B = GenerateBinary(B, S + "1", W, R-1)
    return B

VulcanBinary = ""
for i in range(1,9):
    VulcanBinary = GenerateBinary(VulcanBinary, "", i, i)

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
