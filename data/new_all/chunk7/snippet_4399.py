# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58420941/pandas-typeerror-list-indices-must-be-integers-or-slices-not-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(684222)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(684224)

except ImportError:
    pass
try:
    import csv
    _l_(684226)

except ImportError:
    pass
try:
    import os
    _l_(684228)

except ImportError:
    pass
try:
    from scipy.interpolate import interp1d
    _l_(684230)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(684232)

except ImportError:
    pass
try:
    import glob
    _l_(684234)

except ImportError:
    pass

user_info=[19,20,21,22,23] #number of charge states analyzed using fit.py 
_l_(684235) #number of charge states analyzed using fit.py 


path = r'C:\Users\my_folder' # use your path
_l_(684236) # use your path
all_files = _c_(684240, _a_(684238, _n_(684237, "glob", lambda: glob), "glob"), _n_(684239, "path", lambda: path) + "/*.csv")
_l_(684241)

data = []
_l_(684242)

for filename in _n_(684243, "all_files", lambda: all_files):
    _l_(684254)

    df = _c_(684247, _a_(684245, _n_(684244, "pd", lambda: pd), "read_csv"), _n_(684246, "filename", lambda: filename), index_col=None, header=0)
    _l_(684248)
    _c_(684252, _a_(684250, _n_(684249, "data", lambda: data), "append"), _n_(684251, "df", lambda: df))
    _l_(684253)

my_x=_a_(684256, _n_(684255, "data", lambda: data)[0], "iloc")[2:,0] #assuming that all the files have the same list of x for all data(1~200)
_l_(684257) #assuming that all the files have the same list of x for all data(1~200)

my_y=[]
_l_(684258)
for filenumber in _c_(684263, _n_(684259, "range", lambda: range), _c_(684262, _n_(684260, "len", lambda: len), _n_(684261, "all_files", lambda: all_files))):
    _l_(684274)

    _c_(684272, _a_(684265, _n_(684264, "my_y", lambda: my_y), "append"), _a_(684268, _n_(684266, "data", lambda: data)[_n_(684267, "filenumber", lambda: filenumber)], "iloc")[2:,1:_c_(684271, _n_(684269, "len", lambda: len), _n_(684270, "user_info", lambda: user_info))+1])
    _l_(684273)