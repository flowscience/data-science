#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     18/12/2013
# Copyright:   (c) Eli 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#print "This script looks through a sorted fasta file to find unique seeds for miRNA families by name

file_in = open("C:/RNAseq/ref/ascidian_mirs_sorted.txt", "r")
#file_out = open("C:/RNAseq/miR_targets/RNAhybrid/f2-7_mfe-22_p0.1_clusters/countsfixed.txt", "w")

data = {}

for line in file_in:
    seed = line.split()[1][1:8] #choose seed size and position
    species = line.split()[2]
    name = line.split()[0]
    name = "-".join(name.split("-")[0:2]) #remove duplicate gene number, 5p and 3p annotations
    if name[-1].isdigit():
        pass
    else:
        name = name[0:-1] #remove alphabetic gene suffixes
    print "input line:", name, seed, species
    if name in data: #check if miRNA family name is in table, if true check whether to add seed or species
        print "name found in data:", name
        for subkey in data[name]: #loop through seeds for each miRNA family name
            print "current iterator", subkey, "in", data[name]
            if subkey == seed: #check if seed already a subkey for current miRNA family
                print "SEED FOUND, check if", species, "in", data[name]
                if [species] == data[name][seed]: #loop through species IDs associated with current miRNA key:seed
                        print "SPECIES ALREADY FOUND", name, seed, species, "not added into", data[name]
                        pass
                else:
                        #print data[name][seed]
                        #data[name].update({entry:species}) #add new species ID to current seed
                        print "species before", data[name]
                        data[name][seed].append(species) #add new species ID to current seed
                        print "NEW SPECIES", seed, species, data[name]
            else:
                print "SEED NOT FOUND", name, seed, species, "not added to", data[name]
                pass
        #data[name].update({seed:species}) #add new seed:species pair to current miRNA key
        print "adding", seed, species, "to", data[name]
        data[name].update({seed:species}) #add new seed:species pair to current miRNA key
        print "NEW SEED:", seed, data[name]

    else:
        data[name] = {seed:[species]} # add new miRNA key with current seed:species data
        print "NEW MIRNA:", name, data[name]

print data

for mir in data:
    seeds = []
    for sed in data[mir]:
        if len(sed) >  1: #Output if the seed is found in more than one species
            print mir, sed, data[mir][sed]
        else:
            seeds.append(sed)
        #print "unique seeds", mir, seeds, data[mir][sed]
    if len(seeds) == 1:
        print mir, data[mir], data[mir][sed]
    elif len(seeds) == 2:
        count = 1
        for sed in seeds:
            if count == 1:
                print mir, sed + "a", data[mir][sed]
                count += 1
            elif count == 2:
                print mir, sed + "b", data[mir][sed]
                count = 1
    #else:
     #   for spec in data[mir][sed]:
            #print spec #, data[mir][sed]
      #      if spec == '51511':
       #         print mir, data[mir], len(data[mir])

#print data[]


    #print line.split()[0], seed, line.split()[2]
    #file_out.write(line.split()[0], new, line.split()[2:])

file_in.close()
#file_out.close()
