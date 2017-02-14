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


#This script filters a data files by id's listed one per line in multiple other files
files = glob.glob("C:/RNAseq/mir_targets/de_mirs/*pairs3.txt")
ids = glob.glob("C:/rnaseq/polya_data/clusters/*_DE_fdr05_redo_ids.txt")

#data = open("C:/RNAseq/mir_targets/de_mirs/", "r")

for f in files:
    f_in = open(f)
    filename = f.split("\\")[-1]
    file_out = open('C:/RNAseq/mir_targets/de_mirs/%s_DE_genes.txt' %filename, 'a')
    idlist1 = []
    for line in f_in: #populate id list for each file
        idlist1.append(line.split('\t')[0].split('\n')[0])
    f_in.close
    #file_out.write(data.readline()) #copy header row
    count = 0
    idlist2 = []
    for g in ids:
        data = open(g)
        for line in data: #read through data file for each idlist
            #print line
            name = str(line.split('\t')[0].split('\n')[0])
            #print name
            if name in idlist1:
                #if name in idlist2:
                #   pass
            #else:
                idlist2.append(name)
                idlist1.remove(name)
            #print line
                file_out.write(line)
                count+=1
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

