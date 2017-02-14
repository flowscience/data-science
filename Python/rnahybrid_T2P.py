#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     07/04/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

import sys

if __name__ == '__main__':
    main()

file_in = open("C:/rnaseq/mir_targets/rnahybrid/targets_f2-7_e22_tsv.txt", "r")

for line in file_in:
    #print line
    mir = line[line.find("cin"):].split("\t")[0]
    if "\t" in mir:
        mir = mir.split("\t")[:-1]
    #if mir.split(" ")[-1].isdigit():
     #   mir = mir[:-3]
    #print mir
    mrna = line[line.find("ENSCINT"):].split("\t")[0].replace("T", "P")
    #mrna = line.split("\t")[1].replace("T", "P")
   #print mrna
    print mrna, "\t", "\t".join(line[line.find("ENSCINT"):].split("\t")[1:])
    #sys.stdout.write(mir + "\t" + mrna)
file_in.close