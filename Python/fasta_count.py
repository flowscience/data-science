#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     20/08/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys

def main():
    pass

if __name__ == '__main__':
    main()

f = open("C:/users/eli/desktop/smith lab/data_downloads/aniseed/cionaens.fasta", "r")
#f = open("C:/rnaseq/ref/enscint_fasta.txt", "r")

count=0

for line in f:
    if ">" in line:
        sys.stdout.write(line)
        count+=1
#print count