#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     13/12/2013
# Copyright:   (c) Eli 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#This script takes a FASTA file with KH transcript models and
#outputs the longest transcript model for each gene to a new file.


from Bio import SeqIO
handle = open("KHGene2013.fasta", "rU")

i = 0
longest = [handle[0].id]

for record in SeqIO.parse(handle, "fasta") :
    comparator = record.id.split(".")[0:3]
    if comparator[i] != longest[i].split(".")[0:3]:
        if len(record[i]) >= len(record[i+1]):
            longest.append(record)

handle.close()

i, j = 0, 0
genelist = [mylist[0]]                                                          #Add first transcript to gene list
for ID in mylist:                                                               #Loop through transcript accessions
    print i, len(mylist), len(genelist), ID, mylist[i].split(".")[0:3]          #Display running tally of line being evaluated/total transcripts/total genes/current accession & subset being compared
    if mylist[i].split(".")[0:3] != genelist[j].split(".")[0:3]:                #Evaluate whether current transcript is the same gene as most recently added item to gene list
        genelist.append(mylist[i])                                              #If it's different than the one you just added, add this one too.
        j+=1                                                                    #Use most recently added gene in next comparison
    i+=1                                                                        #Move on to next transcript
#print genelist


output_handle = open("genes.fasta", "w")
SeqIO.write(longest, output_handle, "fasta")
output_handle.close()
