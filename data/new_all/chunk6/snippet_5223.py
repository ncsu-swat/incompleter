# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55391144/in-what-way-can-i-debug-this-attribute-error-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(353008)

except ImportError:
    pass

data = _c_(353011, _a_(353010, _n_(353009, "pd", lambda: pd), "read_csv"), "China_FDIGDP.csv")
_l_(353012)

data1 = _c_(353015, _a_(353014, _n_(353013, "data", lambda: data), "dropna"))
_l_(353016)
_c_(353019, _a_(353018, _n_(353017, "data1", lambda: data1), "to_csv"), "data1.csv", index = False)
_l_(353020)

Data  = _c_(353023, _a_(353022, _n_(353021, "pd", lambda: pd), "read_csv"), "data1.csv")
_l_(353024)

_c_(353027, _n_(353025, "print", lambda: print), _n_(353026, "Data", lambda: Data))
_l_(353028)

x = _c_(353032, _a_(353031, _a_(353030, _n_(353029, "pd", lambda: pd), "Data")["GDP"], "values"))
_l_(353033)
y = _c_(353037, _a_(353036, _a_(353035, _n_(353034, "pd", lambda: pd), "Data")["FDI_net_in"], "values"))
_l_(353038)