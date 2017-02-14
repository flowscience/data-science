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


file_in = open('C:\RNAseq\indiv_variation\Ensemble\enscinT_strand_rpkm.txt', 'r')
file_out = open('C:\RNAseq\indiv_variation\Ensemble\enscinT_strand_rpkm+1.txt', 'w')

i = 0

for line in file_in:
     if float(line.split()[2]) >= 1:
      if float(line.split()[3]) >= 1:
        if float(line.split()[4]) >= 1:
         # print line
          file_out.write(line + "\n")
          i+=1

print i
file_in.close()
file_out.close()



def main():
    pass

if __name__ == '__main__':
    main()


