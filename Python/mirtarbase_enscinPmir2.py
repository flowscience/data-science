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

mirs = []
for line in ids:
    mir = line.split()[0]
    if mir in mirs:
        #mirs[mir].append(line.split()[2])
        pass
    else:
        mirs.append(mir)
        #mirs[mir] = [line.split()[2]]

for line in orth:
    test = line.split()[1][4:-3]
    #for mir in mirs:
        #print mir, test
        #print mir, line.split()[1]
     #   if "-".join(mir.split("-")[0:2]) == test:
      #      print mir, line.split()[3]

    #if test in mirs:
     ###     print mirs[index], line.split()[3]



