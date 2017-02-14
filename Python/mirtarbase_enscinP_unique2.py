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

orth = open("C:/rnaseq/ref/mirtarbase_enscinp.txt")
ids = open("C:/rnaseq/ref/ascidian_mirs_sorted.txt")

pairs = {}
for line in orth:
    mir = "-".join(line.split()[1].split("-")[1:3])
    if mir in pairs:
        pairs[mir].append(line.split()[3])
    else:
        pairs[mir] = [line.split()[3]]

mirs = []
for line in ids:
    mir = "-".join(line.split()[0].split("-")[0:2])
    if mir[-1].isdigit():
        pass
    else:
        mir = mir[:-1]
    #print mir
    if mir in mirs:
        #mirs[mir].append(line.split()[2])
        pass
    else:
        mirs.append(mir)
        #mirs[mir] = [line.split()[2]]

new = {}
for mir in mirs:
    if mir in pairs:
        new[mir] = pairs[mir]
    else:
        pass

for mir in new:
    for g in set(pairs[mir]):
        print mir, g


