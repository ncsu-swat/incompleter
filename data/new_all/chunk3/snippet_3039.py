# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52197977/issue-in-passing-an-array-to-an-index-in-series-objecttypeerror-len-of-unsiz
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
univals = _c_(568595, _n_(568593, "set", lambda: set), _n_(568594, "a", lambda: a))
_l_(568596)
serObj=_c_(568599, _a_(568598, _n_(568597, "pd", lambda: pd), "Series"))
_l_(568600)

for ele in _n_(568601, "univals", lambda: univals):
    _l_(568625)

    indexfound=_c_(568606, _a_(568603, _n_(568602, "np", lambda: np), "where"), _n_(568604, "a", lambda: a) == _n_(568605, "ele", lambda: ele))
    _l_(568607)
    Xpointsfromindex=_c_(568612, _a_(568609, _n_(568608, "np", lambda: np), "take"), _n_(568610, "b", lambda: b), _n_(568611, "indexfound", lambda: indexfound))
    _l_(568613)
    serobj1=_c_(568618, _a_(568615, _n_(568614, "pd", lambda: pd), "Series"), _n_(568616, "Xpointsfromindex", lambda: Xpointsfromindex)[0],index=_n_(568617, "ele", lambda: ele))   ##error happening here
    _l_(568619)   ##error happening here
    _c_(568623, _a_(568621, _n_(568620, "serObj", lambda: serObj), "apend"), _n_(568622, "serobj1", lambda: serobj1))
    _l_(568624)
_c_(568628, _n_(568626, "print", lambda: print), _n_(568627, "serObj", lambda: serObj))
_l_(568629)