#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     04/04/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import sys

file_in = open("C:/RNAseq/miR_targets/RNAhybrid/run1/targets_6bp_mfe-20_p0.1_c_enscinp_pairs.txt", "r")

for line in file_in:
    mir = line.split("\t")[0]
    if mir[0:4] == "cin-":
        mir = mir[4:]
    mir = "-".join(mir.split("-")[0:2])
    if mir[-1].isdigit():
        pass
    else:
        mir = mir[:-1]
    sys.stdout.write(str(mir) + "\t" + str(line.split("\t")[1]))