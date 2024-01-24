# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62878497/how-to-solve-attributeerror-list-object-has-no-attribute-lower-in-scipy-mini
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from scipy.optimize import minimize
    _l_(471155)

except ImportError:
    pass

def f(Y,t,params):
    _l_(471165)

    r, p, K, alpha = _n_(471156, "params", lambda: params)
    _l_(471157)
    aux = _n_(471158, "r", lambda: r) * (_n_(471159, "Y", lambda: Y) ** _n_(471160, "p", lambda: p)) * (1 - (_n_(471161, "Y", lambda: Y) / _n_(471162, "K", lambda: K)) ** _n_(471163, "alpha", lambda: alpha))
    _l_(471164)
    return aux

t = _c_(471174, _a_(471167, _n_(471166, "np", lambda: np), "linspace"), 0, _c_(471170, _n_(471168, "len", lambda: len), _n_(471169, "df", lambda: df)), _c_(471173, _n_(471171, "len", lambda: len), _n_(471172, "df", lambda: df)))
_l_(471175)
y0=1
_l_(471176)
initial_guess = [0.5, 0.5, 200000,0.7]
_l_(471177)

# result = minimize(f,initial_guess) #I used this one first but I got an error (TypeError: f() missing 2 required positional arguments: 't' and 'params') so I changed this one to the one below (I added y0 and t)

result = _c_(471183, _n_(471178, "minimize", lambda: minimize), _n_(471179, "f", lambda: f), _n_(471180, "y0", lambda: y0),_n_(471181, "t", lambda: t),_n_(471182, "initial_guess", lambda: initial_guess))
_l_(471184)