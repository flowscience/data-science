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
import math

total = 0 #Setup a counter for total bases
lengths = [] #Setup empty list to hold lengths
for record in SeqIO.parse(open("C:/RNAseq/3utr1.fasta", "rU"), "fasta") :
    lengths.append(len(record.seq))
    total = total+len(record.seq)      # Add the sequence length to the total
    if len(record.seq) == 0:
            print record
    else:
            pass

count = len(lengths)
average = float(total/count)
print "Total sequence length:", total
print "Total Records:", count
print "Average Length:", average
print "Max, Min:", max(lengths), min(lengths)
#print "Non-Empty Records:", len(non_zeros)

a = []
for l in lengths:
    a.append((l-average)**2)
sd = math.sqrt(sum(a)/len(a))
print "SD:", sd


#output_handle = open("seq_lengths.fasta", "w")
#for item in lengths:
#    output_handle.write(str(lengths[item])+'\n')
#output_handle.close()

#output_handle = open("non_empty.fasta", "w")
#for entry in non_zeros:
#    output_handle.write(str(non_zeros[entry])+'\n')
#output_handle.close()
