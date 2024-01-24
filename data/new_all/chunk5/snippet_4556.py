# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55587722/stuck-with-typeerror-cannot-compare-types-ndarraydtype-object-and-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
cols = ['Keyword']
_l_(664338)

for col in _n_(664339, "cols", lambda: cols):
    _l_(664349)

    val = _c_(664343, _a_(664342, _n_(664340, "df_ch", lambda: df_ch)[_n_(664341, "col", lambda: col)], "value_counts"))
    _l_(664344)
    y = _a_(664347, _n_(664345, "val", lambda: val)[_n_(664346, "val", lambda: val) < 10000], "index")
    _l_(664348)

_n_(664350, "df_ch", lambda: df_ch)[_n_(664351, "col", lambda: col)] = _c_(664357, _a_(664354, _n_(664352, "df_ch", lambda: df_ch)[_n_(664353, "col", lambda: col)], "replace"), {_n_(664355, "x", lambda: x):'other' for x in _n_(664356, "y", lambda: y)})
_l_(664358)