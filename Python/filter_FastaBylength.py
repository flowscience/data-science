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

i = 0

sequences = [] # Setup an empty list
output_handle = open("enscsavP_3utr_6bp+.fasta", "w")
for record in SeqIO.parse(open("C:/rnaseq/ref/ENSCsavP_3utr.txt", "rU"), "fasta"):
    i += 1
    if len(record.seq) > 5 and "Sequence" not in record.seq:
        # Add this record to our list
        sequences.append(record)
        SeqIO.write(record, output_handle, "fasta")

print "Input sequences:", i
print "Found %i sequences over 5bp" % len(sequences)

output_handle.close()

