#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     06/04/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import sys

#This script filters a data file by id's listed one per line in another file

ids = open("C:/rnaseq/ref/ci_mirs_sorted_len.txt", "r")
idlist1 = []
for line in ids:
    name = line.split('\t')[0]
    if name in idlist1:
        sys.stdout.write(name)
    else:
        idlist1.append(name)
