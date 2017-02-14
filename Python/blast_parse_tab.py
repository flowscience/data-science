#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eli
#
# Created:     04/02/2015
# Copyright:   (c) Eli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


import sys

##########################################

#Read ID file
f = open("C:/users/eli/desktop/jgi_mrna_tab.txt")

for line in f:
    if "#" in line:
        pass
    else:
        sys.stdout.write(line)