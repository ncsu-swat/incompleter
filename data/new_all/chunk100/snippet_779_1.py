# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_dictionary(colors, r_id):
    _l_(78678)

    _n_(78668, "colors", lambda: colors)[:] = [_n_(78669, "d", lambda: d) for d in _n_(78670, "colors", lambda: colors) if _c_(78673, _a_(78672, _n_(78671, "d", lambda: d), "get"), 'id') != _n_(78674, "r_id", lambda: r_id)]
    _l_(78675)
    aux = _n_(78676, "colors", lambda: colors)
    _l_(78677)
    return aux
_c_(78680, _n_(78679, "print", lambda: print), 'Original list of dictionary:')
_l_(78681)
_c_(78684, _n_(78682, "print", lambda: print), _n_(78683, "colors", lambda: colors))
_l_(78685)
r_id = '#FF0000'
_l_(78686)
_c_(78689, _n_(78687, "print", lambda: print), '\nRemove id', _n_(78688, "r_id", lambda: r_id), 'from the said list of dictionary:')
_l_(78690)
_c_(78696, _n_(78691, "print", lambda: print), _c_(78695, _n_(78692, "remove_dictionary", lambda: remove_dictionary), _n_(78693, "colors", lambda: colors), _n_(78694, "r_id", lambda: r_id)))
_l_(78697)