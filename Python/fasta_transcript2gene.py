#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     18/12/2013
# Copyright:   (c) Eli 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

from Bio import SeqIO
transcripts = list(SeqIO.parse(open('testtranscripts.fasta', 'rU'), "fasta"))
genes = open("testgenes.fasta", "w")

def get_longest(isoforms):
#        tempisos = open("tempisos.fasta", "w")
#        SeqIO.write(isoforms, tempisos, "fasta")
#        isoforms = SeqIO.parse(open("tempisos.fasta", "rU"), "fasta")
    lengths = []
    for record in isoforms:
        print "isoform:" record.id
        lengths.append(len(record.seq))
    print lengths
    most_bases = max(lengths)
    print most_bases
    for record in isoforms:
        if len(record.seq) == most_bases:
            SeqIO.write(record + '\n', genes, "fasta")

genes.close()


i, j = 0, 0
isoforms = []
for record in transcripts:
    print record.id, len(record.seq), i, j
    if transcripts[i] not in isoforms:                #Ensure first isoform for any gene is added to list
        isoforms.append(transcripts[i])
        i+=1
    if i < len(transcripts) and transcripts[i] != isoforms[j] and transcripts[i].id.split(".")[0:3] == isoforms[j].id.split(".")[0:3]:     #If current transcript is isoform of most recently added to list, add current transcript to list
        isoforms.append(transcripts[i])
        i+=1
        j+=1
    else:                                                                       #If current transcript is not isoform of most recently added to list.
        get_longest(isoforms)
        isoforms = []
        j = 0




