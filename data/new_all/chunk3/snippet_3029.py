# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53203046/dont-know-why-attributeerror-list-object-has-no-attribute-groupby
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df = _c_(570782, _a_(570781, _n_(570780, "pd", lambda: pd), "read_csv"), 'e:/test_csv', low_memory=False)
_l_(570783)

data1 = _c_(570788, _a_(570787, _c_(570786, _a_(570785, _n_(570784, "a", lambda: a), "groupby"), 'ta')['income'], "sum"))
_l_(570789)
_c_(570793, _a_(570792, _a_(570791, _n_(570790, "data1", lambda: data1), "plot"), "pie"), autopct='%.1f%%')
_l_(570794)

data2 = _c_(570799, _a_(570798, _c_(570797, _a_(570796, _n_(570795, "a", lambda: a), "groupby"), 'tb')['income'], "sum"))
_l_(570800)
_c_(570804, _a_(570803, _a_(570802, _n_(570801, "data2", lambda: data2), "plot"), "pie"), autopct='%.1f%%')
_l_(570805)

data3 = _c_(570810, _a_(570809, _c_(570808, _a_(570807, _n_(570806, "a", lambda: a), "groupby"), 'tc')['income'], "sum"))
_l_(570811)
_c_(570815, _a_(570814, _a_(570813, _n_(570812, "data3", lambda: data3), "plot"), "pie"), autopct='%.1f%%')
_l_(570816)

_c_(570819, _a_(570818, _n_(570817, "plt", lambda: plt), "show"))
_l_(570820)