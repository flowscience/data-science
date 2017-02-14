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

#This script extracts duplicates from a data file by comparing Id's and/or values in each row

ids = open("C:/rnaseq/mirna_data/compiled_mir_expression_data_norm.txt", "r")
idlist1 = {}

added = 0
duplist = []
line_count = 0
valsmatched = []
valsmatchedshortname = []
for line in ids: #loop thru file
    line_count+=1
    #print 'line count:', line_count
    name = line.split('\t')[0]
    if '-' in name: #remove species prefix & alphanumeric suffixes for miRNA genes (e.g. cin-let-7e-2 becomes let-7)
        name = '-'.join(name.split('-')[1:3])
        if name[-1].isalpha():
            name = name[:-1]
    #print name
    values = line.split('\n')[0].split('\t')[1:] #put values from all columns into a single vector for comparison
    #print 'Values:', values
    for x in idlist1: #loop thru dictionary
        #print 'Idlist[x]:', idlist1[x]
        if values == idlist1[x]: #check whether values in current line match any previous lines added to dictionary
            #print 'Values matched'
            #print 'name', name.split('-')[1:3]
            #print 'dict name:', x.split('-')[1:3]
            if name == x: #if values match, check for name similarity
                #print '**Names matched: skipping', name + '**'
                duplist.append(line.split('\t')[0]) #append full length name to duplicate list
                #DUPLICATE NOT ADDED TO DICTIONARY THAT ALREADY CONTAINS A MATCHING SHORT NAME/VALUE PAIR
                continue
            else: #names do not match
                valsmatched.append(line.split('\t')[0])
                valsmatchedshortname.append(name)
                if name in idlist1: #check if name already in dictionary
                    break
                #else:
                #    idlist1[name] = values #append short name and values to dictionary
                #print name, 'added with identical values to', x
                    added+=1
                break
        else: #values do not match
            continue
    idlist1[name] = values #add to dictionary when neither name/values match for comparison to subsequent rows
    added+=1

#print 'Line Count:', line_count
#print 'Added to dict:', added
#print 'Values matched:', len(valsmatched)
#print valsmatched
for item in valsmatched:
    print item
#print 'Dups:', len(duplist)
#print duplist
