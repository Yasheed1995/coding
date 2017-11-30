#!/usr/bin/python
import string
a = "ifpmluglesecdlqp_rclfrseljpkq"
d = []

for ch in a:
	c = 0
	
	b = ord(ch)
	b = b - 97
	for i in xrange(1,5):
		if ( (b + 27 * i) - 15 ) % 4 == 0:
			c = ( (b + 27 * i) - 15 ) / 4
			if c >= 27:
				c = c % 27
			d.append(c)
			
print d
e = ""
for i in d:
	if i == 26:
		e += "_"
	else:
		e += chr(i + 97)
	
	
print e