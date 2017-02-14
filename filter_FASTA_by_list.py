#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     19/12/2013
# Copyright:   (c) Eli 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Simple solution for one or multiple ID's, can also be adopted to read files containing 
#a list of ID's one per line by adding an extra for loop to populate the ID list. 
#This script returns entries from ~1GB files in about 1s on my 5th-gen i5.

import sys

#Read in target file

#Setup list
ids = ["AccessionNumber1", "AccessionNumber2", "etc..."]

#Set conditional
go = False

#Read target file
target = open("C:/file_path.txt")

for line in target:
	if go == True:
		if ">" in line:
			go = False
			continue
		else:
			sys.stdout.write(line)
			continue
	else:
		for id in ids:
			if id in line:
				go = True
				sys.stdout.write(line)
			else:
				continue
			
target.close()


def main():
    pass

if __name__ == '__main__':
    main()


