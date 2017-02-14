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

file_in = open("C:/rnaseq/mir_targets/rnahybrid/targets_f2-7_mfe-22_c.txt", "r")

for line in file_in:
    new = "\t".join(line.split(":"))
    new = "\t".join(new.split("|"))
    new = "\t".join(new.split())
    #sys.stdout.write(new)
    print new

file_in.close
