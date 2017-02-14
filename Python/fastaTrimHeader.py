#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     18/12/2013
# Copyright:   (c) Eli 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import sys

#print "This script outputs a new file with the last 12 characters in each record name removed."

file_in = open("C:/rnaseq/ref/ci_mirbase_mature_sorted.fasta", "r")
file_out = open("C:/rnaseq/ref/ci_mirbaseTRIM_mature_sorted.fasta", "w")

#lines = []

for line in file_in:
    if ">" in line:
        new = line[:-13]
        file_out.write(new + "\n")
        sys.stdout.write(new + "\n")
    else:
        file_out.write(new + "\n")
        sys.stdout.write(line)

file_in.close()
file_out.close()
