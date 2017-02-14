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
ids = open("C:/users/eli/desktop/otx_targets/heidi_otx_targets_clone.txt", "r")
idlist1 = []
for line in ids:
     idlist1.append(line.split('\t')[0].split('\n')[1])

files = glob.glob("C:/users/eli/desktop/otx_targets/limma_lfc/*percentile..txt")

for f in files:
    f_in = open(f)
    filename = f.split("\\")[-1]
    file_out = open('C:/RNAseq/mir_targets/de_mirs/%s_JGI.txt' %filename, 'a')
    idlist2 = []

    file_out.write(data.readline()) #copy header row
    for line in f_in:
        name = line.strip('\n').split('\t')[0].strip('"')
        #name = name.split('|')[3].split('.')[0] # for first ID from BLAST target
        variables = line.strip('\n').split('\t')[2:]
        #idlist2[name] = line.split('\t')[1]
        descr = line.strip('\n').split('\t')[1]


    f_in.close


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

