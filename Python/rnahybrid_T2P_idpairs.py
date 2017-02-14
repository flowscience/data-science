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

file_in = open("C:/rnaseq/mir_targets/rnah_ts_accessfilter_pairs.txt", "r")

for line in file_in:
    #print line
    mir = line[line.find("cin-"):].split("\t")[0]
    if "\t" in mir:
        mir = mir.split("\t")[:-1]
    #if mir.split(" ")[-1].isdigit():
     #   mir = mir[:-3]
    #print mir
    mrna = line[line.find("ENSCIN"):].split("\t")[0]
    if "T" in mrna:
        mrna.replace("T", "P")
    #mrna = line.split("\t")[1].replace("T", "P")
   #print mrna
    print mir , "\t", mrna
    #sys.stdout.write(mir + "\t" + mrna)
file_in.close