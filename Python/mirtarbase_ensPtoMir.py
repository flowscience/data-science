#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     26/03/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

p = open("C:/rnaseq/mir_targets/mirtarbase_enscinp.txt")
m = open("C:/rnaseq/mir_targets/mirtarbase_mti.txt", "r")

entrez =
for line in m:
    gene_mir = line.split("\t")