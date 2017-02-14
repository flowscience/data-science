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




file_in = open('C:/RNAseq/multihits_f27_e10_p01.txt', 'r')

i = file_in.readline()[0:11]
print i
j = 0

for line in file_in:
  #print line.split()[1]
  if line.split()[0] == i:
    with open("C:/RNAseq/temp/multihits_f27_e10_p01_%s.txt" %i, "a") as file_out:
      file_out.write(line)
      file_out.close()
  else:
    i = line.split()[0]
    j+=1
    print i, j

file_in.close()



#if __name__ == '__main__':
 #   main()
