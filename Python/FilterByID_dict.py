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


ids = open("C:/rnaseq/apps/targetscan/targetscan_60/CimiRs_enscinT18bp+_all_redo_fixedIDs.txt", "r")

#Take header from ID file & initialize empty dict
#head_ids = ids.readline().strip("\n")
idlist1 = {}
l=0
n=0
#Make dict of ID's (key) & selected variables/annotations (values)
for line in ids:
    #print line
    name = line.strip('\n').split('\t')[1]
    #name = name.strip('cin-')
    values = line.strip('\n').split('\t')[0]
    #values = '\t'.join(line.strip('\n').split('\t')[1:5])
    if name in idlist1:
        if values in idlist1[name]:
            continue
        else:
            idlist1[name].append(values)
    else:
        idlist1[name] = [values]

ids.close

#Debugging code below:
#print 'idlist1:', len(idlist1)
#sorted(idlist1)
#print idlist1
#len_in = len(idlist1)
#print l, n

data = open("C:/rnaseq/coexpression/mirna-mrna/logfc_pearson/1cpm3_5rpkm3_edger_logfcValues_pearson_redo3.txt", "r")

#Output merged header & initialize retrieved list + row counter
#sys.stdout.write('\t'.join(head_ids.split('\t')[1:3]) + '\t' + data.readline())
#sys.stdout.write("JGI" + '\t' + data.readline())
lines = 0
count = 0
idlist2 = []

#Match ID's between lists and return associated variables
for line in data:
    lines+=1
    name = line.strip('\n').split('\t')[0].strip('"')
    if "cin-" in name:
        name = name.replace("cin-", "")
    #    name2 = name[0:-1]
    #else:
    #    name2 = name
    #print name2
    #name = name[-5:]
    #idlist2[name] = line.split('\t')[1]
    descr = line.strip('\n').split('\t')[1]
    #if "," in descr:
    #    descr = descr.split(',')[0]
    #name = line[1:20]
    #kh = '.'.join(line.split('\t')[1].split(':')[1].split('.')[0:4])

    #Loop through input dict keys (IDs) and search for "name" in associated variables
    if name in idlist1:
            #new = idlist1[name][0]
        if descr in idlist1[name]:
            sys.stdout.write(line)
            #idlist2.append(name)
        #sys.stdout.write('\t'.join(idlist1[name]) + "\t" + name + '\t' + '\t'.join(line.split('\t')[2:]))
        #sys.stdout.write('\t'.join(idlist1[name]) + '\t' + '\t'.join(line.split('\t')[1:]))
            #sys.stdout.write('\t'.join(idlist1[name]) + '\t' + line)
        #print lines
    #else:
    #    sys.stdout.write("N/A" + '\t' + line)
        #sys.stdout.write('\t'.join(idlist1[name2]) + "\t" + name + '\t' + '\t'.join(line.split('\t')[2:]))
    #    sys.stdout.write('\t'.join(idlist1[name]) + '\t' + '\t'.join(line.split('\t')[1:]))
        #sys.stdout.write(name + '\t' + '\t'.join(line.split('\t')[1:]))
        #sys.stdout.write(idlist1[name] + "\t" + line.split('\t')[1:])

    #Loop through input dict keys (IDs) and search for "name" in associated variables
        #for item in idlist1[name]: #Loop through keys (refseq)
        #    if item in name: #Check for each ID in the name variable
        #        sys.stdout.write("".join(idlist1[item]) + "\t" + item + "\t" + line)
        #    elif desc in idlist1[item]:
        #        sys.stdout.write("".join(idlist1[item]) + "\t" + item + "\t" + line)


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
        #    pass
        #else:
        #    idlist2.append(name)
        #    idlist1.remove(name)
            #print line
        #count+=1

#print "Matched:", count, "IDs out of", len_in, "sources and", lines, "targets"
#print "Source %:", float(count)/float(len_in)
#print "Target %:", float(count)/float(lines)

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
#print len(idlist1)
#print len(idlist2)
#idlist4 = [x for x in idlist1 if x not in idlist2]
#for item in idlist4:
#    print item

