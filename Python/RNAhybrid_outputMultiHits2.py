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

# THIS FILE REQUIRES RNAhybrid OUTPUT SORTED BY MICRORNA THEN GENE ID


targets = open("C:/RNAseq/mir_targets/rnahybrid/targets_6bp_e20p01_k3-1.srt.txt", "r")

first = targets.readline()
lastmir = first[first.find("cin-"):].split("\t")[0].rstrip("\n")
lastp = first[first.find("ENSCINP"):].split("\t")[0].rstrip("\n")
cluster = 0
multihits = 0
unique = 0
for line in targets:
    mir = line[line.find("cin-"):].split("\t")[0].rstrip("\n") #check if miR is same as previous line
    mRNA =  line[line.find("ENSCINP"):].split("\t")[0].rstrip("\n")
    if mir == lastmir:
        cluster += 1 # increment cluster size for each mRNA in cluster
        if mRNA ==  lastp: #check if mRNA is same as previous line
            multihits += 1  # increment hit count if mRNA already in cluster
        else:
            if multihits > 1: #Print only targets with more than 1 hit
                print "\t".join(line.split()[:]), "\t", multihits # Hits per mRNA in current cluster
                multihits = 1
                unique += 1
                lastp = mRNA
            else: # Reset & increment counters
                multihits = 1
                unique += 1
                lastp = mRNA
    else:
        lastp = mRNA # reset current mRNA for new cluster
        lastmir = mir # reset current miR for new cluster
        cluster = 1 # reset cluster size
        unique = 1
        multihits = 1
#print mir, cluster, unique # Last miR in list hits/cluster & unique targets/cluster
