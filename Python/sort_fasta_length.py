#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     09/03/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

from Bio import SeqIO

handle = open("ref/Ci_mirbase_mature.txt", "rU")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()
records.sort(cmp=lambda x,y: cmp(len(x), len(y)))
#records.sort(cmp=reverse=True)
out_handle = open("sorted.fasta", "w")
SeqIO.write(records, out_handle, "fasta")
out_handle.close()