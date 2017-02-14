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

f_in = open("C:/users/eli/downloads/Galaxy121-[Fetch_closest_non-overlapping_feature_on_data_98_and_data_120_either].bed")

#f_in.readline()

#Print header
sys.stdout.write("motif" +'\t'+ "target" +'\t'+ "chrom" +'\t'+ "mstart" +'\t'+ "mstop" +'\t'+ "gstart" +'\t'+ "gstop" +'\n')

for line in f_in:
    chrom = line.split('\t')[0]
    mstart = line.split('\t')[1]
    mstop = line.split('\t')[2]
    motif = line.split('\t')[3]
    gstart = line.split('\t')[7]
    gstop = line.split('\t')[8]

    target = line.split(';')[1].split(' ')[2]

    sys.stdout.write('\t'.join([motif, target, chrom, mstart, mstop, gstart, gstop]) +'\n')
