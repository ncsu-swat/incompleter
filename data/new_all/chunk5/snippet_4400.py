# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58420941/pandas-typeerror-list-indices-must-be-integers-or-slices-not-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(686863)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(686865)

except ImportError:
    pass
try:
    import csv
    _l_(686867)

except ImportError:
    pass
try:
    import os
    _l_(686869)

except ImportError:
    pass
try:
    from scipy.interpolate import interp1d
    _l_(686871)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(686873)

except ImportError:
    pass
try:
    import glob
    _l_(686875)

except ImportError:
    pass

user_info=[19,20,21,22,23] #number of charge states analyzed using fit.py 
_l_(686876) #number of charge states analyzed using fit.py 


path = r'C:\Users\my_folder' # use your path
_l_(686877) # use your path
all_files = _c_(686881, _a_(686879, _n_(686878, "glob", lambda: glob), "glob"), _n_(686880, "path", lambda: path) + "/*.csv")
_l_(686882)

data = []
_l_(686883)

for filename in _n_(686884, "all_files", lambda: all_files):
    _l_(686895)

    df = _c_(686888, _a_(686886, _n_(686885, "pd", lambda: pd), "read_csv"), _n_(686887, "filename", lambda: filename), index_col=None, header=0)
    _l_(686889)
    _c_(686893, _a_(686891, _n_(686890, "data", lambda: data), "append"), _n_(686892, "df", lambda: df))
    _l_(686894)

my_x=_a_(686897, _n_(686896, "data", lambda: data)[0], "iloc")[2:,0] #assuming that all the files have the same list of x for all data(1~200)
_l_(686898) #assuming that all the files have the same list of x for all data(1~200)

my_y=[]
_l_(686899)
for filenumber in _c_(686904, _n_(686900, "range", lambda: range), _c_(686903, _n_(686901, "len", lambda: len), _n_(686902, "all_files", lambda: all_files))):
    _l_(686915)

    _c_(686913, _a_(686906, _n_(686905, "my_y", lambda: my_y), "append"), _a_(686909, _n_(686907, "data", lambda: data)[_n_(686908, "filenumber", lambda: filenumber)], "iloc")[2:,1:_c_(686912, _n_(686910, "len", lambda: len), _n_(686911, "user_info", lambda: user_info))+1])
    _l_(686914)