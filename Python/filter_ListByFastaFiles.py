#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     11/03/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import sys
from Bio import SeqIO

#Filter a matched ID list by the sequences in a multi-fasta database


sequence_in = list(SeqIO.parse(open("C:/RNAseq/ref/enscinp_3utr_6bp+.fasta", "rU"), "fasta"))
#Read through the matched ID file
id_file = open("C:/RNAseq/ref/enscinpids.txt", "rU")
ids = list([line[:-1] for line in id_file])
print "ids:", len(ids)
print "Seq in:", len(sequence_in)

id_out = []
for record in sequence_in:
    for item in ids:
        if record.id in item:
            id_out.append(item)

print "Found %i matched id's in fasta files" % len(id_out)
#print sequence_out

output_handle = open("C:/RNAseq/ref/enscinP6bp+IDs.txt", "w")
output_handle.write("\n".join(item for item in id_out))
output_handle.close()



