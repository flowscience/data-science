#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     10/03/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

from Bio import SeqIO
#Index the FASTA files you want to extract matched sequences from
files = ["3utr%i.fasta" % (i) for i in range(2)]
print files
ciona_index = SeqIO.index_db("ciona.idx", files, "fasta")
print ("%i sequences indexed" % len(ciona_index))