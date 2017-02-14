#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     21/01/2015
# Copyright:   (c) Eli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#This script takes an input file of sequences & ID's tab separated 1 pair per
#   line and converts it into a multi-FASTA format file.

#Load dependencies
import sys
import textwrap

#Load sequence file
f = open("C:/users/eli/desktop/smith_lab/geo_data/adult_organs/GPL5576_seq_tab.txt")

#Reformat and print each line, one by one
for line in f:
    name = line.strip("\n").split("\t")[0] #Use proper column index for name
    # description = line.strip("\n").split("\t")[0] #Use proper column index(es) for annotation
    seq = line.strip("\n").split("\t")[1] #Use proper column index for sequence
    seq = textwrap.fill(seq, 80) #Reformat maximum characters per line
    sys.stdout.write("> " + name + "\n") #Print FASTA header
    print seq #Return reformatted sequence

#Close sequence file
f.close





def main():
    pass

if __name__ == '__main__':
    main()
