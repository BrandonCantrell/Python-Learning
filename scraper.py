import time 
import urllib2
from urllib2 import urlopen
import datetime
from sys import argv

website = argv[1]
topSplit = '<div class=\"post\">'
bottomSplit = '<div class=\"sp_right\">'



def main():
	try:
		sourceCode = urllib2.urlopen(website).read()
		#print sourceCode
		sourceSplit = sourceCode.split(topSplit)[1].split(bottomSplit)[0]
		print sourceSplit


	except Exception,e:
		print 'failed in the main loop'
		print str(e)

main()
