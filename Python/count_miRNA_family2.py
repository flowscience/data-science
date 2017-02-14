#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     24/03/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import collections

f = open("C:/rnaseq/ref/ascidian_mirs_sorted.txt", "r")

mirs = []
last = ("", "")
for line in f:
    mir = line.split()[0]
    #print last, mir
    species = line.split()[2]
    mir = "-".join(mir.split("-")[0:2])
    if (line.split()[0][-3:] == "-5p" or "-3p") and last == (mir, species):
        pass #dont add other arm to list for counting
    elif mir[-1].isdigit():
        last = (mir, species)
        #print mir
        mirs.append(mir)
    else:
        last = (mir, species)
        mir = mir[:-1] #remove alphabetic subfamily suffix
        #print mir
        mirs.append(mir)

print "miRNA families:", len(set(mirs))
counts = collections.Counter(mirs)
for item in counts:
    print item, counts[item]
#for mir in mirs:


