#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     14/04/2015
# Copyright:   (c) Eli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import sys

#Read data
f_in = open("C:/users/eli/downloads/ish/ish_ci.xml")

#Print header row
sys.stdout.write("gene" +"\t"+ "stage" +"\t"+ "tissue" +"\t"+ "pattern" +"\t"+ "original" +"\t"+ "source" +"\t"+ "exp" +"\t"+ "note" +'\n')

#Set number of header rows to skip
headers = 3
count = 1
source = False

for line in f_in:

    #Skip specified number of header lines
    if count <= headers:
        count+=1
        pass

    #Parse desired information
    else:
        if "experiment id" in line:
            exp = "NA"
            stage = "NA"
            stage_source = "NA"
            gene = "NA"
            tissue = "NA"
            note = "NA"
            pattern = "NA"
            original = "NA"
            exp = line.split('"')[1]
        if "developmental_stage" in line and source == False:
            stage = line.split(">")[1].split('<')[0]
            source = True

        if "developmental_stage" in line and source == True:
            stage_source = line.split(">")[1].split('<')[0]
            source = False

        if "probe_gene_predicted" in line:
            gene = line.split(">")[1].split('<')[0]

        if "staining_localization" in line:
            tissue = line.split(">")[1].split('<')[0]

        if "image_note" in line:
            note = line.split(">")[1].split('<')[0]
            if "Expression pattern:" in note:
                pattern = note.split("Expression pattern:")[1].split("<")[0]

            if "Original annotation:" in note:
                original = note.split("Original annotation:")[1].split(".")[0]

        else:
            pass

        #Output information for parsed record
        if "/experiment" in line:
            #results = [gene, stage, tissue, pattern, original, exp, note]
            output = "\t".join([gene, stage, tissue, pattern, original, stage_source, exp, note])
            sys.stdout.write(output + '\n')
