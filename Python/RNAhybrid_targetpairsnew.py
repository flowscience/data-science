#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Eli
#
# Created:     03/03/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

# THIS FILE REQUIRES TSV format RNAhybrid OUTPUT SORTED BY GENE ID then miRNA ID


targets = open("C:/rnaseq/mir_targets/rnahybrid/targets_f2-7_mfe-22_p0.1_c.txt", "r")

first = targets.readline()
mRNA = first[first.find("ENS"):].split("\t")[0]
mir = first[first.find("miR"):].split("\t")[0]

for line in targets:
    if mRNA == line[line.find("ENS"):].split("\t")[0]: #check if mRNA is same as previous
        if mir == line[line.find("miR"):].split("\t")[0]: #check if miR is same as previous
            pass
        else: #if new miR
            print mRNA, mir # new pair
            mir = line[line.find("miR"):].split("\t")[0] # reset current miR
    else:
        #New Gene: print previous line and restart comparison
        print mRNA, mir # total miR targets/transcript & unique miRs/transcript
        mRNA = line[line.find("ENS"):].split("\t")[0] # reset current mRNA for new cluster
        mir = line[line.find("miR"):].split("\t")[0] # reset current miR for new cluster
print mRNA, mir # Last miR in list hits/cluster & unique targets/cluster
