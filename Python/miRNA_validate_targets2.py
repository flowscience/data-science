#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     04/04/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#This file determines how many miRNA-target pairs are in one list compared to another list


valid = open("C:/rnaseq/mir_targets/mirtarbase_enscinp_consmir.txt", "r")
true = {}
for line in valid: #read validated mir-target pairs into a dictionary
    mir = line.split("\t")[0]
    mrna = line.split("\t")[1].rstrip("\n")
    #print mir, mrna
    if mir in true:
        true[mir].append(mrna)
    else:
        true[mir] = [mrna]
valid.close

tot_true = 0
for mir in true: # Calculate number of non-redundant validated miRNA-target pairs
    tot_true += len(true[mir])
print "validated targets", tot_true

test = open("C:/RNAseq/miR_targets/rnah_ts_accessfilter_pairs.txt", "r")
tot_test = 0
matched = 0
for line in test: # Check if test miRNA-target pairs are in validated set
    if len(line) > 20:
        tot_test += 1
        mir = line[line.find("cin-"):].split("\t")[0].rstrip("\n")
        if mir[0:4] == "cin-":
            mir = mir[4:]
        mir = "-".join(mir.split("-")[0:2])
        #print mir
        while mir[-1].isdigit() == False:
            mir = mir[:-1]
        else:
            pass
        #print mir
        #mrna = line[9:].strip(" ")
        mrna = line[line.find("ENSCIN"):].split()[0].rstrip("\n")
        mrna = mrna.replace("T", "P")
        #print mrna
        #print mir, mrna
        if mir in true:
            #print mrna, "mir found"
            #print true[mir]
            if mrna in true[mir]:
                print mir, mrna
                matched += 1
        else:
            pass
test.close

print "Validated Pairs Retrieved:", matched
print "Precision:", matched/tot_test, str(matched) + '/' + str(tot_test)
print "Recall:", matched/tot_true, str(matched) + '/' + str(tot_true)
