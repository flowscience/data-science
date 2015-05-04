#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     18/02/2015
# Copyright:   (c) Eli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


#This script computes the Group Average-Sum (GAS) Correlation between two sets
# of variables from grouped unmatched observations

import itertools
import sys
import math as math

#Define helper functions
def sum_of_squares(x):
    return sum([i**2 for i in x])

def square_of_sum(x):
    return sum(x) ** 2

#Read data, number of observations for X and Y must be the same within each group
mirs = open("C:/rnaseq/mirna_data/compiled_mir_expression_norm_1cpm3_noparalogs2_10rep.txt")

#Read in headers from data
head_mirs = mirs.readline().strip("\n")

#Print header to output
sys.stdout.write("miRNA" + '\t' + 'mRNA' + '\t' + "Matched" + '\t' + "AvgXY" + '\t' "Min.Rho"+ '\t' "Avg.Rho"+ '\t' "Max.Rho" + '\n')

count=0
count2 = 0
#Loop thru first set of variables - extract values for each variable by group
for row in mirs:
    n = len(row.strip('\n').split('\t')[1:])
    mir = row.split('\t')[0]
    mvals = map(float, row.strip('\n').split('\t')[1:11])
    m0 = map(float, mvals[0:2])
    m1 = map(float, mvals[2:4])
    m3 = map(float, mvals[4:7])
    m8 = map(float, mvals[7:10])

    #Calculate common correlation intermediates for current observation in first set
    sx = sum(mvals) #sum of X
    sx2 = sum_of_squares(mvals) #sum of x^2
    s2x = square_of_sum(mvals) #(sum of x)^2

    polya = open("C:/rnaseq/polya_data/rpkm/rpkm_strand_redo_lessBC9_5for3.txt")
    head_polya = polya.readline().strip("\n")

    #Loop thru second set of variables for each variable in first set
    #Extract values for each variable by group
    for row in polya:
        count2+=1
        mrna = row.split('\t')[0]
        pvals = map(float, row.strip('\n').split('\t')[1:11])
        p0 = map(float, pvals[0:2])
        p1 = map(float, pvals[2:4])
        p3 = map(float, pvals[4:7])
        p8 = map(float, pvals[7:10])

        #Calculate common correlation intermediates for current observation in second set
        sy = sum(pvals) #sum of X
        sy2 = sum_of_squares(pvals) #sum of y^2
        s2y = square_of_sum(pvals) #(sum of y)^2

        #Calculate X*Y's for within group combinations, X and Y must be same length within groups
        #Each list will contain only all combinations of sets, e.g. [X1*Y1, X2*Y2] & [X1*Y2, X2*Y1]
        #Length of each = number of possible ordered combinations = factorial(len(x)) or factorial(len(y))
        T0 = [sum([a*b for a,b in zip(j,k)]) for j,k in zip([m0]*2,list(itertools.permutations(p0, 2)))]
        T1 = [sum([a*b for a,b in zip(j,k)]) for j,k in zip([m1]*2,list(itertools.permutations(p1, 2)))]
        T3 = [sum([a*b for a,b in zip(j,k)]) for j,k in zip([m3]*6,list(itertools.permutations(p3, 3)))]
        T8 = [sum([a*b for a,b in zip(j,k)]) for j,k in zip([m8]*6,list(itertools.permutations(p8, 3)))]

        #T0 = [[m*p for m in m0] for p in p0]
        #T1 = [[m*p for m in m1] for p in p1]
        #T3 = [[m*p for m in m3] for p in p3]
        #T8 = [[m*p for m in m8] for p in p8]

        #Produce all combinations between groups of XY combinations
        #Generates 2x nesting: Each sublist is [T0,T1,T2,T3]
        #Length of each = number of possible combinations = len(T0)*len(T1)*len(T2)*len(T3)
        T0138 = [sum([m,p,q,r]) for m in T0 for p in T1 for q in T3 for r in T8]
        #avgXY = sum(T0138)/len(T0138)

        #Estimate rho for each combination
        rhos = []
        for sxy in T0138:
            r = (n*sxy-sx*sy)/math.sqrt((n*sx2-(s2x))*(n*sy2-(s2y)))
            rhos.append(r)

        minR = min(rhos)
        maxR = max(rhos)
        aveR = sum(rhos)/len(rhos)
        #aveXYR = (n*avgXY-sx*sy)/math.sqrt((n*sx2-(s2x))*(n*sy2-(s2y)))

        #Calculate traditional sum of xy
        sxyt = float(sum([m*p for m,p in zip(mvals,pvals)]))
        rt = (n*sxyt-sx*sy)/math.sqrt((n*sx2-(s2x))*(n*sy2-(s2y)))

        #Print result for current pair of variables
        if minR*maxR > 0:
            sys.stdout.write(mir + '\t' + mrna + '\t' + str(rt) + '\t' + str(minR) + '\t'  + str(aveR) + '\t'  + str(maxR) + '\n')
    continue