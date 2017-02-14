#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     06/04/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import sys

#This script filters a MEME motif file by id's listed one per line in another file

#Read id list file
ids = open("C:/users/eli/desktop/tf_list.txt", "r")
idlist1 = []
for line in ids:
    thing = line.strip('\n').split('\t')[0]

    #Trim input ID if necessary to match ID's in MEME motif file
    thing = thing[0:-3]
    idlist1.append(thing)
ids.close

#Read MEME motif file
data = open("C:/users/eli/desktop/intestinalis_TFmotifs_MEME3.txt", "r")

for line in data:
    #Print all header rows by default
    output = True

    #Check if current motif ID in input list
    if "MOTIF" in line:
        name = line.strip('\n').split(' ')[1]
        if name in idlist1:
            output = True
        else:
            output = False

    #If yes, write all lines until next motif
    elif output == True:
        sys.stdout.write(line)

