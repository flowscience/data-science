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

ids = open("C:/Users/Eli/Desktop/Smith_Lab/data_downloads/ANISEED/KH_gene_name.txt", "r")
for line in ids:
    iden = line.split('\t')[0]
    #print iden
    name = '.'.join(line.split('\t')[1].split('.')[0:3])
    #print name
    sys.stdout.write(iden + '\t' + name + '\n')
##for line in ids:
##    wiki = line.split('\t')[2]
##    enscint = line.split('\t')[3]
##    uniprot = line.split('\t')[4]
##    rfam = line.split('\t')[5].split('\n')[0]
##    if len(wiki) > 0:
##        if wiki[0:3] != 'LOC' and wiki[0:4] != 'CIN.':
##            sys.stdout.write('\t'.join(line.split('\t')[0:3]) + '\n')
##    elif len(enscint) > 0:
##        if enscint[0:4] != 'CIN.':
##            sys.stdout.write('\t'.join(line.split('\t')[0:2]) + '\t' + line.split('\t')[3] + '\n')
##    elif len(uniprot) > 0:
##        if uniprot[0:4] != 'CIN.' and uniprot[0:3] != 'LOC':
##            sys.stdout.write('\t'.join(line.split('\t')[0:2]) + '\t' + line.split('\t')[4] + '\n')
##    elif len(rfam) > 0:
##        sys.stdout.write('\t'.join(line.split('\t')[0:2]) + '\t' + line.split('\t')[4] + '\n')
##    else:
##        sys.stdout.write('\t'.join(line.split('\t')[0:2]) + '\n')