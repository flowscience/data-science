#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     07/04/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#This script takes two ID lists and outputs a matrix indicating whether IDs in a third list are found in either of the first two

print "miRNA \t cin \t csav \t odi"

cs_in = open("C:/rnaseq/ref/cs_mirbase_precursor.txt", "r")
cs = []
for line in cs_in:
    if line.startswith(">"):
        cs.append("-".join(line.split("-")[1:4])[:-11])
cs_in.close

od_in = open("C:/rnaseq/ref/od_mirbase_precursor.txt", "r")
od = []
for line in od_in:
    if line.startswith(">"):
        od.append("-".join(line.split("-")[1:4])[:-11])
od_in.close

#print cs
#print od

ci_in = open("C:/rnaseq/ref/ci_mirbase_precursor.txt", "r")
count = 1
for line in ci_in:
    if line.startswith(">"):
        name = "-".join(line.split("-")[1:4])[:-11]
        #print name
        if name in cs:
            if name in od:
                print name, count, count, count
                count += 1
            else:
                print name, count, count, 0
                count += 1
        else:
            if name in od:
                print name, count, 0, count
                count += 1
            else:
                print name, count, 0, 0
                count += 1
    else:
        pass
ci_in.close

