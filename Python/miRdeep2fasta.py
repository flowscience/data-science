#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     19/12/2013
# Copyright:   (c) Eli 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#def main():


#if __name__ == '__main__':
 #   main()


file_in = open('C:/rnaseq/miRna_data/mirdeep_precursor.txt', 'r')

for line in file_in:
    print ">" + line.split("\t")[0]
    print line.split("\t")[1]

file_in.close()



