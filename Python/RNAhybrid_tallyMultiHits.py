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

# THIS FILE REQUIRES RNAhybrid multihits.py OUTPUT SORTED BY GENE ID


targets = open("C:/RNAseq/mir_targets/targetscan/6bp+_ams_mirdeep_Ci_multihits.txt", "r")

mRNA = str(targets.readline().split()[0])
#print mRNA
count = 0
unique = 1
total = 1

for line in targets:
    #print int(line.split()[2])
    if mRNA == str(line.split()[1]): #check if miR is same as current (previous line)
        count = count + int(line.split()[2])  # increment hit count if mRNA already in cluster
    else:
            print mRNA, count # Hits per mRNA in current cluster
            unique += 1
            total += count
            count = int(line.split()[2]) # reset hit count if mRNA not in current cluster
            mRNA = str(line.split()[1]) # reset current mRNA
print "Unique.Total", unique, total

#print mir, cluster, unique # Last miR in list hits/cluster & unique targets/cluster
