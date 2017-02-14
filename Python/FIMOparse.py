#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     12/04/2015
# Copyright:   (c) Eli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


import sys

f_in = open("C:/users/eli/desktop/ciona_tfs/fimo_p05e-6.txt")

#Skip file header line
f_in.readline()

#BED Format header
sys.stdout.write('chrom' +'\t'+ 'start' +'\t'+ 'stop' +'\t'+ 'motif' +'\t'+ 'score' +'\t'+ 'strand' +'\t'+ 'CNE' +'\n')

for line in f_in:
    motif = line.split('\t')[0]
    seq = line.split('\t')[1]
    start = int(line.split('\t')[2])
    stop = int(line.split('\t')[3])
    strand = line.split('\t')[4]
    score = line.split('\t')[5]
    pvalue = line.split('\t')[6]
    qvalue = line.split('\t')[7]
    matched = line.split('\t')[8]
    #sequence = line.strip("\n").split('\t')[9]

    #Extract exact genomic position from relative start/stop
    if "chr" in seq:
        chrom = seq.split("_")[1]
        chrom = chrom[0:3] + "_" + chrom[3:]
        c_start = int(seq.split("_")[2])
    elif "scaffold" in seq:
        chrom = "_".join(seq.split("_")[1:3])
        c_start = int(seq.split("_")[3])
    start = c_start+start
    stop = c_start+stop

    #BED format output
    output = '\t'.join([chrom, str(start), str(stop), motif, score, strand, seq])
    sys.stdout.write(output + '\n')