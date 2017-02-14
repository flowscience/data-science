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



import glob
import os
os.chdir("C:/rnaseq/polyA_data/counts")

files = glob.glob("C:/rnaseq/polyA_data/counts/BC*.txt")
#print files

i=1

for file_in in files:
    name = file_in.split("\\")[-1]
    print name
    f = open(file_in)
    file_out = open('C:/RNAseq/polyA_data/rpkm/%s.txt' %name, 'a')
    transcripts = 0
    for line in f:
        if "mRNA" in line:
            file_out.write(line)
            transcripts+=1
    f.close()
    file_out.close()
    print f, "Transcripts:", transcripts
    i+=1


def main():
    pass

if __name__ == '__main__':
    main()


