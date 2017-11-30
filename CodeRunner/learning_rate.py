#!/usr/bin/python
import math
from decimal import *
a = 0.027
fstr = repr(a)
print fstr
signif_digits, fract_digits = fstr.split('.')
fract_lastdigit = int(fract_digits[-1])
print fract_lastdigit
interval = 10 ** (-len(fract_digits)-1)
print a + interval * 10
w = float('nan')
print w

print (0.1 + 0.1 + 0.1 - 0.3) == 0

x = 0.017221999999999998
print round(x - 0.005, 2)
signif_digits, fract_digits = repr(x).split('.')
print fract_digits
for i in range(len(fract_digits)):
	if fract_digits[i] == '9' and fract_digits[i+1] == '9' and fract_digits[i+2] == '9':
		print round(math.floor(x * (10 ** (i+1))) / 10 ** (i+1), i)
		break

