#!/usr/bin/python

from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str =raw_input("enter the string")
print str.translate(trantab)
