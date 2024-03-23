# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56673753/nameerror-name-fh-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from netCDF4 import Dataset
    _l_(666603)

except ImportError:
    pass
try:
    import numpy as np
    _l_(666605)

except ImportError:
    pass
my_example_nc_file = r'''\D:\UoR\Practice data\cru10min30_tmp.nc'
fh = (my_example_nc_file, mode='r')'''
_l_(666606)
lons = _a_(666608, _n_(666607, "fh", lambda: fh), "variables")['lon'][:]
_l_(666609)
lats = _a_(666611, _n_(666610, "fh", lambda: fh), "variables")['lat'][:]
_l_(666612)
tmax = _a_(666614, _n_(666613, "fh", lambda: fh), "variables")['Tmax'][:]
_l_(666615)
tmax_units = _a_(666618, _a_(666617, _n_(666616, "fh", lambda: fh), "variables")['Tmax'], "units")
_l_(666619)