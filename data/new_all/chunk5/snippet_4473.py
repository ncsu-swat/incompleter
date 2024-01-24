# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57053149/typeerror-list-indices-must-be-integers-or-slices-not-str-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(663814)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(663816)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(663818)

except ImportError:
    pass
new_df=[]
_l_(663819)
temp_cols=['Hour','Minute','Second','x_second','RTD_sensor']
_l_(663820)
### Set your path to the folder containing the .csv files
PATH = 'C:\\Users\\UserName\\Documents\\python\\NASA\\FEMTOBearingDataSet\\Training_set\\Bearing1_1\\temp\\' # Use your path
_l_(663821) # Use your path

### Fetch all files in path
fileNames = _c_(663825, _a_(663823, _n_(663822, "os", lambda: os), "listdir"), _n_(663824, "PATH", lambda: PATH))
_l_(663826)

### Filter file name list for files ending with .csv
fileNames = [_n_(663827, "file", lambda: file) for file in _n_(663828, "fileNames", lambda: fileNames) if '.csv' in _n_(663829, "file", lambda: file)]
_l_(663830)

### Loop over all files
for file in _n_(663831, "fileNames", lambda: fileNames):
    _l_(663854)


    ### Read .csv file and append to list
    df = _c_(663837, _a_(663833, _n_(663832, "pd", lambda: pd), "read_csv"), _n_(663834, "PATH", lambda: PATH) + _n_(663835, "file", lambda: file), sep=',', header=None, names=_n_(663836, "temp_cols", lambda: temp_cols), index_col = None)
    _l_(663838)
    for column in _c_(663843, _n_(663839, "range", lambda: range), 0,_c_(663842, _n_(663840, "len", lambda: len), _n_(663841, "temp_cols", lambda: temp_cols))):
        _l_(663853)

        _c_(663851, _a_(663845, _n_(663844, "new_df", lambda: new_df)['Mean'], "append"), _c_(663850, _a_(663849, _a_(663847, _n_(663846, "df", lambda: df), "iloc")[:,_n_(663848, "column", lambda: column)], "mean")))
        _l_(663852)

_c_(663857, _a_(663856, _n_(663855, "new_df", lambda: new_df), "head"))
_l_(663858)