#!/usr/bin/env python

from bigfloat import *

def GenerateBitstring(bitstring, suffix, recurse):
    if recurse == 0:
        bitstring = bitstring + suffix
    else:
        bitstring = GenerateBitstring(bitstring, suffix + "0", recurse-1)
        bitstring = GenerateBitstring(bitstring, suffix + "1", recurse-1)
    return bitstring

VulcanBinary = ""
for i in range(1,9):
    VulcanBinary = GenerateBitstring(VulcanBinary, "", i)

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
