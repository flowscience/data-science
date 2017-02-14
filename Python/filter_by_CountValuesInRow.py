#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     19/12/2013
# Copyright:   (c) Eli 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#This script copies each line into a temporary list, then evaluates each item in
# the list for a given criteria (e.g. >=1). The you can choose whether to print
# the line according to how many items in the line meet the specified criteria.


import sys
import glob
import os
#os.chdir("C:/rnaseq/polyA_data/counts")

file_in = open("C:/rnaseq/polya_data/rpkm/rpkm_strand_ens_rpkm.txt")
#print files

i=1
sys.stdout.write(file_in.readline()) #copy header row
for line in file_in:
    line_list = line.strip('\n').split('\t')[1:]
    #print line_list
    count = 0
    for item in line_list:
        if float(item) >= 1:
            count+=1
    if count >= 3:
        sys.stdout.write(line)
    #next(file_in)
    #print line.split('\t')[16]
    #name = file_in.split("\\")[-1]
    #print name
    #f = open(file_in)
    #file_out = open('C:/RNAseq/polyA_data/rpkm/%s.txt' %name, 'a')
    #transcripts = 0
    #for line in f:
    #a = float(line.split('\t')[4])
    #b = float(line.split('\t')[8])
    #c = float(line.split('\t')[12])
    #d = float(line.split('\t')[16])
    #print a,b,c,d
    #if line.split('\t')[4] < 1.0 and line.split('\t')[8] < 1.0 and line.split('\t')[12] < 1.0 and line.split('\t')[16] < 1.0:
    #if a>1 or b>1 or c>1 or d>1:
    #        pass
    #else:
            #file_out.write(line)
            #print line
            #sys.stdout.write(line)
            #transcripts+=1
    i+=1

file_in.close()
    #file_out.close()
    #print f, "Transcripts:", transcripts
    #i+=1


def main():
    pass

if __name__ == '__main__':
    main()


