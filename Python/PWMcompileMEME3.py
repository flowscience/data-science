#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     08/04/2015
# Copyright:   (c) Eli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import glob

files = glob.glob("C:/users/eli/downloads/Ciona_intestinalis_2015_04_06_1-31_pm/pwms_all_motifs/*_1.01.txt")

#f_out = open("C:/users/eli/desktop/intestinalis_conserved_all_GFF.txt", "w")
with open("C:/users/eli/desktop/intestinalis_TFmotifs_MEME3.txt", "w") as f_out:
    f_out.write("MEME version 4" +'\n'+'\n')
    f_out.write("ALPHABET= ACGT " +'\n'+'\n')
    f_out.write("strands: + - " +'\n'+'\n')
    f_out.write("Background letter frequencies " +'\n')
    f_out.write("A 0.250 C 0.250 G 0.250 T 0.250" + '\n'+'\n')

    for f in files:
        filename = f.split("\\")[-1].split(".")[0]

        #f_out.write("MOTIF " + filename +'\n')
        #f_out.write("letter-probability matrix: alength= 4 w= 10 nsites= 20 E= 0" + '\n')

        f_in = open(f)
        pwm = []
        w = 0

        for line in f_in:
            if line[0]=="P":
                pass
            else:
                w+=1
                ACGT = line.strip('\n').split('\t')[1:]
                rounded = [round(float(x),6) for x in ACGT]
                error = 1-sum(rounded)
                #errorlist = [x-y for x,y in zip(ACGT,rounded)]
                if error != 0:
                    corrected = [x+(error/4) for x in rounded]
                    corrected = [round(float(x),6) for x in corrected]
                    if sum(corrected)==1:
                        pwm.append("PROBABILITIES DO NOT SUM TO 1")
                    pwm.append(' '.join([str(x) for x in corrected]))
                else:
                    pwm.append(' '.join([str(x) for x in rounded]))

        if w > 0:
            f_out.write("MOTIF " + filename +'\n')
            f_out.write("letter-probability matrix: alength= 4 w= " +str(w)+ " nsites= 20 E= 0" + '\n')
            for pos in pwm:
                f_out.write(pos+'\n')
            f_out.write('\n')

        f_in.close
        f_out.close