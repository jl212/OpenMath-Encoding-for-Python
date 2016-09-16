# Encoding Python parser for OpenMath (http://www.openmath.org/)
# See https://docs.python.org/3.4/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
Element = ET.Element
SubElement = ET.SubElement

import objects
import types

from omparse import omdicts

################################################################
#
# OpenMath integer (OMI)
#
def OMInt( x ):
    """Return OMI node representing given integer"""
    omelt = Element("OMI")
    omelt.text = str(x)
    return omelt

#
# OpenMath float (OMF)
#
def OMFloat( x ):
    """Returns OMF node representing given float"""
    omelt = Element("OMF")
    omelt.attrib = { 'dec' : str(x) }
    return omelt

#
# OpenMath string (OMSTR)
#
def OMSTRing( x ):
    """Returns OMSTR node representing given string"""
    omelt = Element("OMSTR")
    omelt.text = x
    return omelt

################################################################
#
# True/False (logic1.true, logic1.false)
#
def OMBool( x ):
    """Returns OMS node representing given boolean"""
    omelt = Element("OMS")
    omelt.attrib = { 'cd' : 'logic1', 'name' : str(x).lower() }
    return omelt

################################################################
#
# List (list1.list)
#
def OMList( x ):
    """Returns an OMA node containing the OM 
    encoding for the given list"""
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = { 'cd' : 'list1', 'name' : 'list' }
    omelt.append(oms)
    for t in x: 
        omelt.append(OMelement(t))
    return omelt

################################################################
#
# Complex (complex1.complex_cartesian)
#
def OMComplex( x ):
    """Returns an OMA node containing the OM encoding
     for the given complex number"""
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = { 'cd' : 'complex1', 'name' : 'complex_cartesian'}
    omareal = OMelement(x.real)
    omaimag = OMelement(x.imag)
    omelt.append(oms)
    omelt.append(omareal)
    omelt.append(omaimag)
    return omelt

################################################################
#
# Dictionary (dict1.dictionary) (Easy level extension)
#
def OMDict( x ):
    """Returns the OMA node representing the given Python 
    dictionary, using a custom OM Content Dictionary"""
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'dict1', 'name' : 'dictionary'}
    omelt.append(oms)
    for i in x.values():
        omelt.append(OMelement(i))
    return omelt

################################################################
#
# Matrix (linalg2.matrix) (Medium to Hard level extension)
# Decides if param is a matrix or just a python list
#
def OMMatrix( x ):
    """Returns either OM encoding to represent a matrix or a list"""
    if(type(x[0]) == list):
        length = len(x[0])
    for g in x:
        if(type(g) != list):
            return OMList(x)
        elif(len(g) != length):
            return OMList(x)
        elif(not all(isinstance(i, (int, float)) for i in g)):
            return OMList(x)
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'linalg2', 'name' : 'matrix'}
    omelt.append(oms)
    for y in x:
        oma = Element("OMA")
        omsx = Element("OMS")
        omsx.attrib = {'cd' : 'linalg2', 'name' : 'matrixrow'}
        oma.append(omsx)
        for z in y:
            oma.append(OMelement(z))
        omelt.append(oma)
    return omelt

################################################################
#
# Attributions - Hard level Extension
#
def OMAttr( x ):
    """Returns a OMATTR node, representing the given Attribution object"""
    omelt = Element("OMATTR")
    omatp = Element("OMATP")
    for i in x.attrPair:
        if(not type(i) == types.FunctionType):
            omatp.append(PyElementHandler[type(i)](i))
        for cd, dic in omdicts.items():
            for name, value in dic.items():
                if(i == value):
                    oms = Element("OMS")
                    oms.attrib = {'cd' : cd, 'name' : name}
                    omatp.append(oms)
    omelt.append(omatp)
    omelt.append(PyElementHandler[type(x.deriv)](x.deriv))
    return omelt


################################################################
#
# OMelement
#
# Generates OM encoding dependant on type of given object
#
PyElementHandler = { int : OMInt, list : OMMatrix, float : OMFloat, str : OMSTRing, bool : OMBool, complex : OMComplex, dict : OMDict, objects.Attribution : OMAttr }

def OMelement( x ):
    """Returns the xml tree representing the given Python object"""
    if(type(x) in PyElementHandler):
        return PyElementHandler[type(x)](x)
    else:
        print("Cannot encode to OpenMath format!\n")

################################################################
#
# OMobject
#
# Wraps OpenMath encoding for x into OpenMath object
#
def OMobject( x ):
    """Returns an OMOBJ node representing the given Python object"""
    omobj = Element("OMOBJ")
    omobj.insert(1,OMelement(x))
    return omobj

################################################################

