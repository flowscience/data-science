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

#This script re-parses the output from filterbyID_dict_parse
#It finds refseq ID's (should be unique in file, one per line) and checks whether
#   multiple genes have been assigned. If so, it splits the genes and returns them
#   one per line with the matching refseqID and any other data.

import sys

data = open("C:/users/eli/desktop/smith_lab/geo_data/life_cycle/data/encinT_cloneBLAST_refseqGenbank.txt")
i=1


for line in data:
    if i == 1:
        head_cols = len(line.strip('\n').split('\t'))
        i+=1
        sys.stdout.write(line)
    else:
        cols = len(line.strip('\n').split('\t'))
        if cols > head_cols:
            genes = head_cols-cols
            gene_list = line.split('\t')[0:genes]
            annot = line.strip('\n').split('\t')[genes:]
            for gene in gene_list:
                sys.stdout.write(gene +'\t' + annot)

        else:
            sys.stdout.write(line)





def main():
    pass

if __name__ == '__main__':
    main()
