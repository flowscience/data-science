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

ids = open("C:/rnaseq/mirna_data/clusters/10rep_redo2/1cpm3redo_edgeR_deseq_p05_logFC.txt", "r")

idlist1 = []
for line in ids:
    #print line
    name = line.strip('\n').split('\t')[0]
    #name = name[:19]
    idlist1.append(name)
ids.close
#print 'idlist1:', len(idlist1)
#sorted(idlist1)
#print idlist1

#data = open("C:/rnaseq/coexpression/mirna-mrna/logfc_pearson/deseq2_logfc_1cpm3_5rpkm3_redo_pearson-070_targetscan.txt", "r")
data = open("C:/rnaseq/mirna_data/clusters/10rep_redo2/1cpm3redo_edgeR_deseq2_logFC_vals_redo.txt", "r")

#sys.stdout.write(data.readline()) #copy header row
count = 0
idlist2 = []

for line in data:
    #print line
    name = line.strip('\n').split('\t')[0]
    #name2 = "ENSCINT" + name[7:]
    #print name
    #name2 = str(name[4:])
    #print name
    #idlist2[name] = line.split('\t')[1]
    #print 'name:', name
    descr = line.split('\t')[1].strip('\n')
    #if "," in descr:
    #    descr = descr.split(',')[0]
    #name = line[1:20]
    #kh = '.'.join(line.split('\t')[1].split(':')[1].split('.')[0:4])
    #print name
    if name in idlist1:
        #if 'Uncharacterized' in descr or 'UNKNOWN' in descr:
        #    descr = idlist1[name]
        sys.stdout.write(line)
        #idlist1.remove(name)
        #idlist1[name]
    #else:
    #    pass
    #    sys.stdout.write(name + '\t' + line.split('\t')[1][1:8].upper() + '\t' + '7719' + '\n')
        #if name in idlist2:
         #   pass
        #else:
        #idlist2.append(name)
        #idlist1.remove(name)
            #print line
        count+=1
#print count
#for item in idlist1:
#    print item
    #sys.stdout.write(item + '\t' + idlist2[item] + '\t' + idlist1[item] + '\n')
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
#        print item


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

