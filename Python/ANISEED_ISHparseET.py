#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Eli
#
# Created:     14/04/2015
# Copyright:   (c) Eli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#http://effbot.org/zone/element.htm

import elementtree.ElementTree as ET
import sys

tree = ET.parse("C:/users/eli/downloads/ish/ish_ci.xml")

# the tree root is the toplevel html element
print tree.findtext("experiment")

# if you need the root element, use getroot
root = tree.getroot()

print root
