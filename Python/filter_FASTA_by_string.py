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

# This script takes a file of ID's and converts them into a list.
# Next, it uses values in the first column of a target file to search the ID list.
# Finally, lines in the target file with matched ID's can be split or printed whole.

import sys

##########################################


#Read in target file and intialize empty list for matched IDs
target = open("C:/users/ejspi/desktop/cannabis_genome/purple_kush/canSat3_genome/canSat3_genome.fa")

id = "scaffold50824"
go = False

# Scan target file
	for line in target:
		if go == True:
			if ">" in line:
				go = False
				break
			else:
				sys.stdout.write(line)
				continue
	else:
		if id in line:
			go = True
			sys.stdout.write(line)
		else:
			go = False
			
target.close()


def main():
    pass

if __name__ == '__main__':
    main()


