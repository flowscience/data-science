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

pairs = {}
for line in orth:
    mir = "-".join(line.split()[1].split("-")[1:3])
    if mir in pairs:
        pairs[mir].append(line.split()[3])
    else:
        pairs[mir] = [line.split()[3]]

for mir in pairs:
    for g in set(pairs[mir]):
        print mir, g


