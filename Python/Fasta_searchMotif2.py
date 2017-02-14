#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Eli
#
# Created:     03/03/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import sys
import re

sequences = open("C:/users/eli/desktop/otx_targets/late_consensus_fasta.txt", "r")

motifs = ["AAAAC", "AATTG", "GATTA", "AAACA", "ATTAG", "AAATC", "ATTAA", "AATTA", "AAAGC", "AACAA"]
motifs = sorted(motifs)

#Print header row
sys.stdout.write("Gene" + '\t' + '\t'.join(motifs) + '\n')

rowcount = 0

for line in sequences:
    if line.startswith(">"):

        #Process previous sequence before moving to next
        if rowcount > 0 and len(seq) > 0:
            seq = ''.join(seq)
            motif_dict = {key: "" for key in motifs}

            for motif in motifs:
                positions = [m.start() for m in re.finditer(motif, seq)]
                pairs = []
                index = 0
                count = 0

                for pos in positions:
                    if index == 0:
                        last = pos
                        index+=1
                    else:
                        current = pos
                        #Define distance between motif occurences
                        if current-last <= 125:
                            count+=1
                            pairs.append([last,current])
                            index+=1
                            last = current
                motif_dict[motif] = count

            motif_counts = []
            for m in motif_dict:
                motif_counts.append([m, motif_dict[m]])
            motif_counts = sorted(motif_counts)

            counts = []
            for m2 in motif_counts:
                counts.append(str(m2[1]))
            sys.stdout.write(name + '\t' + '\t'.join(counts) + '\n')

        #Proceed to next sequence
        name = line.lstrip(">").strip('\n') #line.replace(line, line[5:-14])
        seq = []
        rowcount+=1

    #Add lines of sequence to list until next header row reached
    else:
        seq.append(line.strip('\n'))

#for pair in pairs:
    #sys.stdout.write(str(pair[0])), sys.stdout.write(str(pair[1]))
#    sys.stdout.write(str(pair).strip("['']").replace("\\n","") + "\n")
    #sys.stdout(str(pair))
    #collation.write(str(pair))

#print len(pairs)
