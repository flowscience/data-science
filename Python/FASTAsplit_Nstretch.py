#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     09/04/2015
# Copyright:   (c) Eli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#This script takes a fasta file containing 1 or more records as input.
#It searches for a repeat motif, then splits records into as many new sequences
#   necessary to remove all occurences of the motif.
#Sequence positions can be maintained if record headers are properly formatted.

###########################################################################

#Load dependencies
import sys

#Read input sequence(s) in FASTA format
f_in = open("C:/users/eli/desktop/fasta_test.txt")

#Set repeat motif to search for, split on & exclude
motif = 'N'*8

#Loop through records
seq = []
for line in f_in:

    #New record (header parsing at bottom of script)
    if ">" in line:

        #Concatenate list into string
        seq = "".join(seq)

        #Handle empty records & skip analysis for first sequence until it's parsed
        #Continue only as long as sequence contains motif
        while len(seq) > 0 and motif in seq:

            #Remove stretches of N's from exterior (regardless of motif)
            trim_l = seq.lstrip("N")
            trim_r = seq.rstrip("N")
            trim = seq.strip("N")

            #Calculate start/end positions of trimmed input sequence
            n = len(seq)
            l = len(seq)-len(trim_l)
            r = len(seq)-len(trim_r)
            trim_start = n + l
            trim_end = n + len(trim_r)

            #Check for motif in trimmed sequence
            count = 0
            if motif in trim:
                NL = seq.find(motif)
                NR = seq.rfind(motif)

                #Extract & output sequence before first occurence of motif
                if NL != -1:
                    before = seq[0:NL]
                    before_start = trim_start
                    before_end = trim_start + len(before)
                    print chrom, before_start, before_end, strand
                    print before
                else:
                    NL = trim_start

                #Extract & output sequence after last occurence of motif
                if NR != -1:
                    after = seq[NR+len(motif):]
                    after_start = trim_end-len(after)
                    after_end = trim_end
                    print chrom, after_start, after_end, strand
                    print after
                else:
                    NR = trim_end

            #Extract middle of sequence
            middle = seq[NL:NR+len(motif)]
            middle_start = trim_start + len(before)
            middle_end = trim_end - len(after)

            #Output middle of sequence if it does not contain motif
            if motif not in seq:
                print chrom, middle_start, middle_end, strand
                print middle

            #Reset value of seq to the part that still may contain the motif
            seq = middle
            print seq

        #Parse header information
        seq = []
        head = line.strip('\n')[1:]

        chrom = head.split("_")[1]
        start = head.split("_")[2]
        end = head.split("_")[3]
        strand = head.split("_")[4].split(" ")[0]

    #Parse sequence lines into list for all non-empty non-header lines
    else:
        if len(line) > 0:
            seq.append(line.strip('\n'))

        #with open("C:/users/eli/desktop/intestinalis_conserved_all_GFF.txt", "a") as f_out:
        #    f_out.write(seqname +'\t'+ start +'\t'+ end +'\t'+ strand +'\n')
f_in.close
#f_out.close