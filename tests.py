import openmath
from openmath import *

################################################################
#
# Tests basic requirements
#

a = 42
if(a == ParseOMstring(OMstring(a))):
	print('integer test PASSED')
else:
	print('integer test FAILED')

a = [1,2,3]
if(a == ParseOMstring(OMstring(a))):
	print('list test PASSED')
else:
	print('list test FAILED')

a = [1,2,[3,4,5]]
if(a == ParseOMstring(OMstring(a))):
	print('nested list test PASSED')
else:
	print('nested list test FAILED')

a = 1.0
if(a == ParseOMstring(OMstring(a))):
	print('float test PASSED')
else:
	print('float test FAILED')

a = 'this is a string'
if(a == ParseOMstring(OMstring(a))):
	print('string test PASSED')
else:
	print('string test FAILED')

a = True
if(a == ParseOMstring(OMstring(a))):
	print('boolean test PASSED')
else:
	print('boolean test FAILED')

a = 1.5 + 3.3j
if(a == ParseOMstring(OMstring(a))):
	print('complex number test PASSED')
else:
	print('complex number test FAILED')

a = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if(ParseOMfile('tst/range.xml') == a):
	print('integer interval test PASSED')
else:
	print('integer interval test FAILED')

a = [[1, 2, 3], [42, 5, 6], [0, -1, -100]]
if(ParseOMfile('tst/matrix.xml') == a):
	print('matrix test PASSED')
else:
	print('matrix test FAILED')

################################################################
#
# Tests on attribution object
#
a = ParseOMfile('tst/omattr.xml')
if(a.deriv == 3628800 and a.attrPair[1] == 10 and a.attrPair[0] == oms_integer1_factorial):
	print('attributions test PASSED')
else:
	print('attributions test FAILED')

################################################################
#
# Some tests on arith1 CD
#

a = 6
if(ParseOMfile('tst/divide.xml') == a):
	print('division test PASSED')
else:
	print('division test FAILED')

if(ParseOMfile('tst/gcd.xml') == a):
	print('gcd test PASSED')
else:
	print('gcd test FAILED')

a = 78
if(ParseOMfile('tst/plus.xml') == a):
	print('plus test PASSED')
else:
	print('plus test FAILED')

a = 2.0
if(ParseOMfile('tst/root.xml') == a):
	print('root test PASSED')
else:
	print('root test FAILED')

