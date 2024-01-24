# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55587722/stuck-with-typeerror-cannot-compare-types-ndarraydtype-object-and-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
cols = ['Keyword']
_l_(694537)

for col in _n_(694538, "cols", lambda: cols):
    _l_(694548)

    val = _c_(694542, _a_(694541, _n_(694539, "df_ch", lambda: df_ch)[_n_(694540, "col", lambda: col)], "value_counts"))
    _l_(694543)
    y = _a_(694546, _n_(694544, "val", lambda: val)[_n_(694545, "val", lambda: val) < 10000], "index")
    _l_(694547)

_n_(694549, "df_ch", lambda: df_ch)[_n_(694550, "col", lambda: col)] = _c_(694556, _a_(694553, _n_(694551, "df_ch", lambda: df_ch)[_n_(694552, "col", lambda: col)], "replace"), {_n_(694554, "x", lambda: x):'other' for x in _n_(694555, "y", lambda: y)})
_l_(694557)