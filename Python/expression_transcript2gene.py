#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     06/01/2015
# Copyright:   (c) Eli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#This script takes transcript level gene expression data and converts it to
#   gene level data.

#This script takes two files:
#   1) A paired tabular list of gene IDs and all associated transcript IDs
#   2) A data matrix labeled with transcript IDs

#Read in gene-transcript paired ID file



#Replace the transcript ID's with gene ID's
#Find redundant gene ID's and through pairwise comparison remove the lowest means







#Make dictionary composed of {gene:[transcripts]} key:value pairs


#Read data file


#Loop through dictionary keys (genes), for each gene:
#   1) Create an empty dictionary
#   2) Loop through the values (transcripts) for the current key (gene)
#   3) For each transcript, extract the expression values to a list
#   4) Find the mean expression level and add the transcript:mean to the dict
#   5) Extract the transcript ID with the highest mean to a new list


#Loop through gene-transcript paired ID file











def main():
    pass

if __name__ == '__main__':
    main()
