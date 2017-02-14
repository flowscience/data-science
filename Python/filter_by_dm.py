#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     20/10/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


import sys
from itertools import islice


with open("C:/rnaseq/mirna_data/compiled_mir_expression_data_norm_3cpm3_CV-1_any_diffmean2.txt") as f:

    # Find columns containing "dm" in the header row, put in dictionary with column indices
    first_line = f.readline()
    first_split = first_line.split("\t")
    dm_names = {}
    for colname in first_split:
        if "dm" in colname:
            dm_names[colname] = first_split.index(colname) #add 'colname':index to dictionary
    groups = []
    for colname in dm_names:
        groups.append(colname[2:4])
    groups = set(groups)
    #print "Groups:", groups
    #print "Sample Names:", dm_names

    #calculate dms for each dm column, add to dictionary as 'colname:dm'
    dm_vals = {}
    dms = {}
    rownum = 1
    temp = open("C:/rnaseq/mirna_data/temp_out.txt", "w") # Copy data to temp file to remove header row and enable proper sorting
    for row in f:
        #print row
        temp.write(row.replace("\t", ' ').strip('\n'))
        if rownum == 1:
            for colname in dm_names:
                dm_vals[colname] = [float(row.split("\t")[dm_names[colname]])]
        else:
            for colname in dm_names:
                #print row.split("\t")[dm_names[colname]], rownum
                dm_vals[colname].append(float(row.split("\t")[dm_names[colname]]))
        rownum+=1
    temp.close()
    for colname in dm_vals:
        dms[colname] = sum(dm_vals[colname])/rownum

    # Store data rows in an object
    file_out = open("C:/rnaseq/mirna_data/temp_out.txt", "r")
    data = file_out.readlines()
    file_out.close

        #print colname, dm_names[colname]
        #print(sum(float(row.split()[13] for row in f)))
        #print(sum(row.split(13) for row in list(f)))
        #print(sum(float(row.split()[13] for row in list(f))))
        #dms[colname] = sum(float(row.split()[13]) for row in f) #islice(f, a, b)) # a= first row, b=last row,

    # construct another dictionary containing 'group name:[dms]'
    group_dms = {}
    for group in groups:
        count_groups = len(groups)
        #print group
        for colname in dms:
            #print colname
            if group in colname:
                if group in group_dms:
                    group_dms[group].append(dms[colname])
                    #print group, colname
                else:
                    group_dms[group] = [dms[colname]]
                    #print colname, dms[colname]
            else:
                pass
    #print group_dms


    rm_rows = [] #list to be populated with row ID's that should be removed
    for group in group_dms:
        big = max(group_dms[group]) #find the maximum dm value in each group
        for colname in dms:
            if str(big) in colname: #find the sample ID corresponding to the maximum dm in each group
                for colname in dm_names:
                    #sample = colname
                    data = sorted(data, key=colname)
        for line in islice(f, 2, 2):
            print line
            rm_rows.append(line.split('/t')[0])
    print rm_rows



    print((max(dms.values())))
    sorted(f, key=max(dms[colname]))

    # for each dm group, find max, sort by that col, add row ID to list, copy other rows to temp file, repeat


