#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     09/04/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

f1 = open("C:/rnaseq/polyA_data/clusters/1dpa_DE_fdr05_redo.txt", "r")
f2 = open("C:/rnaseq/polyA_data/clusters/3dpa_DE_fdr05_redo.txt", "r")
f3 = open("C:/rnaseq/polyA_data/clusters/8dpa_DE_fdr05_redo.txt", "r")

#Loop through files and extract ID's to lists
f1_ids = []
f2_ids = []
f3_ids = []

count = 1
for line in f1:
    if count == 1: #skip header row
        count += 1
        pass
    else:
        f1_ids.append(str(line.split("\t")[0]))
count = 1
for line in f2:
    if count == 1: #skip header row
        count += 1
        pass
    else:
        f2_ids.append(str(line.split("\t")[0]))
count = 1
for line in f3:
    if count == 1: #skip header row
        count += 1
        pass
    else:
        f3_ids.append(str(line.split("\t")[0]))

#Cross check ID lists, errors can occur if the files aren't formatted properly.
#print f1_ids, f2_ids, f3_ids

f1 = open("C:/rnaseq/polyA_data/clusters/1dpa_DE_fdr05_redo.txt", "r")
f2 = open("C:/rnaseq/polyA_data/clusters/3dpa_DE_fdr05_redo.txt", "r")
f3 = open("C:/rnaseq/polyA_data/clusters/8dpa_DE_fdr05_redo.txt", "r")

linecount = 1
for line in f1: # check whether ids in first condition matched others
    added = 0
    if linecount == 1:
        linecount += 1
    else:
        for ids2 in f2_ids:
            if ids2 in line: # 1dpa id matched to 3dpa id
                for ids3 in f3_ids:
                    if ids3 in line: #1dpa id also matched to 8dpa
                        with open("C:/RNAseq/polyA_data/clusters/edgeR_de_1-3-8dpa_redo.txt", "a") as file_out:
                            file_out.write("1dpa" + "\t" + line)
                            file_out.close()
                            added = 1
                            break

                    else: #1dpa id only matched to 3dpa id
                        pass
                with open("C:/RNAseq/polyA_data/clusters/edgeR_de_1-3dpa_redo.txt", "a") as file_out:
                            file_out.write("1dpa" + "\t" + line)
                            file_out.close()
                            added = 1
                            break
        # id is unique to 1st condition
        for ids3 in f3_ids:
                    if ids3 in line: #1dpa matched only to 8dpa
                        with open("C:/RNAseq/polyA_data/clusters/edgeR_de_1-8dpa_redo.txt", "a") as file_out:
                            file_out.write("1dpa" + "\t" + line)
                            file_out.close()
                            added = 1
                            break
                    else:
                        #print "unique to first condition"
                        pass
        if added == 0:
            with open("C:/RNAseq/polyA_data/clusters/edgeR_de_1dpa_unique_redo.txt", "a") as file_out:
                            file_out.write("1dpa" + "\t" + line)
                            file_out.close()
                            continue

linecount = 1
for line in f2: # check whether ids in second condition matched others
    added = 0
    if linecount == 1:
        linecount += 1
    else:
        for ids1 in f1_ids:
            if ids1 in line: # 3dpa id matched to 1dpa id
                for ids3 in f3_ids:
                    #print "8dpa", ids
                    if ids3 in line: #1dpa id also matched to 8dpa
                        with open("C:/RNAseq/polyA_data/clusters/edgeR_de_1-3-8dpa_redo.txt", "a") as file_out:
                            file_out.write("3dpa" + "\t" + line)
                            file_out.close()
                            added = 1
                            break
                    else: #3dpa id only matched to 1dpa id
                        pass
                with open("C:/RNAseq/polyA_data/clusters/edgeR_de_1-3dpa_redo.txt", "a") as file_out:
                            file_out.write("3dpa" + "\t" + line)
                            file_out.close()
                            added = 1
                            break
        for ids3 in f3_ids:
                    if ids3 in line: #3dpa matched only to 8dpa
                        with open("C:/RNAseq/polyA_data/clusters/edgeR_de_3-8dpa_redo.txt", "a") as file_out:
                            file_out.write("3dpa" + "\t" + line)
                            file_out.close()
                            added = 1
                            break
                    else:
                        pass
        if added == 0:
            with open("C:/RNAseq/polyA_data/clusters/edgeR_de_3dpa_unique_redo.txt", "a") as file_out:
                            file_out.write("3dpa" + "\t" + line)
                            file_out.close()
                            continue


linecount = 1
for line in f3: # check whether ids in 3rd condition matched others
    added = 0
    if linecount == 1:
        linecount += 1
    else:
        for ids1 in f1_ids:
            if ids1 in line: # 8dpa id matched to 1dpa id
                for ids2 in f2_ids:
                    #print "3dpa", ids
                    if ids2 in line: #8dpa id also matched to 3dpa
                        with open("C:/RNAseq/polyA_data/clusters/edgeR_de_1-3-8dpa_redo.txt", "a") as file_out:
                            file_out.write("8dpa" + "\t" + line)
                            file_out.close()
                            added = 1
                            break
                    else: #8dpa id only matched to 1dpa id
                        pass
                with open("C:/RNAseq/polyA_data/clusters/edgeR_de_1-8dpa_redo.txt", "a") as file_out:
                            file_out.write("8dpa" + "\t" + line)
                            file_out.close()
                            added = 1
                            break
        for ids2 in f2_ids:
                    if ids2 in line: #8dpa matched only to 3dpa
                        with open("C:/RNAseq/polyA_data/clusters/edgeR_de_3-8dpa_redo.txt", "a") as file_out:
                            file_out.write("8dpa" + "\t" + line)
                            file_out.close()
                            added = 1
                            break
                    else:
                        pass
        if added == 0:
            with open("C:/RNAseq/polyA_data/clusters/edgeR_de_8dpa_unique_redo.txt", "a") as file_out:
                            file_out.write("8dpa" + "\t" + line)
                            file_out.close()
                            continue

f1.close
f2.close
f3.close