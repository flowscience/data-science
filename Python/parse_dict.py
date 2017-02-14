#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     03/12/2015
# Copyright:   (c) Eli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import sys

#This script filters a data file by id's listed one per line in another file


ids = open("C:/users/eli/downloads/mart_export_10.txt", "r")

#Take header from ID file & initialize empty dict
#head_ids = ids.readline().strip("\n")
idlist1 = {}
l=0
n=0
#Make dict of ID's (key) & selected variables/annotations (values)
for line in ids:
    #print line
    name = line.strip('\n').split('\t')[0]
    #name = name.strip('cin-')
    values = line.strip('\n').split('\t')[1]
    #values = '\t'.join(line.strip('\n').split('\t')[1:5])
    if name in idlist1:
        if values in idlist1[name]:
            continue
        else:
            idlist1[name].append(values)
    else:
        idlist1[name] = [values]

ids.close

for entry in idlist1:
    sys.stdout.write(entry + '\t' + ', '.join(idlist1[entry][:]) + '\n')