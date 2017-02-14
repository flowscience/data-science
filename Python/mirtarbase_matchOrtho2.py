#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     26/03/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

mirtarbase = open("C:/rnaseq/mir_targets/mirtarbase_mti.txt", "r")
ortho = open("C:/rnaseq/mir_targets/mirtarbase_gprofiler_orthos.txt", "r")

matched = {}
count = 0
ids = []
for line in mirtarbase:
    count += 1
    ids.append(line.split("\t")[4])
    #print entrezID

#print ids
for item in ids:
    for line in ortho:
        #print line.split()[1].split(":")[1]
        acc = line.split("\t")[1].split(":")[1]
        #print item, acc
        if acc in ids and acc != "N/A":
            if acc in matched:
                matched[acc].append(line.split()[4])
            else:
                matched[acc] = [line.split()[4]]
                        #print acc, "appended
        else:
            pass
            #if acc == item:
             #   matched[acc] = [line.split()[4]]
                #print acc, "added"
            #else:
          #  pass
    #print count

#print matched

for entrez in matched:
    for ciona in entrez:
        print entrez, matched[entrez][ciona]
    #print entrez, "\t".join(matched[entrez])