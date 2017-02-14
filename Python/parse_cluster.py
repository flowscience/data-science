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


#This script takes a mixed miRNA-target pair list and splits into output files for each cluster

file_in = open('C:/RNAseq/mirna_data/clusters/edger_8dpa/8dpa_de_pairs_p01-2.txt', 'r')

first = file_in.readline()
mir = first[first.find("cin"):].split("\t")[0].rstrip("\n")
j = 0
#print mir, j

for line in file_in:
  #print line.split()[1]
  if mir in line:
    with open("C:/RNAseq/mirna_data/clusters/edger_8dpa/%s_p01.txt" %mir, "a") as file_out:
      file_out.write(line)
      file_out.close()
  else:
    mir = line[line.find("cin"):].split("\t")[0].rstrip("\n")
    j+=1
    with open("C:/RNAseq/mirna_data/clusters/edger_8dpa/%s_p01.txt" %mir, "a") as file_out:
      file_out.write(line)
      file_out.close()
    #print mir, j

file_in.close()



#if __name__ == '__main__':
 #   main()
