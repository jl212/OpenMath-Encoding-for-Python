################################################################
#
# Parsing OpenMath objects
# 
import operator

import math
from math import exp, log

import fractions
from fractions import gcd

import string
from string import ascii_letters

import objects
from objects import *

################################################################
#
# Basic OpenMath elements
#

# OpenMath integer
def ParseOMI(node):
    """Returns the inner text of an OMI node as a Python int"""
    return int(node.text)

# OpenMath float
def ParseOMF(node):
    """Returns the 'dec' attribute of an OMF node as 
    a Python float"""
    return float(node.get('dec'))

# OpenMath string
def ParseOMSTR(node):
    """Returns the inner text of an OMSTR node"""
    return node.text
    

################################################################
#
# OpenMath content dictionaries
#
omdicts = {}

# list1    http://www.openmath.org/cd/list1.xhtml
omdicts['list1'] = {}

# list1.list
def oms_list1_list(list):
    """Returns the given list parameter"""
    return list

omdicts['list1']['list'] = oms_list1_list

#nums1
omdicts['nums1'] = {}

#nums1.rational
def oms_nums1_rational(list):
    """Calculates the float representation of the given rational number"""
    return list[0]/list[1]

omdicts['nums1']['rational'] = oms_nums1_rational

# logic1	http://www.openmath.org/cd/logic1.xhtml
omdicts['logic1'] = {}

# logic1.true
omdicts['logic1']['true'] = True

#logic1.false
omdicts['logic1']['false'] = False

#complex1
omdicts['complex1'] = {}

#complex1.complex_cartesian
def oms_complex1_complex_cartesian(list):
    """Returns a Python complex number object"""
    return complex(list[0], list[1])

omdicts['complex1']['complex_cartesian'] = oms_complex1_complex_cartesian

#interval1
omdicts['interval1'] = {}

#interval1.integer_interval
def oms_interval1_integer_interval(list_param):
    """Returns a list representation of the given interval"""
    return list(range(list_param[0], list_param[1]+1))

omdicts['interval1']['integer_interval'] = oms_interval1_integer_interval

#linalg2
omdicts['linalg2'] = {}

#linalg2.matrix
def oms_linalg2_matrix(list):
    """Returns the given list paramater"""
    return list

omdicts['linalg2']['matrix'] = oms_linalg2_matrix

#linalg2.matrixrow
omdicts['linalg2']['matrixrow'] = oms_linalg2_matrix

################################################################
#
# Content dictionary for Python Dictionaries - easy level extension
#

#dict1
omdicts['dict1'] = {}

#dict1.dictionary
def oms_dict1_dictionary(list):
    """Returns a python dictionary with the parameters as the values and arbitrary keys"""
    dicts = {}
    key = 0
    for i in list:
        dicts[ascii_letters[key]] = i
        key += 1
    return dicts

omdicts['dict1']['dictionary'] = oms_dict1_dictionary

################################################################
#
# Arith1 content dictionary - medium level extension
#

#arith1
omdicts['arith1'] = {}

#arith1.gcd
def oms_arith1_gcd(list):
    """Calculates the Greatest Common Divisor from the two given integers"""
    return gcd(list[0], list[1])

omdicts['arith1']['gcd'] = oms_arith1_gcd

#arith1.lcd
def oms_arith1_lcm(list):
    """Calculates the lowest common multiple from the two given integers"""
    return (list[0] * list[1]) / oms_arith1_gcd(list)

omdicts['arith1']['lcm'] = oms_arith1_lcm

#arith1.plus
def oms_arith1_plus(list):
    """Calulcates the sum of all elements in the list"""
    total = 0
    for i in list:
        total += i
    return total

omdicts['arith1']['plus'] = oms_arith1_plus

#arith1.minus
def oms_arith1_minus(list):
    """Calculates the result of all the elements in the list subtracted"""
    total = 0
    for i in list:
        total -= i
    return total

