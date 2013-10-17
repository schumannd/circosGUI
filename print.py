#!/usr/bin/python
from __future__ import print_function
import sys, os


def main():
	# ringSegemntsFileName = raw_input("ring segment name file:")
	if len(sys.argv) == 2:
		createRingFragmentsFile(sys.argv[1])
	else:
		print ("""
Usage (Alpha): ./createCircosFiles.py <ring fragments filename>
fragment file should only contain one continous string per line
""")

def createRingFragmentsFile(fileName):
	ringSegments = readFile(fileName)

	outputFile = open('fragments.data','w')

	for i, name in enumerate(ringSegments):
		line = "chr - label" + str(i+1) + " " + name.strip() + " 0 " + str(100)
		print(line, file=outputFile)

def readFile(fname):
	with open(fname) as f:
		content = f.readlines()
	return content

if __name__ == "__main__":
	main()