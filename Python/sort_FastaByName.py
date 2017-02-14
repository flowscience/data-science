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
#Parse the ids, sort and print records based on sorted list
ids = sorted((rec.id) for rec in SeqIO.parse("C:/rnaseq/ref/Ci_miRbase_mature.txt","fasta"))
record_index = SeqIO.index("C:/rnaseq/ref/Ci_miRbase_mature.txt", "fasta")
records = (record_index[id] for id in ids)
SeqIO.write(records, "sorted.fasta", "fasta")