omdicts['arith1']['minus'] = oms_arith1_minus

#arith1.unary_minus
def oms_arith1_unary_minus(arg):
    """Returns the negation of the given integer"""
    if isinstance(arg, list):
        return (-list[0])
    else:
        return -arg

omdicts['arith1']['unary_minus'] = oms_arith1_unary_minus

#arith1.times
def oms_arith1_times(list):
    """Calculates the product of all the elements in the list"""
    total = 1
    for i in list:
        total *= i
    return total

omdicts['arith1']['times'] = oms_arith1_times

#arith1.divide
def oms_arith1_divide(list):
    """Returns the result from the division of two numbers"""
    return list[0] / list[1]

omdicts['arith1']['divide'] = oms_arith1_divide

#arith1.power
def oms_arith1_power(list):
    """Calculates the power of one number to another"""
    if(type(list[1]) == int):
        return list[0] ** list[1]
    else:
        return exp(list[1] * log(list[0]))

omdicts['arith1']['power'] = oms_arith1_power

#arith1.abs
def oms_arith1_abs(arg):
    """Returns the absolute values of a number"""
    if isinstance(arg, list):
        return abs(list[0])
    else:
        return abs(arg)

omdicts['arith1']['abs'] = oms_arith1_abs

#arith1.root
def oms_arith1_root(list):
    """Returns the given root of a number"""
    return exp(log(list[0])/list[1])

omdicts['arith1']['root'] = oms_arith1_root

#arith1.sum
def oms_arith1_sum(list):
    """Represents the sum of a function applied over a given interval"""
    total = 0
    for i in list[0]:
        total += list[1](i)
    return total

omdicts['arith1']['sum'] = oms_arith1_sum

#arith1.product
def oms_arith1_product(list):
    """Represents the product of a function applied over a given interval"""
    total = 1
    for i in list[0]:
        total *= list[1](i)
    return total

omdicts['arith1']['product'] = oms_arith1_product

################################################################
#
# Factorial - Medium Extension
#

#integer1
omdicts['integer1'] = {}

#integer1.factorial
def oms_integer1_factorial(list):
    """Calculates the factorial of a number"""
    if(type(list) == int):
        x = list
    else:
        x = list[0]
    y = x
    while (x > 1):
        y = y * (x - 1)
        x -= 1
    return y

omdicts['integer1']['factorial'] = oms_integer1_factorial

################################################################
#
# Attributions - Hard level Extension
#

def ParseOMATTR(node):
    """Parses a OMATTR node and returns an Attribution object"""
    attr = ParseOMelement(node[0])
    attr.deriv = ParseOMelement(node[1])
    return attr

def ParseOMATP(node):
    """Parses a OMATP node and generates an Attribution object"""
    omatp = []
    for child in node.findall("*"):
        omatp.append(ParseOMelement(child))
    a = Attribution(omatp, 0)
    return a

################################################################

def ParseOMS(node):
    """Returns a function object from the OM CDs"""
    return omdicts[ node.get('cd') ][ node.get('name') ]

def ParseOMA(node):
    """Parses an OM application to get a Python object representation"""
    elts = []
    for child in node.findall("*"):
        elts.append( ParseOMelement(child) )
    # now the first element of 'elts' is a function to be applied to the rest of the list
    return elts[0](elts[1:len(elts)]) 

ParseOMelementHandler = { 'OMI' : ParseOMI, 'OMS' : ParseOMS, 'OMA' : ParseOMA,
 'OMF' : ParseOMF, 'OMSTR' : ParseOMSTR, 'OMATTR' : ParseOMATTR, 'OMATP' : ParseOMATP }

def ParseOMelement(obj):
    """Returns a Python representation of the given node"""
    return ParseOMelementHandler[obj.tag](obj)

def ParseOMroot(root):
    """Returns the Python representation of the given node"""
    return ParseOMelement(root[0])


################################################################
