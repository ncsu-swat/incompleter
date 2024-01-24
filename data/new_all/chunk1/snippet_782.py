# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53402504/cant-loop-the-distance-between-two-locations-typeerror-numpy-float64-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(406725)

except ImportError:
    pass
try:
    import numpy as np
    _l_(406727)

except ImportError:
    pass
try:
    from pandas import DataFrame
    _l_(406729)

except ImportError:
    pass

Data = _c_(406732, _a_(406731, _n_(406730, "pd", lambda: pd), "read_csv"), '/home/aziz/Desktop/langlat.csv')
_l_(406733)
data = _c_(406737, _a_(406735, _n_(406734, "pd", lambda: pd), "DataFrame"), _n_(406736, "Data", lambda: Data))
_l_(406738)
lat1 = _n_(406739, "data", lambda: data)['Lattude'][2:]
_l_(406740)
lat = _c_(406747, _a_(406742, _n_(406741, "pd", lambda: pd), "DataFrame"), _c_(406746, _a_(406744, _n_(406743, "np", lambda: np), "array"), _n_(406745, "lat1", lambda: lat1)))
_l_(406748)
lang1 = _n_(406749, "data", lambda: data)['Langitude'][2:]
_l_(406750)
lang = _c_(406757, _a_(406752, _n_(406751, "pd", lambda: pd), "DataFrame"), _c_(406756, _a_(406754, _n_(406753, "np", lambda: np), "array"), _n_(406755, "lang1", lambda: lang1)))
_l_(406758)
try:
    import geopy.distance
    _l_(406760)

except ImportError:
    pass


for i in _c_(406765, _n_(406761, "range", lambda: range), _c_(406764, _n_(406762, "len", lambda: len), _n_(406763, "lat", lambda: lat))):
    _l_(406799)

    for j in _c_(406770, _n_(406766, "range", lambda: range), _c_(406769, _n_(406767, "len", lambda: len), _n_(406768, "lat", lambda: lat))):
        _l_(406798)

        coords_1 = (_c_(406774, _n_(406771, "all", lambda: all), _n_(406772, "lat", lambda: lat)[0][_n_(406773, "i", lambda: i)]), _c_(406778, _n_(406775, "all", lambda: all), _n_(406776, "lang", lambda: lang)[0][_n_(406777, "i", lambda: i)]))
        _l_(406779)
        coords_2 = (_c_(406783, _n_(406780, "all", lambda: all), _n_(406781, "lat", lambda: lat)[0][_n_(406782, "j", lambda: j)]), _c_(406787, _n_(406784, "all", lambda: all), _n_(406785, "lang", lambda: lang)[0][_n_(406786, "j", lambda: j)]))
        _l_(406788)
        _c_(406796, _n_(406789, "print", lambda: print), _a_(406795, _c_(406794, _a_(406791, _a_(406790, geopy, "distance"), "distance"), _n_(406792, "coords_1", lambda: coords_1), _n_(406793, "coords_2", lambda: coords_2)), "km"))
        _l_(406797)