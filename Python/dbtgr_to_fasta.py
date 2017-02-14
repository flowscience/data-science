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


file_in = open('dbtgr.sequences.tab', 'r')
file_out = open('dbtgr_promoters.fasta.txt', 'a')

for line in file_in:
    file_out.write(">" + line.split()[1] + "\n")
    temp = line.split()
    for item in temp:
            if len(item) > 100:
                file_out.write(item + "\n" + "\n")


file_in.close()
file_out.close()


