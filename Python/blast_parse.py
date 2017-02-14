#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     22/01/2015
# Copyright:   (c) Eli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import sys

#This script filters a data file by id's listed one per line in another file

blast = open("C:/users/eli/desktop/smith_lab/geo_data/life_cycle/data/enscinGT_refseq_mRNA_ncRNA_protein.txt", "r")
idlist1 = {}
for line in ids:
    last = ""
    query =
    subject =
    #print line
    idlist1[line.strip('\n').split('\t')[1]] = list(line.strip('\n').split('\t'))
ids.close
#print 'idlist1:', len(idlist1)
#sorted(idlist1)
#print idlist1

data = open("C:/users/eli/desktop/smith_lab/geo_data/life_cycle/data/enscinGT_emblGenbank_refseqmRNA.txt", "r")
sys.stdout.write(data.readline()) #copy header row
count = 0
idlist2 = {}

for line in data:
    #print line
    name = line.strip('\n').split('\t')[1].strip('"')
    idlist2[name] = line.split('\t')[1]
    #print 'name:', name
    descr = line.strip('\n').split('\t')[3]
    #if "," in descr:
    #    descr = descr.split(',')[0]
    #name = line[1:20]
    #kh = '.'.join(line.split('\t')[1].split(':')[1].split('.')[0:4])
    #print name
    if name in idlist1:
        if 'Uncharacterized' in descr or 'UNKNOWN' in descr:
            descr = idlist1[name]
        sys.stdout.write('\t'.join(idlist1[name]) + '\t' + '\t'.join(line.split('\t')[2:]))
        #sys.stdout.write('\t'.join(line.split('\t')[0:2]) + '\t' + descr + '\n')
        #del idlist1[name]
    else:
        pass
        #sys.stdout.write(line + '\n')
        #if name in idlist2:
         #   pass
        #else:
            #idlist2.append(name)
            #idlist1.remove(name)
            #print line
        count+=1

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

