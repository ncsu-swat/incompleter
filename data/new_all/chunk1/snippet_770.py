# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57579326/lenstras-elliptic-curve-problem-with-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sympy import mod_inverse
    _l_(397151)

except ImportError:
    pass
try:
    import math
    _l_(397153)

except ImportError:
    pass
try:
    import secrets
    _l_(397155)

except ImportError:
    pass
try:
    from collections import namedtuple
    _l_(397157)

except ImportError:
    pass
Point = _c_(397159, _n_(397158, "namedtuple", lambda: namedtuple), "Point", "x y")
_l_(397160)


def point_valid(P,a,b,p):
    _l_(397182)

    O = 'Inf_Point'
    _l_(397161)
    if _n_(397162, "P", lambda: P) == _n_(397163, "O", lambda: O):
        _l_(397181)

        aux = True
        _l_(397164)
        return aux
    else:
        aux = (_a_(397166, _n_(397165, "P", lambda: P), "y")**2 - (_a_(397168, _n_(397167, "P", lambda: P), "x")**3 + _n_(397169, "a", lambda: a)*_a_(397171, _n_(397170, "P", lambda: P), "x") + _n_(397172, "b", lambda: b))) % _n_(397173, "p", lambda: p) == 0 and 0 <= _a_(397175, _n_(397174, "P", lambda: P), "x") < _n_(397176, "p", lambda: p) and 0 <= _a_(397178, _n_(397177, "P", lambda: P), "y") < _n_(397179, "p", lambda: p)
        _l_(397180)
        return aux


def inverse_point(P,p):
    _l_(397197)

    O = 'Inf_Point'
    _l_(397183)
    # Just calculates the inverse point
    if _n_(397184, "P", lambda: P) == _n_(397185, "O", lambda: O):
        _l_(397188)

        aux = _n_(397186, "P", lambda: P)
        _l_(397187)
        return aux
    aux = _c_(397195, _n_(397189, "Point", lambda: Point), _a_(397191, _n_(397190, "P", lambda: P), "x"), (-_a_(397193, _n_(397192, "P", lambda: P), "y")) % _n_(397194, "p", lambda: p))
    _l_(397196)
    return aux


def point_add(P, Q, a, b, p):
    _l_(397304)

    O = 'Inf_Point'
    _l_(397198)
    # Checking that the points are valid if not raise an exception error
    if not (_c_(397204, _n_(397199, "point_valid", lambda: point_valid), _n_(397200, "P", lambda: P),_n_(397201, "a", lambda: a),_n_(397202, "b", lambda: b),_n_(397203, "p", lambda: p)) and _c_(397210, _n_(397205, "point_valid", lambda: point_valid), _n_(397206, "Q", lambda: Q),_n_(397207, "a", lambda: a),_n_(397208, "b", lambda: b),_n_(397209, "p", lambda: p))):
        _l_(397214)

        raise _c_(397212, _n_(397211, "ValueError", lambda: ValueError), "Invalid inputs")
        _l_(397213)

    if _n_(397215, "P", lambda: P) == _n_(397216, "O", lambda: O):
        _l_(397294)

        R = _n_(397217, "Q", lambda: Q)
        _l_(397218)
    elif _n_(397219, "Q", lambda: Q) == _n_(397220, "O", lambda: O):
        _l_(397293)

        R = _n_(397221, "P", lambda: P)
        _l_(397222)
    elif _n_(397223, "Q", lambda: Q) == _c_(397227, _n_(397224, "inverse_point", lambda: inverse_point), _n_(397225, "P", lambda: P),_n_(397226, "p", lambda: p)):
        _l_(397292)

        R = _n_(397228, "O", lambda: O)
        _l_(397229)
    else:
        if _n_(397230, "P", lambda: P) == _n_(397231, "Q", lambda: Q):
            _l_(397271)

            try:
                _l_(397243)

                inv = _c_(397236, _n_(397232, "mod_inverse", lambda: mod_inverse), 2 * _a_(397234, _n_(397233, "P", lambda: P), "y"),_n_(397235, "p", lambda: p))
                _l_(397237)
            except _n_(397238, "ValueError", lambda: ValueError):
                _l_(397242)

                aux = 2 * _a_(397240, _n_(397239, "P", lambda: P), "y")
                _l_(397241)
                return aux
            dydx = (3 * _a_(397245, _n_(397244, "P", lambda: P), "x")**2 + _n_(397246, "a", lambda: a)) * _n_(397247, "inv", lambda: inv)
            _l_(397248)
        else:
            try:
                _l_(397264)

                inv =  _c_(397255, _n_(397249, "mod_inverse", lambda: mod_inverse), _a_(397251, _n_(397250, "Q", lambda: Q), "x") - _a_(397253, _n_(397252, "P", lambda: P), "x"),_n_(397254, "p", lambda: p))
                _l_(397256)
            except _n_(397257, "ValueError", lambda: ValueError):
                _l_(397263)

                aux = _a_(397259, _n_(397258, "Q", lambda: Q), "x") - _a_(397261, _n_(397260, "P", lambda: P), "x")
                _l_(397262)
                return aux
            dydx = (_a_(397266, _n_(397265, "Q", lambda: Q), "y") - _a_(397268, _n_(397267, "P", lambda: P), "y")) * _n_(397269, "inv", lambda: inv)
            _l_(397270)
        x = (_n_(397272, "dydx", lambda: dydx)**2 - _a_(397274, _n_(397273, "P", lambda: P), "x") - _a_(397276, _n_(397275, "Q", lambda: Q), "x")) % _n_(397277, "p", lambda: p)
        _l_(397278)
        y = (_n_(397279, "dydx", lambda: dydx) * (_a_(397281, _n_(397280, "P", lambda: P), "x") - _n_(397282, "x", lambda: x)) - _a_(397284, _n_(397283, "P", lambda: P), "y")) % _n_(397285, "p", lambda: p)
        _l_(397286)
        R = _c_(397290, _n_(397287, "Point", lambda: Point), _n_(397288, "x", lambda: x), _n_(397289, "y", lambda: y))
        _l_(397291)

    # Making sure the result is on the curve
    assert _c_(397300, _n_(397295, "point_valid", lambda: point_valid), _n_(397296, "R", lambda: R),_n_(397297, "a", lambda: a),_n_(397298, "b", lambda: b),_n_(397299, "p", lambda: p))
    _l_(397301)
    aux = _n_(397302, "R", lambda: R)
    _l_(397303)
    # Returning the result
    return aux


