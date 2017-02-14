#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     05/04/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

aln = open("C:/rnaseq/temp/6bp+.aln", "r")

count = 0
for line in aln:
    count += 1
    name = line[:19]
    #print name
    if count%6 == 4:
        print name, 7719, line[26:]
        prev = name
        #count += 1
    elif count%6 == 5:
    #elif name[0:7] == "enscsa":
        #count += 1
        print prev, 51511, line[26:]
aln.close