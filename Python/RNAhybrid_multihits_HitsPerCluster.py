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


targets = open("C:/RNAseq/mir_targets/rnahybrid/targets_6bp_e20p01_multihits.txt", "r")

first = targets.readline()
lastmir = first[first.find("cin-"):].split("\t")[0]
cluster = 0

for line in targets:
    mir = line[line.find("cin-"):].split("\t")[0]
    if mir == lastmir: #check if miR is same as current (previous line)
        cluster += 1 # increment cluster size for each mRNA in cluster
    else:
            print mir, cluster # Hits per mRNA in current cluster
            lastmir = mir
            cluster = 1

print mir, cluster # Last miR in list hits/cluster & unique targets/cluster
