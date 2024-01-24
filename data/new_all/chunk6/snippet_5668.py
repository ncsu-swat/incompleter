# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73316878/nameerror-name-s-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import scipy.stats
    _l_(365217)

except ImportError:
    pass
try:
    from numpy import sqrt, log, exp, pi
    _l_(365219)

except ImportError:
    pass

N = _a_(365222, _a_(365221, _a_(365220, scipy, "stats"), "norm"), "cdf")
_l_(365223)
d1 = (_c_(365227, _n_(365224, "log", lambda: log), _n_(365225, "S", lambda: S)/_n_(365226, "K", lambda: K)) + (_n_(365228, "r", lambda: r)+_n_(365229, "sigma", lambda: sigma)**2/2)*_n_(365230, "t", lambda: t)) / (_n_(365231, "sigma", lambda: sigma)*_c_(365234, _n_(365232, "sqrt", lambda: sqrt), _n_(365233, "t", lambda: t)))
_l_(365235)
d2 = _n_(365236, "d1", lambda: d1) - _n_(365237, "sigma", lambda: sigma) * _c_(365240, _n_(365238, "sqrt", lambda: sqrt), _n_(365239, "t", lambda: t))
_l_(365241)

def bs_price(c_p, S, K, r, t, sigma):
    _l_(365273)

    if _n_(365242, "c_p", lambda: c_p) == 'c':
        _l_(365272)

        aux = _c_(365245, _n_(365243, "N", lambda: N), _n_(365244, "d1", lambda: d1)) * _n_(365246, "S", lambda: S) - _c_(365249, _n_(365247, "N", lambda: N), _n_(365248, "d2", lambda: d2)) * _n_(365250, "K", lambda: K) * _c_(365254, _n_(365251, "exp", lambda: exp), -_n_(365252, "r", lambda: r)*_n_(365253, "t", lambda: t))
        _l_(365255)
        return aux
    elif _n_(365256, "c_p", lambda: c_p) == 'p':
        _l_(365271)

        aux = _c_(365259, _n_(365257, "N", lambda: N), -_n_(365258, "d2", lambda: d2)) * _n_(365260, "K", lambda: K) * _c_(365264, _n_(365261, "exp", lambda: exp), -_n_(365262, "r", lambda: r)*_n_(365263, "t", lambda: t)) - _c_(365267, _n_(365265, "N", lambda: N), -_n_(365266, "d1", lambda: d1)) * _n_(365268, "S", lambda: S)
        _l_(365269)
        return aux
    else:
        aux = "Please specify call or put options."
        _l_(365270)
        return aux

MAX_TRY = 1000
_l_(365274)
def find_iv_newton(c_p, S, K, r, t, market_price):
    _l_(365312)

    _sigma = 0.5
    _l_(365275)
    for i in _c_(365278, _n_(365276, "range", lambda: range), _n_(365277, "MAX_TRY", lambda: MAX_TRY)):
        _l_(365309)

        _bs_price = _c_(365286, _n_(365279, "bs_price", lambda: bs_price), _n_(365280, "c_p", lambda: c_p), _n_(365281, "S", lambda: S), _n_(365282, "K", lambda: K), _n_(365283, "r", lambda: r), _n_(365284, "t", lambda: t), sigma=_n_(365285, "_sigma", lambda: _sigma))
        _l_(365287)
        diff = _n_(365288, "market_price", lambda: market_price) - _n_(365289, "_bs_price", lambda: _bs_price)
        _l_(365290)
        vega = _n_(365291, "S", lambda: S)*_c_(365294, _n_(365292, "N_prime", lambda: N_prime), _n_(365293, "d1", lambda: d1))*_c_(365297, _n_(365295, "sqrt", lambda: sqrt), _n_(365296, "t", lambda: t))
        _l_(365298)
        if _c_(365301, _n_(365299, "abs", lambda: abs), _n_(365300, "diff", lambda: diff)) < _n_(365302, "ONE_CENT", lambda: ONE_CENT):
            _l_(365305)

            aux = _n_(365303, "_sigma", lambda: _sigma)
            _l_(365304)
            return aux
        _sigma += _n_(365306, "diff", lambda: diff)/_n_(365307, "vega", lambda: vega)
        _l_(365308)
    aux = _n_(365310, "_sigma", lambda: _sigma)
    _l_(365311)
    return aux