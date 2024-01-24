# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59225923/attribute-error-white-extracting-column-from-a-csv-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(663691)

except ImportError:
    pass
try:
    from astropy.table import Table
    _l_(663693)

except ImportError:
    pass

#reading the data from the dataset file
data=_c_(663696, _a_(663695, _n_(663694, "pd", lambda: pd), "read_csv"), 'winequality-red.csv',sep=',')
_l_(663697)

#Declaring a class named as One
class One:
    _l_(663714)

    def __init__(self):
        _l_(663713)

        # Assigning the value that are less than 11 in
        # the data set to the value data_lessthan11
        data_lessthan11 = _a_(663699, _n_(663698, "data", lambda: data), "loc")[(_a_(663701, _n_(663700, "data", lambda: data), "quality")<11)]
        _l_(663702)

        # Assigning the filtered value from the data_less
        # than11(which consists of values less than 11)
        # which is greater than 5
        _n_(663703, "self", lambda: self).data_greaterthan5 = _a_(663705, _n_(663704, "data", lambda: data), "loc")[(_a_(663707, _n_(663706, "data_lessthan11", lambda: data_lessthan11), "quality")>5)]
        _l_(663708)
        _c_(663711, _n_(663709, "print", lambda: print), _n_(663710, "data_lessthan11", lambda: data_lessthan11))
        _l_(663712)

#declaring an object for the class One
one = _c_(663716, _n_(663715, "One", lambda: One))
_l_(663717)

# assigning the whole value from the class one into
# size_One to recall it outside the class
size_One = _a_(663719, _n_(663718, "one", lambda: one), "data_greaterthan5")
_l_(663720)

_c_(663723, _n_(663721, "print", lambda: print), _n_(663722, "size_One", lambda: size_One))
_l_(663724)