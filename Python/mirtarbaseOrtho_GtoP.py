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

prot = open("C:/rnaseq/ref/enscinGTP_ID.txt")

pairs = {}
for line in prot:
    if line.split("\t")[0] in pairs:
        pairs[line.split("\t")[0]].append(line.split("\t")[2])
    else:
        pairs[line.split("\t")[0]] = [line.split("\t")[2]]

prot.close

gene = open("C:/rnaseq/ref/mirtarbase_orthos.txt")

for line in gene:
    test = line.split()[2].rstrip("\n")
    if test == "N/A":
        pass
    elif test in pairs:
        prots = []
        for p in set(pairs[test]):
            prots.append(p)
        for p in set(prots):
            print line.split()[0], line.split()[1], test, p
    else:
        pass
gene.close
