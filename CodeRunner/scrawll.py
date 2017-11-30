#!/usr/bin/python

import urllib2 as url2

f = open("all.txt", 'r')
read = f.readlines()
read_ls = [line.strip('\r\n') for line in read if len(line.strip("\n")) > 5]
print read_ls
read_ls_test = ["salary", "salaries", "wage", "wages", "students", "student"]
final_ls = []
used_urls = []

def scrawl (url, num):
	used_urls.append(url)
	urls = []
	all_url = []
	try:
		request = url2.Request(url)
		print request
		response = url2.urlopen(request)
		print response
		html = response.read()
		#print html
	except url2.URLError, e:
		pass
		
	return final_ls

def main():
	url = "https://www.tnfsh.tn.edu.tw/bin"
	
	return scrawl(url, 0)

print main()
