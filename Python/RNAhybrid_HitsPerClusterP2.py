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

# THIS FILE REQUIRES TSV format RNAhybrid OUTPUT SORTED BY MICRORNA THEN GENE ID


targets = open("C:/RNAseq/mir_targets/rnahybrid/targets_6bp_e20p01_k3-1.srt.txt", "r")

first = targets.readline()
mRNA = first[first.find("ENSCINP"):].split("\t")[0]
mir = first[first.find("cin"):].split("\t")[0]
cluster = 1
count = 1
unique = 1

for line in targets:
    if mir == line[line.find("cin"):].split("\t")[0]: #check if miR is same as current (previous line)
        cluster += 1 # increment cluster size for each mRNA in cluster
        if mRNA == line[line.find("ENSCINP"):].split("\t")[0]: #check if mRNA is same as current (previous line)
            count += 1  # increment hit count if mRNA already in cluster
        else:
            #print mir, mRNA, count # Hits per mRNA in current cluster
            count = 1 # reset hit count if mRNA not in current cluster
            unique += 1
            mRNA = line[line.find("ENSCINP"):].split("\t")[0] # reset current mRNA
    else:
        #print mir, mRNA, count # Final mRNA in a cluster, hits
        print mir, cluster, unique # miR hits/cluster & unique targets/cluster
        mRNA = line[line.find("ENSCINP"):].split("\t")[0] # reset current mRNA for new cluster
        mir = line[line.find("cin"):].split("\t")[0] # reset current miR for new cluster
        cluster = 1 # reset cluster size
        unique = 1
print mir, cluster, unique # Last miR in list hits/cluster & unique targets/cluster
