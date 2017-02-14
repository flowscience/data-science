#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     24/04/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#This script takes a file of  miRs & consensus mature/star sequences and counts reads from text converted miRDeep2 novel miR PDF files

import glob
import math
import csv

#Read the miRDeep provisional IDs & consensus sequences from file
idseqs = {}
ids = open("C:/rnaseq/mirna_data/mirdeep2_novel_mirs/provid_mat_star.txt", "r")
for line in ids: # create key:value pairs of mir:[mature, star]
    idseqs[line.split("\t")[0]] = [line.split("\t")[1], line.split("\t")[2].rstrip("\n")]
ids.close

#Get raw format text converted PDF files
files = glob.glob("C:/rnaseq/mirna_data/mirdeep2_novel_mirs/textconvert/*.txt")

#Put sample ID's into list
samples = ["A16", "A09", "A10", "A15", "A13", "A14", "B08", "B12", "B03", "B15", "B05", "B06"]
samples = sorted(samples)
mirs = {}

# Prepare 2-level dict to hold subkey:(sample) with values (mature/star counts in a 2-list)
# for a primary key:(novel miR)
for mir in idseqs:
    mirs[mir] = {}
    for s in samples:
        mirs[mir][s] = [0, 0]

# Print header row
temp = []
tempcount = {}
for s in samples: #apply hashing algorithm to sort sample IDs as they are sorted during parsing
    tempcount[s] = [0]
for t in tempcount:
    temp.append(t + "-mature")
    temp.append(t + "-star")
print "miRDeep2_ID" + "\t" + "\t".join(temp)


for f in files:
    unique = 0 #unique read counter
    matreads = {} #store mature reads
    starreads = {} #store star reads
    sampcount = {}
    for s in samples: #populate dictionary keys using sample ID's
        matreads[s] = [0]
        starreads[s] = [0]
        sampcount[s] = [0, 0]
    mir = f.split('\\')[-1].rstrip(".txt") #Get miRDeep2 provisional ID from file name
    mature = idseqs[mir][0] #Use provisional ID to get mature sequence
    star = idseqs[mir][1] #Use provisional ID to get star sequence
    f_in = open(f, "r")
    for line in f_in:
        if len(line) > 50: #ignore header lines
            if unique == 0: #first hairpin line, get positions of mature/star sequences
                matpos = line.find(mature)
                starpos = line.find(star)
                unique += 1 #increment unique read counter
                pass
            elif "." in line: #parse lines with precursor hairpin representations
                pin = line.split()[0]
                sample = line.split()[-1] #get sample ID from last column in line
                unique += 1 #increment unique read counter
                if matpos < starpos: #mature is 5'
                    #looppos = starpos - matpos + len(mature)
                    if pin[matpos].isalpha() or pin[matpos+len(mature)-2].isalpha(): # count reads that overlap mature start/end position
                        if pin[matpos-3].isalpha() or pin[matpos+len(mature)+3].isalpha(): #exclude reads that lie "x" bp outside consensus position
                            pass
                        else:
                            matreads[sample].append(int(line.split()[-3]))
                    elif pin[starpos+2].isalpha() or pin[starpos+len(star)].isalpha(): # count reads that overlap star start/end position
                        if pin[starpos-3].isalpha() or pin[starpos+len(star)+3].isalpha(): #exclude reads that lie "x" bp outside consensus position
                            pass
                        else:
                            starreads[sample].append(int(line.split()[-3]))
                elif matpos > starpos: #mature is 3'
                    #looppos = matpos - starpos + len(star)
                    if pin[matpos].isalpha() or pin[matpos+len(mature)].isalpha(): # count reads that overlap mature start/end position
                        if pin[matpos-3].isalpha() or pin[matpos+len(mature)+3].isalpha(): #exclude reads that lie "x" bp outside consensus position
                            pass
                        else:
                            matreads[sample].append(int(line.split()[-3]))
                    elif pin[starpos].isalpha() or pin[starpos+len(star)-2].isalpha(): # count reads that overlap star start/end position
                        if pin[starpos-3].isalpha() or pin[starpos+len(star)+3].isalpha(): #exclude reads that lie "x" bp outside consensus position
                            pass
                        else:
                            starreads[sample].append(int(line.split()[-3]))
    for s in matreads: #sum mature reads and add to sample dict
        count = sum(matreads[s])
        sampcount[s][0] = count
    for s in starreads: #sum star reads and add to sample dict
        count = sum(starreads[s])
        sampcount[s][1] = count
    #continue
    for samp in sampcount:
        mirs[mir][samp][0] = sampcount[samp][0]
        mirs[mir][samp][1] = sampcount[samp][1]

mattot = []
startot = []
for mir in mirs:
    values = []
    for samp in mirs[mir]:
        values.append(mirs[mir][samp][0])
        values.append(mirs[mir][samp][1])
        mattot.append(mirs[mir][samp][0])
        startot.append(mirs[mir][samp][1])
    values = str(values).strip("[]").replace(",", "").replace("[", "").replace("]", "")
    print mir, "".join(values)
print "Mature total:", sum(mattot)
print "Star total:", sum(startot)