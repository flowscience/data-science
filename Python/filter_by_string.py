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

# This script takes a file of ID's and converts them into a list.
# Next, it uses values in the first column of a target file to search the ID list.
# Finally, lines in the target file with matched ID's can be split or printed whole.

import sys

##########################################

#Read ID file
#ids = open("C:/users/eli/desktop/otx_targets/late_logFCpred_JGI.txt")

#Initialize and populate ID list
id_list = []
#for line in ids:
#    id_list.append(line.strip('\n').split('\t')[0])
#ids.close

#Check structure of ID list
#print len(id_list)
#print id_list

##########################################

#Read in target file and intialize empty list for matched IDs
target = open("C:/rnaseq/coexpression/mirna-mrna/logfc_pearson/1cpm3_5rpkm3_edger_logfcValues_pearson_redo3_targetscan.txt")
id_list2 = []

#Return header row of target file
#sys.stdout.write(target.readline())

id_list = ["CDS", "stop_codon"]

# Scan target file
for line in target:
    #print float(line.split("\t")[2])
    #Extract ID from target file
    #name = line.strip('\n').split('\t')[2]
    #print name
    if float(line.split("\t")[2]) < -0.85:
        sys.stdout.write(line)
    #Search ID list for "name" in the current line
    #if name in id_list:
            #id_list.remove(name) #Return only the first occurence of the ID
            #id_list2.append(name) #Keep track of ID's that were found
    #        sys.stdout.write(line) #Return the current line
target.close()



# Optional block to output ID's in list not found in target file
#for item in id_list:
#    print item




def main():
    pass

if __name__ == '__main__':
    main()


