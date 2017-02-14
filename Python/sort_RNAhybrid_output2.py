#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Eli
#
# Created:     03/03/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

# THIS SCRIPT SORTS RNAhybrid OUTPUT BY MICRORNA THEN GENE ID


targets = open("C:/RNAseq/targets_f2-7_ALL_c.txt", "r")

text = []
for line in targets:
    text.append(str(line).rstrip("\n"))

targets.close
print "text imported to list, input file closed"
text = [i.split(":") for i in text]
print "list split"
text.sort(key=lambda line: (line[2],line[0]))
print "list sorted"
text = [' '.join(i) for i in text]
print "sorted list rejoined"
file_out = open("C:/RNAseq/targets_f2-7_ALL_c_sorted.txt", "w")
print "file out opened"
for item in text:
    file_out.write(item + "\n")
file_out.close
#print text