def point_multiply(P,n,a,b,p):
    _l_(397340)

    O = 'Inf_Point'
    _l_(397305)
    Q = _n_(397306, "P", lambda: P)
    _l_(397307)
    R = _n_(397308, "O", lambda: O)
    _l_(397309)
    while _n_(397310, "n", lambda: n) > 0:
        _l_(397337)

        if _n_(397311, "n", lambda: n) % 2 == 1:
            _l_(397320)

            R = _c_(397318, _n_(397312, "point_add", lambda: point_add), _n_(397313, "R", lambda: R),_n_(397314, "Q", lambda: Q),_n_(397315, "a", lambda: a),_n_(397316, "b", lambda: b),_n_(397317, "p", lambda: p))
            _l_(397319)
        Q = _c_(397327, _n_(397321, "point_add", lambda: point_add), _n_(397322, "Q", lambda: Q),_n_(397323, "Q", lambda: Q),_n_(397324, "a", lambda: a),_n_(397325, "b", lambda: b),_n_(397326, "p", lambda: p))
        _l_(397328)
        n = _c_(397332, _a_(397330, _n_(397329, "math", lambda: math), "floor"), _n_(397331, "n", lambda: n)/2)
        _l_(397333)
        if _n_(397334, "n", lambda: n) > 0:
            _l_(397336)

            continue
            _l_(397335)
    aux = _n_(397338, "R", lambda: R)
    _l_(397339)
    return aux



def random_curve(N):
    _l_(397376)

    while True:
        _l_(397375)

        A = _c_(397344, _a_(397342, _n_(397341, "secrets", lambda: secrets), "randbelow"), _n_(397343, "N", lambda: N))
        _l_(397345)
        x = _c_(397349, _a_(397347, _n_(397346, "secrets", lambda: secrets), "randbelow"), _n_(397348, "N", lambda: N))
        _l_(397350)
        y = _c_(397354, _a_(397352, _n_(397351, "secrets", lambda: secrets), "randbelow"), _n_(397353, "N", lambda: N))
        _l_(397355)
        P = _c_(397359, _n_(397356, "Point", lambda: Point), _n_(397357, "x", lambda: x),_n_(397358, "y", lambda: y))
        _l_(397360)
        B = (_n_(397361, "y", lambda: y)**2 - _n_(397362, "x", lambda: x)**3 - _n_(397363, "A", lambda: A)*_n_(397364, "x", lambda: x)) % _n_(397365, "N", lambda: N)
        _l_(397366)

        if (4*_n_(397367, "A", lambda: A)**3 + 27*_n_(397368, "B", lambda: B)**2) % _n_(397369, "N", lambda: N) != 0:
            _l_(397374)

            aux = (_n_(397370, "A", lambda: A),_n_(397371, "B", lambda: B),_n_(397372, "P", lambda: P))
            _l_(397373)
            return aux


def lenstra(N,B):
    _l_(397417)

    a,b,P = _c_(397379, _n_(397377, "random_curve", lambda: random_curve), _n_(397378, "N", lambda: N))
    _l_(397380)
    for i in _c_(397383, _n_(397381, "range", lambda: range), 2,_n_(397382, "B", lambda: B)+1):
        _l_(397416)

        if _c_(397386, _n_(397384, "type", lambda: type), _n_(397385, "P", lambda: P))== _n_(397387, "int", lambda: int):
            _l_(397405)

            d = _c_(397392, _a_(397389, _n_(397388, "math", lambda: math), "gcd"), _n_(397390, "P", lambda: P),_n_(397391, "N", lambda: N))
            _l_(397393)
            if _n_(397394, "d", lambda: d) < _n_(397395, "N", lambda: N):
                _l_(397404)

                aux = _n_(397396, "d", lambda: d)
                _l_(397397)
                return aux
            elif _n_(397398, "d", lambda: d) == _n_(397399, "N", lambda: N):
                _l_(397403)

                _c_(397401, _n_(397400, "print", lambda: print), 'start again')
                _l_(397402)
        Q = _c_(397412, _n_(397406, "point_multiply", lambda: point_multiply), _n_(397407, "P", lambda: P),_n_(397408, "i", lambda: i),_n_(397409, "a", lambda: a),_n_(397410, "b", lambda: b),_n_(397411, "N", lambda: N))
        _l_(397413)
        P = _n_(397414, "Q", lambda: Q)
        _l_(397415)

_c_(397421, _n_(397418, "print", lambda: print), _c_(397420, _n_(397419, "lenstra", lambda: lenstra), 8453621,15))
_l_(397422)