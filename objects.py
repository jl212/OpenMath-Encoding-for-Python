################################################################
#
# Objects used to represent OM encoding
#

class Attribution:
    """ Stores an attribution equal to a OMATTR node """
    def __init__(self, attrPair, deriv):
        self.attrPair = attrPair
        self.deriv = deriv

    def __str__(self):
        return "%s can be observed from %s" % (self.deriv, self.attrPair)

