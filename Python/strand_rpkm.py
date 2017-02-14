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


file_in = open('C:\RNAseq\indiv_variation\Ensemble\ens_transcript_reads_013.txt', 'r')
file_out = open('C:\RNAseq\indiv_variation\Ensemble\ens_transcript_reads_013_strand_rpkm.txt', 'w')
opposites_out = open('C:\RNAseq\indiv_variation\Ensemble\ens_transcript_reads_013_strand_rpkm.txt', 'w')

counter = 0
opposites = 0

for line in file_in:
    if line.split()[5] == "+":
        file_out.write(str(line.split()[3] + line.split()[9]).strip("[\", \"]") + "\n")
        if line.split()[6] < line.split()[7:]: # check if read counts were higher on the opposite strand, print both
            opposites_out.write(str(line.split()[3] + line.split()[9:11]).strip("[\", \"]") + "\n")
            opposites+=1
        print counter
    else:
        newline = line.split()[3] + line.split()[10]
        file_out.write(str(newline).strip("[\", \"]") + "\n")
        if line.split()[6] < line.split()[7:]: #check if read counts were higher on the opposite strand, print both
            opposites_out.write(str(line.split()[3] + line.split()[9:11]).strip("[\", \"]") + "\n")
            opposites+=1
        print counter
    counter+=1
print opposites

file_in.close()
file_out.close()



def main():
    pass
if __name__ == '__main__':
    main()


