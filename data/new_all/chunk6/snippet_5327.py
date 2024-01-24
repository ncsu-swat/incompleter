# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66995341/typeerror-cannot-unpack-non-iterable-int-object-when-i-tried-to-attend-the-le
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
D = _c_(348553, _n_(348550, "calculate_distances", lambda: calculate_distances), _n_(348551, "x", lambda: x),_n_(348552, "y", lambda: y))
_l_(348554)

fig = _c_(348557, _a_(348556, _n_(348555, "plt", lambda: plt), "figure"), figsize=(6,6));
_l_(348558)
total_distance = 0
_l_(348559)
for i in _c_(348562, _n_(348560, "range", lambda: range), _n_(348561, "n_city", lambda: n_city)-1):
    _l_(348603)

    _c_(348567, _a_(348564, _n_(348563, "plt", lambda: plt), "scatter"), _n_(348565, "x", lambda: x),_n_(348566, "y", lambda: y),marker="s",c="k");
    _l_(348568)
    _c_(348581, _a_(348570, _n_(348569, "plt", lambda: plt), "plot"), [_n_(348571, "x", lambda: x)[_n_(348572, "i", lambda: i)],_n_(348573, "x", lambda: x)[_n_(348574, "i", lambda: i)+1]], [_n_(348575, "y", lambda: y)[_n_(348576, "i", lambda: i)],_n_(348577, "y", lambda: y)[_n_(348578, "i", lambda: i)+1]],
             alpha=(_n_(348579, "i", lambda: i)+1)/_n_(348580, "n_city", lambda: (n_city)),lw=2,color="k");
    _l_(348582)
    total_distance += _n_(348583, "D", lambda: D)[_n_(348584, "i", lambda: i),_n_(348585, "i", lambda: i)+1]
    _l_(348586)
    _c_(348590, _a_(348588, _n_(348587, "plt", lambda: plt), "title"), "Distance traveled = %0.3f" %_n_(348589, "total_distance", lambda: total_distance))
    _l_(348591)
    _c_(348594, _a_(348593, _n_(348592, "time", lambda: time), "sleep"), 1.0)  
    _l_(348595)  
    _c_(348597, _n_(348596, "clear_output", lambda: clear_output), wait = True)
    _l_(348598)
    _c_(348601, _n_(348599, "display", lambda: display), _n_(348600, "fig", lambda: fig)) # Reset display
    _l_(348602) # Reset display