import csv
import sys 
import os
import hashlib



inFile = sys.argv[1]

def inMeth(inFile):
	with open((inFile),'rb') as file:
   		contents = csv.reader(file, delimiter=',')



fileContents = [ x.split(',') for x in ''.join(open(inFile).readlines()).splitlines() ]



print fileContents















	
			
			






