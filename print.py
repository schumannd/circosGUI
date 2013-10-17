#!/usr/bin/python
from __future__ import print_function
import sys, os


def main():
	# ringSegemntsFileName = raw_input("ring segment name file:")
	if len(sys.argv) == 3:
		createRingFragmentsDataFile(sys.argv[1])
		createScatterDataFile(sys.argv[2])
	else:
		print ("""
Usage (Alpha): ./createCircosFiles.py <ring fragments filename>
fragment file should only contain one continous string per line
""")

def createScatterDataFile(filename):
	values = readNumbers(filename)
	
	# normalizing Step
	maximumValue = max(values)
	for i, value in enumerate(values):
		values[i] /= maximumValue

	outputFile = open('scatter.data','w')
	for i, value in enumerate(values):
		line = "label " + str(1) + " " + str(50) + " " + str(value)
		print(line, file=outputFile)

def createRingFragmentsFile(filename):
	ringSegments = readStrings(filename)

	outputFile = open('fragments.data','w')
	for i, name in enumerate(ringSegments):
		line = "chr - label" + str(i+1) + " " + name.strip() + " 0 " + str(100)
		print(line, file=outputFile)

def readStrings(filename):
	with open(filename) as f:
		content = f.readlines()
	return content

def readNumbers(filename):
	content = [float(line.strip()) for line in open(filename)]
	return content

if __name__ == "__main__":
	main()