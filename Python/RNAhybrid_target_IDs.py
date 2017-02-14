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

targets = open("targets_f2-7_mfe-22_p0.1_c.txt", "r")
#collation = open("collated_od.txt", "w")


for line in targets:
    name = str(line)[0:18]
    print name