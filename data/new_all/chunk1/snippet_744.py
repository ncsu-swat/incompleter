# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63007486/pywinauto-typeerror-item-2-in-argtypes-passes-a-union-by-value-which-is-unsu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pywinauto.application import Application
    _l_(396864)

except ImportError:
    pass
app = _c_(396868, _a_(396867, _c_(396866, _n_(396865, "Application", lambda: Application), backend="uia"), "start"), "thinkorswim.exe")
_l_(396869)