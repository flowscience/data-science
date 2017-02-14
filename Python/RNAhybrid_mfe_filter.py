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

import sys

targets = open("targets_all_f2-7_c.txt", "r")
#collation = open("collated_od.txt", "w")


for line in targets:
    mfe = float(line.split(":")[4])
    if abs(mfe) >= 22.0:
        #print line
         sys.stdout.write(line)