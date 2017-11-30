#!/usr/bin/python
# encoding: utf-8

import urllib2

request = urllib2.Request("http://tech-marsw.logdown.com/blog/2016/01/10/01-basic-crawler")
response = urllib2.urlopen(request)
html = response.read()
print html

fileout = file("01_blog.html","w")
fileout.write(html)
fileout.close()
