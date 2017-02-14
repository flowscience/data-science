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
with open("C:/users/eli/desktop/intestinalis_TFmotifs_transfac2.txt", "w") as f_out:
    for f in files:
        filename = f.split("\\")[-1].split(".")[0]

        f_out.write(filename + '\n')
        f_out.write("C.intestinalis" + '\n')

        f_in = open(f)
        for line in f_in:
            if line[0]=="P":
                f_out.write("P0" +'\t'+ "A" +'\t'+ "C" +'\t'+ "G" +'\t'+ "T" +'\n')
            elif int(line.split('\t')[0]) < 10:
                f_out.write("0"+line)
            else:
                f_out.write(line)

        f_out.write("XX" + '\n')
        f_out.write("//" + '\n')

        f_in.close
        f_out.close