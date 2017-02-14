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

import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
       print 'test.py -i <inputfile> -o <outputfile>'
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print 'test.py -i <inputfile> -o <outputfile>'
          sys.exit()
       elif opt in ("-i", "--ifile"):
          inputfile = arg
       elif opt in ("-o", "--ofile"):
          outputfile = arg
          print 'Output file is "', outputfile
    #print 'Input file is "', inputfile


    #This script filters a data file by id's listed one per line in another file


    ids = open(inputfile, "r")

    #Take header from ID file & initialize empty dict
    #head_ids = ids.readline().strip("\n")
    idlist1 = {}
    target_list = []
    targets=0
    #Make dict of ID's (key) & selected variables/annotations (values)
    for line in ids:
        name = line.strip('\n').split('\t')[0]
        #name = name.strip('cin-')
        values = line.strip('\n').split('\t')[1]
        if name in idlist1:
            if values in idlist1[name]:
                continue
            else:
                idlist1[name].append(values)
                targets+=1
                target_list.append(values)
        else:
            idlist1[name] = [values]
            targets+=1
            target_list.append(values)
    ids.close

    #Debugging code below:
    print 'Unique Queries:', len(idlist1)
    print 'Query-Target Pairs:', targets
    print 'Unique Targets:', len(set(target_list))

if __name__ == "__main__":
   main(sys.argv[1:])