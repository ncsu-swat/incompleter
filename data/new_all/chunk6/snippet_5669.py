# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73316878/nameerror-name-s-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import scipy.stats
    _l_(358324)

except ImportError:
    pass
try:
    from numpy import sqrt, log, exp, pi
    _l_(358326)

except ImportError:
    pass

N = _a_(358329, _a_(358328, _a_(358327, scipy, "stats"), "norm"), "cdf")
_l_(358330)
d1 = (_c_(358334, _n_(358331, "log", lambda: log), _n_(358332, "S", lambda: S)/_n_(358333, "K", lambda: K)) + (_n_(358335, "r", lambda: r)+_n_(358336, "sigma", lambda: sigma)**2/2)*_n_(358337, "t", lambda: t)) / (_n_(358338, "sigma", lambda: sigma)*_c_(358341, _n_(358339, "sqrt", lambda: sqrt), _n_(358340, "t", lambda: t)))
_l_(358342)
d2 = _n_(358343, "d1", lambda: d1) - _n_(358344, "sigma", lambda: sigma) * _c_(358347, _n_(358345, "sqrt", lambda: sqrt), _n_(358346, "t", lambda: t))
_l_(358348)

def bs_price(c_p, S, K, r, t, sigma):
    _l_(358380)

    if _n_(358349, "c_p", lambda: c_p) == 'c':
        _l_(358379)

        aux = _c_(358352, _n_(358350, "N", lambda: N), _n_(358351, "d1", lambda: d1)) * _n_(358353, "S", lambda: S) - _c_(358356, _n_(358354, "N", lambda: N), _n_(358355, "d2", lambda: d2)) * _n_(358357, "K", lambda: K) * _c_(358361, _n_(358358, "exp", lambda: exp), -_n_(358359, "r", lambda: r)*_n_(358360, "t", lambda: t))
        _l_(358362)
        return aux
    elif _n_(358363, "c_p", lambda: c_p) == 'p':
        _l_(358378)

        aux = _c_(358366, _n_(358364, "N", lambda: N), -_n_(358365, "d2", lambda: d2)) * _n_(358367, "K", lambda: K) * _c_(358371, _n_(358368, "exp", lambda: exp), -_n_(358369, "r", lambda: r)*_n_(358370, "t", lambda: t)) - _c_(358374, _n_(358372, "N", lambda: N), -_n_(358373, "d1", lambda: d1)) * _n_(358375, "S", lambda: S)
        _l_(358376)
        return aux
    else:
        aux = "Please specify call or put options."
        _l_(358377)
        return aux

MAX_TRY = 1000
_l_(358381)
def find_iv_newton(c_p, S, K, r, t, market_price):
    _l_(358419)

    _sigma = 0.5
    _l_(358382)
    for i in _c_(358385, _n_(358383, "range", lambda: range), _n_(358384, "MAX_TRY", lambda: MAX_TRY)):
        _l_(358416)

        _bs_price = _c_(358393, _n_(358386, "bs_price", lambda: bs_price), _n_(358387, "c_p", lambda: c_p), _n_(358388, "S", lambda: S), _n_(358389, "K", lambda: K), _n_(358390, "r", lambda: r), _n_(358391, "t", lambda: t), sigma=_n_(358392, "_sigma", lambda: _sigma))
        _l_(358394)
        diff = _n_(358395, "market_price", lambda: market_price) - _n_(358396, "_bs_price", lambda: _bs_price)
        _l_(358397)
        vega = _n_(358398, "S", lambda: S)*_c_(358401, _n_(358399, "N_prime", lambda: N_prime), _n_(358400, "d1", lambda: d1))*_c_(358404, _n_(358402, "sqrt", lambda: sqrt), _n_(358403, "t", lambda: t))
        _l_(358405)
        if _c_(358408, _n_(358406, "abs", lambda: abs), _n_(358407, "diff", lambda: diff)) < _n_(358409, "ONE_CENT", lambda: ONE_CENT):
            _l_(358412)

            aux = _n_(358410, "_sigma", lambda: _sigma)
            _l_(358411)
            return aux
        _sigma += _n_(358413, "diff", lambda: diff)/_n_(358414, "vega", lambda: vega)
        _l_(358415)
    aux = _n_(358417, "_sigma", lambda: _sigma)
    _l_(358418)
    return aux