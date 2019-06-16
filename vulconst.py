#!/usr/bin/env python

from bigfloat import *
import string

def GenerateBitstring(bitstring, suffix, recurse):
    if recurse == 0:
        bitstring = bitstring + suffix
    else:
        bitstring = GenerateBitstring(bitstring, suffix + "0", recurse-1)
        bitstring = GenerateBitstring(bitstring, suffix + "1", recurse-1)
    return bitstring

VulcanBinary = ""
MaxRecursion = 8

for i in range(1,MaxRecursion+1):
    VulcanBinary = GenerateBitstring(VulcanBinary, "", i)

print '.' + VulcanBinary

with precision(2000):
    VulcanDecimal = BigFloat(0)
    b = BigFloat(1)

    for c in VulcanBinary:
        b = b/2.
        if c == '1':
            VulcanDecimal = VulcanDecimal+b

print VulcanDecimal
print string.join([x + ', ' for x in str(VulcanDecimal)[2:]])
