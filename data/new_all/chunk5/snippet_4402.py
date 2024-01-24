# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58420941/pandas-typeerror-list-indices-must-be-integers-or-slices-not-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(662409)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(662411)

except ImportError:
    pass
try:
    import csv
    _l_(662413)

except ImportError:
    pass
try:
    import os
    _l_(662415)

except ImportError:
    pass
try:
    from scipy.interpolate import interp1d
    _l_(662417)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(662419)

except ImportError:
    pass
try:
    import glob
    _l_(662421)

except ImportError:
    pass

user_info=[19,20,21,22,23] #number of charge states analyzed using fit.py 
_l_(662422) #number of charge states analyzed using fit.py 


path = r'C:\Users\my_folder' # use your path
_l_(662423) # use your path
all_files = _c_(662427, _a_(662425, _n_(662424, "glob", lambda: glob), "glob"), _n_(662426, "path", lambda: path) + "/*.csv")
_l_(662428)

data = []
_l_(662429)

for filename in _n_(662430, "all_files", lambda: all_files):
    _l_(662441)

    df = _c_(662434, _a_(662432, _n_(662431, "pd", lambda: pd), "read_csv"), _n_(662433, "filename", lambda: filename), index_col=None, header=0)
    _l_(662435)
    _c_(662439, _a_(662437, _n_(662436, "data", lambda: data), "append"), _n_(662438, "df", lambda: df))
    _l_(662440)

my_x=_a_(662443, _n_(662442, "data", lambda: data)[0], "iloc")[2:,0] #assuming that all the files have the same list of x for all data(1~200)
_l_(662444) #assuming that all the files have the same list of x for all data(1~200)

my_y=[]
_l_(662445)
for filenumber in _c_(662450, _n_(662446, "range", lambda: range), _c_(662449, _n_(662447, "len", lambda: len), _n_(662448, "all_files", lambda: all_files))):
    _l_(662461)

    _c_(662459, _a_(662452, _n_(662451, "my_y", lambda: my_y), "append"), _a_(662455, _n_(662453, "data", lambda: data)[_n_(662454, "filenumber", lambda: filenumber)], "iloc")[2:,1:_c_(662458, _n_(662456, "len", lambda: len), _n_(662457, "user_info", lambda: user_info))+1])
    _l_(662460)