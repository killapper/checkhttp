#!/usr/bin/env python
import urllib2
import urlparse
import threading
import re
import os
import sys

def test(domain):
	portlist = [80,81,82,83,84,85,86,87,88,89,808,8080,8081,8082,8083,8084,8085,8086,8086,8087,8088,8089]
	for port in portlist:
		try: 
			response = urllib2.urlopen('http://'+domain+':'+str(port), timeout=5)
			if(response.getcode() == 200):
				print domain
				return
		except:
			domain=domain
	try: 
		response = urllib2.urlopen('https://'+domain, timeout=5)
		if(response.getcode() == 200):
			print domain
			return
	except:
		domain=domain

def arguments():
	import optparse
	parser = optparse.OptionParser()
	parser.add_option('-i', dest='infile', help='input file')
	(options, args) = parser.parse_args()
	if options.infile is None:
		parser.print_help()
		sys.exit(-1)
	return options.infile
def main():
	threads=[]  
	infile = arguments()
	for line in open(infile):
		threads.append(threading.Thread(target=test,args=(line.strip(),)))
	for i in threads:
		i.start()
	for i in threads:
		i.join()

if __name__ == '__main__':
	main();
