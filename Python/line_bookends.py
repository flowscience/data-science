#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     10/04/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

targets = open("C:/RNAseq/mir_targets/rnahybrid/targets_f2-7_e10p01_multihits.txt", "r")

for line in targets:
    print line.split()[0], "\t", line.split()[-1]