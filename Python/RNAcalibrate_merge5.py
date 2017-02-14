#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     22/03/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import math
import glob

data = {} #This table will associate each ID with an array of values from the input files

for handle in glob.iglob("C:/RNAseq/calmirdeep_ts*.txt"): #read each file into the table
    f = open(handle, "r")
    for line in f:
        #print line
        if str(line.split("\t")[0]) in data: #check if row ID is in table, add to existing
            #print data[line.split()[0]]
                if str(line.split("\t")[3]) == "nan": #filter out erroenous values
                    pass
                else:
                    data[line.split("\t")[0]].append(float(line.split("\t")[3].strip("'")))
        else:
            if str(line.split("\t")[3]) == "nan":
                    pass
            else:
                if line.split("\t")[0] == "query":
                    pass
                else:
                    data[line.split("\t")[0]] = [float(line.split("\t")[3].strip("'"))] #create new ID key in table
    f.close

print "miR  calibrations  avg  sd  cv" # output file header

for key in data: #filter outliers
    avg = sum(data[key])/len(data[key])
    sd_temp = []
    for n in data[key]:
        sd_temp.append((n-avg)**2)
    sd = math.sqrt(sum(sd_temp)/len(sd_temp))
    cv = sd/avg
    check = 1
    filtered_vals = data[key]
    for i in range(len(data[key])):
        if abs(cv) > 0.05 and len(filtered_vals) > 1 or min(filtered_vals) < 0:
            if check == 1: #first pass, remove only negative numbers and zeros
                filtered_vals = []
                for n in data[key]:
                    if n <= 0:
                        pass
                    else:
                        filtered_vals.append(n)
                check += 1
            else:
                avg = sum(filtered_vals)/len(filtered_vals)
                sd_temp = []
                for n in filtered_vals:
                    sd_temp.append((n-avg)**2)
                sd = math.sqrt(sum(sd_temp)/len(sd_temp))
                cv = sd/avg
                #print check, cv, len(filtered_vals)
                temp_vals = []
                if check < 10: #or check == 3: #early passes, use a weak filter on variation
                    for n in filtered_vals:
                        if n > (avg+(sd*2)) or n < (avg-(sd*2)): #allows for light trimming of groups that only have a few outliers
                            pass
                        else:
                            #print "n, avg, sd:", n, avg, sd
                            temp_vals.append(n)
                    filtered_vals = temp_vals
                    check += 1
                elif check < 15: #subsequent passes, option of using a stronger variation filter
                    for n in filtered_vals:
                        if n > (avg+(sd*1.5)) or n < (avg-(sd*1.5)):
                            pass
                        else:
                            #print "n, avg, sd:", n, avg, sd
                            temp_vals.append(n)
                    filtered_vals = temp_vals
                    check += 1
                else: #subsequent passes, option of using a stronger variation filter
                    for n in filtered_vals:
                        if n > (avg+(sd)) or n < (avg-(sd)):
                            pass
                        else:
                            #print "n, avg, sd:", n, avg, sd
                            temp_vals.append(n)
                    filtered_vals = temp_vals
                    check += 1

        else:
            pass
    print key, len(filtered_vals), avg, sd, cv
#print data[key]




