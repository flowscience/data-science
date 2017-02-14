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
import math

#This script filters a data file by id's listed one per line in another file


ids = open("C:/users/eli/desktop/smith_lab/geo_data/life_cycle/data/gpl4556_blast_parse_enscinT_redo_noDupPairs.txt", "r")

#Read in header from ID file & initialize empty dict
head_ids = ids.readline().strip("\n")
idlist1 = {}

#Make dict of ID's (key) & selected variables/annotations (values)
for line in ids:
    name = line.strip('\n').split('\t')[1]
    #name = name.split('|')[3].split('.')[0] # for first ID from BLAST target
    values = line.strip('\n').split('\t')[0]
    if name in idlist1:
        if values not in idlist1[name]:
            idlist1[name].append(str(values))
    else:
        idlist1[name] = [values]

ids.close

#print sum(len(x for x in idlist1))/len(x for x in idlist1)

#Debugging code below:
print 'idlist1:', len(idlist1)
#sorted(idlist1)
#print idlist1

data = open("C:/users/eli/desktop/smith_lab/geo_data/life_cycle/data/gse6308_slimdata.txt", "r")

#Output merged header & initialize retrieved list + row counter
#sys.stdout.write('\t'.join(head_ids.split('\t')[2:5]) + '\t' + data.readline())
sys.stdout.write(data.readline()) #Output data header only
count = 0
found = 0
idlist2 = {}

#Match ID's between lists and return associated variables
for line in data:
    count+=1
    #print count
    name = line.strip('\n').split('\t')[0].strip('"')
    #name = name.split('|')[3].split('.')[0] # for first ID from BLAST target
    #idlist2[name] = line.split('\t')[1]
    descr = line.strip('\n').split('\t')[0]
    #if "," in descr:
    #    descr = descr.split(',')[0]
    #name = line[1:20]
    #kh = '.'.join(line.split('\t')[1].split(':')[1].split('.')[0:4])

    #FAST VERSION: Use to search dictionary keys (ID's)
    if name in idlist1:
        found+=1
        #sys.stdout.write('\t'.join(idlist1[name]) + "\t" + line)
print count
print found

        #Print each value to new line
        #if len(idlist1[name]) > 1:
        #    for item in idlist1[name]:
                #sys.stdout.write(item + "\t" + '\t'.join(line.split('\t')[1:]))
        #else:
            #sys.stdout.write('\t'.join(idlist1[name]) + "\t" + '\t'.join(line.split('\t')[1:]))
    #SLOW VERSION: Loop through keys then search in associated variables
    #for item in idlist1: #Loop through keys (refseq)
     #   if item in line: #Check for each ID in the name variable

            #Print each value to a new line
      #      if len(idlist1[item]) > 1:
      #          #print "Double!"
       #         for value in idlist1[item]:
       #             sys.stdout.write(descr + '\t' + value + '\t' + item + '\n')
        #    else:
        #        sys.stdout.write(descr + '\t' + '\t'.join(idlist1[item]) + item + '\n')
        #    continue
        #elif descr in idlist1[item]:
        #    sys.stdout.write("\t".join(idlist1[item]) + "\t" + item + "\t" + line)
        #    continue

    #if name in idlist1:
    #    if 'Uncharacterized' in descr or 'UNKNOWN' in descr:
    #        descr = idlist1[name]
    #    sys.stdout.write('\t'.join(idlist1[name]) + '\t' + '\t'.join(line.split('\t')[2:]))
        #sys.stdout.write('\t'.join(line.split('\t')[0:2]) + '\t' + descr + '\n')
        #del idlist1[name]
    #else:
    #    pass
        #sys.stdout.write(line + '\n')
        #if name in idlist2:
         #   pass
        #else:
            #idlist2.append(name)
            #idlist1.remove(name)
            #print line
          #      count+=1

#Code for checking remaining values in ID list
#for item in idlist1:
#    print "bakow!"
#    sys.stdout.write(item + '\t' + idlist2[item] + '\t' + idlist1[item] + '\n')
    #else:
     #   print line.split('\t')[0]
#print len(idlist1), len(idlist2)
#print len(idlist1)-len(idlist2)
#print len(idlist1)
#sorted(idlist2)
#print idlist1
#for item in idlist2:
#    if item in idlist1:
#        idlist1.remove(item)
#print 'idlist1-idlist2', len(idlist1)
#for item in idlist1:
#    print item


#cross check input and output lists
#idlist3= []
#for thing in idlist1:
#    if thing in idlist2:
#        pass
#    else:
#        idlist3.append(thing)

#print len(idlist3)
#print len(idlist4)
#idlist4 = [x for x in idlist1 if x not in idlist2]