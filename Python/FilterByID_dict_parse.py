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

ids = open("C:/rnaseq/mirna_data/clusters/10rep_redo_deseq-edger/DEseq2_1cpm3redo_nopara2_logFCall.txt", "r")

#Take header from ID file & initialize empty dict
head_ids = ids.readline().strip("\n")
idlist1 = {}
#id_count = 0
#Make dict of ID's (key) & selected variables/annotations (values)
for line in ids:
    name = line.strip('\n').split('\t')[0]
    #name = name[4:]
    #if len(name.split('-')) > 3:
    #    name = '-'.join(name.split('-')[1:])
        #arm = name.split('-')[-1]
        #name = '-'.join(['-'.join(name.split('-')[0:2]), arm])
    name = name.strip('cin-')
    #print name
    #name = name[-5:]
    #values = '\t'.join(line.strip('\n').split('\t')[1:3])
    values = '\t'.join(line.strip('\n').split('\t')[1:4])
    #if "ENSCINP" in values:
    #    values2 = values[7:]
    #    values = "ENSCINT" + values2
    #values = '\t'.join(line.strip('\n').split('\t')[2:])
    #values = values[0:-3]
    if name in idlist1 and len(name) > 0:
        if values in idlist1[name]:
            continue
        else:
            idlist1[name].append(values)
    elif len(name) > 0:
        idlist1[name] = [values]
    #id_count+=1
    #if id_count%1000==0:
    #    print id_count

ids.close

#Debugging code below:
#print 'idlist1:', len(idlist1)
#sorted(idlist1)
#print idlist1
idlist1 = ['miR-216']

data = open("C:/rnaseq/coexpression/mirna-mrna/logfc_pearson/1cpm3_5rpkm3_redo2_edger_logfcValues_pearson_targetscan_deseq2logfc_mirs2.txt", "r")

#Output merged header & initialize retrieved list + row counter
#sys.stdout.write("LogFC.consensus" + '\t' + data.readline())
#sys.stdout.write("LogFC.consensus" + '\t' + '\t'.join(data.readline().split('\t')[0:3]) + '\n')
#sys.stdout.write(data.readline())
#data.readline()
matched = 0
idlist2 = {}
out = 0

#Match ID's between lists and return associated variables
for line in data:
    #print line
    name = line.strip('\n').split('\t')[6]
    #print name
    #name = name.split('|')[3].split('.')[0] # for first ID from BLAST target
    #name = name[0:7]
    #if name[-1].isalpha():
    #    name = name[0:-1]
    #print name
    #variables = line.strip('\n').split('\t')[5,9,10]
    #idlist2[name] = line.split('\t')[1]
    descr = line.strip('\n').split('\t')[1]
    #if "," in descr:
    #    descr = descr.split(',')[0]
    #name = line[1:20] # for trimmed encin gene name
    #kh = '.'.join(line.split('\t')[1].split(':')[1].split('.')[0:4])

    #Loop through input dict ID's and search for "name" in associated variables
    #for item in idlist1: #Loop through keys (refseq)
    if name in idlist1: #match primary ID's
        #for item in idlist1[name].split(' '):
            sys.stdout.write('\t'.join(idlist1[0]) + '\t' + line)
                #EXCHANGE ID'S BUT KEEP REST OF LINE/DESCRIPTION
    #            sys.stdout.write(descr + '\t' + '\t'.join(idlist1[name]) + '\n')
    #else:
    #    sys.stdout.write(descr + '\t' + name + '\n')
                #print idlist1[name]
                #sys.stdout.write(line.strip('\n') + '\t' + '\t'.join(idlist1[name]) + '\n')
                #continue
                #matched +=1
    else:
        sys.stdout.write(line)
        #if name in idlist1[item]: #Check for each ID in the name variable
        #    idlist2[name] = variables
    #            values = idlist1[item]
    #            stop = 1
                #while stop <= len(values):
     #   if descr in idlist1[name]:
     #       sys.stdout.write(line)
        #    out+=1
#print out
#Return items in matched list (idlist2) using associations from idlist1
#for mir in idlist1:
#    if mir in idlist2:
#        sys.stdout.write(mir + '\t' + '\t'.join(idlist2[mir]) + '\n')
#    for mrna in idlist1[mir]:
#        if mrna in idlist2:
#            sys.stdout.write(mrna+ '\t' + '\t'.join(idlist2[mrna]) + '\n')

                #if len(idlist1[name]) > 1:
                #   for value in idlist1[name]: #Print all values on separate lines
                #        sys.stdout.write(value + '\t' + line)
                        #sys.stdout.write(descr + '\t' + value + '\t' + name + '\t' + '\t'.join(variables) + '\n')
                #        sys.stdout.write(value + '\t' + '\t'.join(line.split('\t')[0:]))
                        #sys.stdout.write(value + '\t' + '\t'.join(line.split('\t')[0:3]) + '\n')
                #        out+=1
                #else:
                #    sys.stdout.write('\t'.join(idlist1[name]) + '\t' + line)
                    #sys.stdout.write(descr + '\t' + ".\t".join(idlist1[name]) + '\t' + name + '\t' + '\t'.join(variables) + '\n')
                    #print idlist1[name]
                #    sys.stdout.write(('\t'.join(idlist1[name]) + '\t' + '\t'.join(line.split('\t')[0:])))
                    #sys.stdout.write(name + '\t' + '\t'.join(idlist1[name]) + '\t' + '\t'.join(line.split('\t')[2:]))
                #    out+=1

#print matched, out
                        #print gene
                        #print idlist1[item]
    #                    sys.stdout.write(value + "\t" + name + '\t' + line)#'\t' + '\t'.join(line.split('\t')[2:]))
    #                    stop+=1
                        #continue

    #if name in idlist1:
    #    if descr in idlist1[name]:
    #        sys.stdout.write(line)
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
        #count+=1

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