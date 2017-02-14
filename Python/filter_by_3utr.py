#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     19/12/2013
# Copyright:   (c) Eli 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


file_in = open('KH.KHGene.2013.gff.gff3', 'r')

for line in file_in:
    if "three_prime_UTR" in line:
          print line

file_in.close()