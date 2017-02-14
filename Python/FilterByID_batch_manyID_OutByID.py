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
#print ids
data = open("C:/rnaseq/polya_data/rpkm/rpkm_strand_ens_rpkm+5.txt", "r")
count = 0
for f in ids: # Pass through the ID files
    #print f
    idlist1 = []
    f_in = open(f)
    filename = f.split("\\")[-1].split("_")[0]
    for line in f_in: #Populate id list with id's from all id files
        protein = line.split('\t')[0].split('\n')[0]
        transcript = str(protein).replace("P", "T")
        idlist1.append(transcript)
    f_in.close()
    #print idlist1
    idlist2 = []
    data = open("C:/rnaseq/polya_data/rpkm/rpkm_strand_ens_rpkm+5.txt", "r")
    for line in data:
        name = line.split('\t')[0].split('\n')[0]
        file_out = open('C:/RNAseq/mir_targets/de_mirs/%s_DE_genes_rpkm.txt' %filename, 'a')
        idlist2.append(name + "\n")
        if name in idlist1:
            #print filename
            #sys.stdout.write(line)
            file_out.write(line)
            count += 1




#print idlist1
#for item in idlist1:
#    print item
    #sys.stdout.write(item)



#count=0

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

