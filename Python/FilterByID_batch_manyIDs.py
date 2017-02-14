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
import glob


#This script filters multiple data files by id's listed one per line in another file
ids = glob.glob("C:/RNAseq/mir_targets/de_mirs/*_DE_genes.txt")

#Populate id list with id's from all id files
idlist1 = []
for f in ids:
    f_in = open(f)
    for line in f_in:
        protein = line.split('\t')[0].split('\n')[0]
        transcript = str(protein).replace("P", "T")
        idlist1.append(transcript)
    f_in.close()

#print idlist1
for item in idlist1:
    print item
    #sys.stdout.write(item)

data = open("C:/rnaseq/polya_data/rpkm/rpkm_strand_ens_rpkm+5.txt", "r")
idlist2 = []
count=0
for line in data:
    name = line.split('\t')[0].split('\n')[0]
    idlist2.append(name + "\n")
    if name in idlist1:
        #sys.stdout.write(line)
        #file_out.write(data.readline()) #copy header row
        count += 1
data.close()

#idlist3 = []
#for item in idlist1:
#        if item in idlist2:
                #if name in idlist2:
                #   pass
            #else:
                #idlist3.append(name)
                #idlist2.remove(name)
            #print line
#                file_out.write(item + '\n')
#                count+=1
        #else:
        #    pass
    #print len(idlist1)
    #print len(idlist2)
    #print idlist2
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

