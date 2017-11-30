#!/usr/bin/python
import sys

ip = sys.argv[1]
def convertIP(ip):
	print '.'.join([bin(int(x)+256)[3:] for x in ip.split('.')])
convertIP(ip)
