#-------------------------------------------------------------------------------
# Name:        module1
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

from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("C:/users/eli/downloads/ish/ish_ci.xml")
collection = DOMTree.documentElement
#if collection.hasAttribute("experiments"):
#   print "Root element : %s" % collection.getAttribute("experiments")

# Get all the movies in the collection
experiments = collection.getElementsByTagName("experiment")

# Print detail of each movie.
for exp in experiments:

   if exp.hasAttribute("developmental_stage"):
      stage = exp.getAttribute("developmental_stage")

   type = exp.getElementsByTagName('probe_gene_predicted')[0]
   print "Type: %s" % probe_gene_predicted.childNodes[0].data
