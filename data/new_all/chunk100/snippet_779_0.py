# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_dictionary(colors, r_id):
    _l_(78648)

    _n_(78638, "colors", lambda: colors)[:] = [_n_(78639, "d", lambda: d) for d in _n_(78640, "colors", lambda: colors) if _c_(78643, _a_(78642, _n_(78641, "d", lambda: d), "get"), 'id') != _n_(78644, "r_id", lambda: r_id)]
    _l_(78645)
    aux = _n_(78646, "colors", lambda: colors)
    _l_(78647)
    return aux
colors = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
_l_(78649)
_c_(78651, _n_(78650, "print", lambda: print), 'Original list of dictionary:')
_l_(78652)
_c_(78655, _n_(78653, "print", lambda: print), _n_(78654, "colors", lambda: colors))
_l_(78656)
_c_(78659, _n_(78657, "print", lambda: print), '\nRemove id', _n_(78658, "r_id", lambda: r_id), 'from the said list of dictionary:')
_l_(78660)
_c_(78666, _n_(78661, "print", lambda: print), _c_(78665, _n_(78662, "remove_dictionary", lambda: remove_dictionary), _n_(78663, "colors", lambda: colors), _n_(78664, "r_id", lambda: r_id)))
_l_(78667)