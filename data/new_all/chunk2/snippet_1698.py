# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61945311/i-am-trying-to-perform-the-euler-method-in-python-but-i-am-getting-a-type-error
##Parameters
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
g = 9.8 #in m/s^2
_l_(445718) #in m/s^2
l = 0.5 #in m
_l_(445719) #in m
omega0 = _c_(445724, _a_(445721, _n_(445720, "np", lambda: np), "sqrt"), _n_(445722, "g", lambda: g)/_n_(445723, "l", lambda: l))
_l_(445725)

def euler(theta0, w0, deltat, t_end):
    _l_(445782)

    t0 = 0 #in s
    _l_(445726) #in s

    ##Constructing the arrays
    t_arr = _c_(445733, _a_(445728, _n_(445727, "np", lambda: np), "arange"), _n_(445729, "t0", lambda: t0), _n_(445730, "t_end", lambda: t_end) + _n_(445731, "deltat", lambda: deltat), _n_(445732, "deltat", lambda: deltat))
    _l_(445734)
    w = _c_(445740, _a_(445736, _n_(445735, "np", lambda: np), "zeros"), _c_(445739, _n_(445737, "len", lambda: len), _n_(445738, "t_arr", lambda: t_arr))) #angular velocity in rad/s
    _l_(445741) #angular velocity in rad/s
    theta = _c_(445747, _a_(445743, _n_(445742, "np", lambda: np), "zeros"), _c_(445746, _n_(445744, "len", lambda: len), _n_(445745, "t_arr", lambda: t_arr)))
    _l_(445748)

    ##Setting up our initial conditions
    _n_(445749, "w", lambda: w)[0] = _n_(445750, "w0", lambda: w0)
    _l_(445751)
    theta = _n_(445752, "theta0", lambda: theta0)
    _l_(445753)

    ##Performing the Euler method for both small and large angles
    for i in _c_(445758, _n_(445754, "range", lambda: range), _c_(445757, _n_(445755, "len", lambda: len), _n_(445756, "t_arr", lambda: t_arr)) -1):
        _l_(445779)

        _n_(445759, "w", lambda: w)[_n_(445760, "i", lambda: i) + 1] = _n_(445761, "w", lambda: w)[_n_(445762, "i", lambda: i)] - (_n_(445763, "omega0", lambda: (omega0))**2)*_c_(445768, _a_(445765, _n_(445764, "np", lambda: np), "sin"), _n_(445766, "theta", lambda: theta)[_n_(445767, "i", lambda: i)])*_n_(445769, "deltat", lambda: deltat)
        _l_(445770)
        _n_(445771, "theta", lambda: theta)[_n_(445772, "i", lambda: i) + 1] = _n_(445773, "theta", lambda: theta)[_n_(445774, "i", lambda: i)] + _n_(445775, "w", lambda: w)[_n_(445776, "i", lambda: i)]*_n_(445777, "deltat", lambda: deltat)
        _l_(445778)
    aux = _n_(445780, "theta", lambda: theta)
    _l_(445781)


    return aux


_c_(445784, _n_(445783, "euler", lambda: euler), 0.07, 0, 0.05, 5)
_l_(445785)