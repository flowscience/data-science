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

targets = open("targets_f2-7_10per_mfe-10_c.txt", "r")
#collation = open("collated_od.txt", "w")

count = 0
other = 0

for line in targets:
    if len(str(line)) > 100:
        count += 1
        if count % 1000 == 0:
            print count
    else:
        other += 1

print "miRNA-target pairs:", count
print "Other:"other