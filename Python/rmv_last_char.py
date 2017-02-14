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

print "This script outputs a new file with the last character on each line removed."

file_in = open("Ci_rRNA_end.txt", "r")
file_out = open("endfixed.txt", "w")

lines = []

for line in file_in:
    new = line[:-2]
    file_out.write(new + '\n')

file_in.close()
file_out.close()
