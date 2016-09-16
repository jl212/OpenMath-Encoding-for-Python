# Python parser for OpenMath (http://www.openmath.org/)
# See https://docs.python.org/3.4/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
Element = ET.Element
SubElement = ET.SubElement

import omparse
from omparse import *

import omput
from omput import *

import xml.dom.minidom as MD

################################################################

def ParseOMfile(fname):
    """Parses xml file (OpenMath encoding) to a Python representation"""
    tree = ET.parse(fname)
    root = tree.getroot()
    omobj = ParseOMroot(root)
    return omobj

def ParseOMstring(omstring):
    """Parses xml string (OpenMath encoding) to a Python representation"""
    root = ET.fromstring(omstring)
    omobj = ParseOMroot(root)
    return omobj

################################################################
def OMppstring( x ):
    """Turns given Python object into an OM xml string with indentation"""
    print((MD.parseString(OMstring(x))).toprettyxml())

def OMstring( x ):
    """Turns given Python object into an OM xml string"""
    return ET.tostring( OMobject( x ) ) 

def OMprint( x ):
    """Prints OM representation of given Python object to standard output"""
    ET.dump( OMobject( x ) ) 

################################################################

