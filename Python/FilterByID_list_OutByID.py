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

ids = open("C:/rnaseq/mirna_data/clusters/1cpm3_10rep_intercept_DE_cpm_ids.txt", "r")
idlist1 = []
for line in ids:
    #print line
    idlist1.append(line.split('\t')[0].split('\n')[0])
ids.close
#print 'idlist1:', len(idlist1)
#sorted(idlist1)
#print idlist1

data = open("C:/rnaseq/mir_targets/rnah_ts_accessfilter_nr_pairs3.txt", "r")
#sys.stdout.write(data.readline()) #copy header row
count = 0
idlist2 = {}

for line in data:
    #print line
    name = line.split('\t')[1].split('\n')[0]
    #idlist2[name] = line.split('\t')[1]
    #print 'name:', name
    #descr = line.split('\t')[2].split('\n')[0]
    #if "," in descr:
    #    descr = descr.split(',')[0]
    #name = line[1:20]
    #kh = '.'.join(line.split('\t')[1].split(':')[1].split('.')[0:4])
    #print name
    if name in idlist1:
        file_out = open('C:/RNAseq/mir_targets/de_mirs/%s_rnah_ts_accessfilter_nr_pairs3.txt' %name, 'a')
        file_out.write(line)
        #if 'Uncharacterized' in descr or 'UNKNOWN' in descr:
        #    descr = idlist1[name]
        #sys.stdout.write(line)
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
        count+=1
#print count
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

