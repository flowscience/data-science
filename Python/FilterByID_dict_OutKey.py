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

#Take header from ID file & initialize empty dict
#head_ids = ids.readline().strip("\n")

idlist1 = {}
#id_count = 0
#Make dict of ID's (key) & selected variables/annotations (values)
for line in ids:
    key = line.strip('\n').split('\t')[0]
    values = line.strip('\n').split('\t')[1]

    if key in idlist1 and len(key) > 0:
        if values in idlist1[key]:
            continue
        else:
            idlist1[key].append(values)
    elif len(key) > 0:
        idlist1[key] = [values]
    #id_count+=1
    #if id_count%1000==0:
    #    print id_count

ids.close

#Debugging code for IDlist:
#print 'idlist1:', len(idlist1)
#sorted(idlist1)
#print idlist1


for key in idlist1:
    for value in idlist1[key]:
