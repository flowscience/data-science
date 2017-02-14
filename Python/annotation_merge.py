#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     22/01/2015
# Copyright:   (c) Eli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#This script takes a tab delimited file of ID's, each with many annotations
#   and returns a single annotation per ID based on order of the variables
#   (earlier ones are evaluated first) and desired filtering criteria
#Load dependencies
import sys

#Load data
f = open("C:/users/eli/desktop/smith_lab/geo_data/life_cycle/data/encinGT_emblGenbank_refseq2.txt")

#Make empty list to count number of ID's assigned to each variable
counts = [0]
i = 1

#Get ID for each line
for line in f:
    id = line.strip('\n').split('\t')[1]

    #Count number of variables and expand assignment counting list
    if i == 1:
        vars = len(line.split('\t'))
        counts = counts*vars
        i+=1

    #Assess variables
    for i in range(2,vars): #Start with 3rd column

        #Extract value from current variable
        annot = line.strip('\n').split('\t')[i]

        #Check variable for conditions
        if "X" in annot: #Check for refseq identifier "XM" or "XR"
            sys.stdout.write(id + "\t" + annot + '\n')
            counts[i]+=1
            break

        #Print last variable if no matches found
        elif i == vars:
            sys.stdout.write(id + "\t" + annot + '\n')
            counts[i]+=1
            break

#Return number of ID's assigned to each variable
print "\t".join(str(n) for n in counts)




