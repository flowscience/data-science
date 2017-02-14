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

import glob
from Bio import SeqIO

#Index the FASTA files you want to extract matched sequences from
#files = ["C:/RNAseq/3utr%i.fasta" % (i) for i in range(2)]
#print files
#files = ["C:/RNAseq/3utr0.fasta", "C:/RNAseq/3utr1.fasta"]
#files = [glob.iglob("C:/RNAseq/3utr*.fasta")]
#ciona_index = SeqIO.index_db("ciona.idx", files, "fasta")
ci_index = SeqIO.index("C:/rnaseq/3utr0.fasta", "fasta")
cs_index = SeqIO.index("C:/rnaseq/3utr1.fasta", "fasta")
#print "Sequence files:", files
print ("%i sequences indexed" % (len(ci_index) + len(cs_index)))


#Read through the matched ID file
id_file = open("C:/RNAseq/enscinPenscsavP6bp+_matchedIDs.txt", "rU")
ids = list([line[:-1] for line in id_file])
print "IDs:", len(ids)

#Output matched records from index DB
#Create a new file for each set of matched records (each line of input will output one file)
records = []
for i, line in enumerate(ids):
    sep_ids = line.split()
    #sprint sep_ids
    #if len(sep_ids) == 2:
    if (sep_ids[0] in ci_index) and (sep_ids[1] in cs_index):
        #print sep_ids
        records = [ci_index[sep_ids[0]], cs_index[sep_ids[1]]]
        SeqIO.write(records, "C:/RNAseq/temp/matched_%s.fasta" %sep_ids[0], "fasta")
        #SINGLE FILE OUTPUT records.append(ciona_index[item] for item in sep_ids)
        #Single file output doesn't work, just use BASH function cat on the multiple files
    else:
        pass
#print records
#SINGLE FILE OUTPUT SeqIO.write(records, "C:/RNAseq/temp/mir124-2-5p_targets.fasta", "fasta")

#pipe_handle = StringIO()
#SeqIO.write(records, pipe_handle, "fasta")
#fastas = pipe_handle.getvalue()
#sys.stdout.write(fastas + "\n")

#WARNING: this script has a bug which excludes the final id pair due to a key error
