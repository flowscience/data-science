#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     13/02/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     13/02/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

from Bio import SeqIO

#sequence_in = SeqIO.to_dict(SeqIO.parse(open("ref/ENSCINP_3utr_18bp+.fasta", "rU"), "fasta"))
sequence_in = list(SeqIO.parse(open("C:/rnaseq/ref/ENScinP_3utr_6bp+.fasta", "rU"), "fasta"))
temp_ids = open("C:/rnaseq/enscinPenscsavP6bp+_matchedIDs.txt", "rU")
ids = list([line[:-1] for line in temp_ids])

print "Seq in:", len(sequence_in)
print "ids:", len(ids)

#sequence_out = {k:v for k,v in sequence_in.items() if (k in ids)}
sequence_out = []
for record in sequence_in:
    for item in ids:
        for i in item:
            if i == record.id:
                sequence_out.append(record)

print "Found %i sequences with matched id's" % len(sequence_out)
#print sequence_out

output_handle = open("C:/rnaseq/ref/ENScinP_3utr6bp+_matched2.fasta", "w")
SeqIO.write(sequence_out, output_handle, "fasta")
output_handle.close()




