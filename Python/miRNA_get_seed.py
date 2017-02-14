#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     18/12/2013
# Copyright:   (c) Eli 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#print "This script outputs a new file with the last character on each line removed."

file_in = open("C:/RNAseq/miR_targets/RNAhybrid/f2-7_mfe-22_p0.1_clusters/counts2.txt", "r")
#file_out = open("C:/RNAseq/miR_targets/RNAhybrid/f2-7_mfe-22_p0.1_clusters/countsfixed.txt", "w")

for line in file_in:
    seed = line.split()[1][1:8]
    print line.split()[0], new, line.split()[2:]
    #file_out.write(line.split()[0], new, line.split()[2:])

file_in.close()
file_out.close()
