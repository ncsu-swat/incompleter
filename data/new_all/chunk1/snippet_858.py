# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61088264/getting-a-typeerror-numpy-float64-object-is-not-callable-error-in-program
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(417046)

except ImportError:
    pass

#Defining how to integrate a function using the trapezium rule
def integrate(f, a, b, N:_n_(417047, "int", lambda: int)):
    _l_(417077)

    h = (_n_(417048, "b", lambda: b)-_n_(417049, "a", lambda: a)) / _n_(417050, "N", lambda: N)       
    _l_(417051)       
    s = 0               
    _l_(417052)               

    for i in _c_(417055, _n_(417053, "range", lambda: range), 1,_n_(417054, "N", lambda: N)):
        _l_(417065)

        c = _c_(417060, _n_(417056, "f", lambda: f), _n_(417057, "a", lambda: a) + _n_(417058, "i", lambda: i)*_n_(417059, "h", lambda: h))
        _l_(417061)
        s = _n_(417062, "s", lambda: s) + _n_(417063, "c", lambda: c)
        _l_(417064)

    Area = _n_(417066, "h", lambda: h)*(0.5*_c_(417069, _n_(417067, "f", lambda: f), _n_(417068, "a", lambda: a)) + 0.5*_c_(417072, _n_(417070, "f", lambda: f), _n_(417071, "b", lambda: b)) + _n_(417073, "s", lambda: s))
    _l_(417074)
    aux = _n_(417075, "Area", lambda: Area)
    _l_(417076)
    return aux

def func(o, m, x):
    _l_(417089)

    aux = _c_(417087, _a_(417079, _n_(417078, "np", lambda: np), "cos"), _n_(417080, "m", lambda: m)*_n_(417081, "o", lambda: o) - _n_(417082, "x", lambda: x)*_c_(417086, _a_(417084, _n_(417083, "np", lambda: np), "sin"), _n_(417085, "o", lambda: o)))        #1st attempt at defining the bessel function
    _l_(417088)        #1st attempt at defining the bessel function
    return aux        #1st attempt at defining the bessel function

def J(m,x):
    _l_(417101)

    aux = (1 / _a_(417091, _n_(417090, "np", lambda: np), "pi")) * _c_(417099, _n_(417092, "integrate", lambda: integrate), _c_(417096, _n_(417093, "func", lambda: func), 0, _n_(417094, "m", lambda: m), _n_(417095, "x", lambda: x)), 0, _a_(417098, _n_(417097, "np", lambda: np), "pi"), 10000)
    _l_(417100)
    return aux

#Produce range of x-values from 0 to 20.
xvals = _c_(417104, _a_(417103, _n_(417102, "np", lambda: np), "linspace"), 0,20,200)
_l_(417105)

#Calculating the value of the bessel function for each value of x and m
for i in _c_(417107, _n_(417106, "range", lambda: range), 200):
    _l_(417126)


    for j in _c_(417109, _n_(417108, "range", lambda: range), 3):
        _l_(417125)

        bessel = _c_(417114, _n_(417110, "J", lambda: J), _n_(417111, "j", lambda: j), _n_(417112, "xvals", lambda: xvals)[_n_(417113, "i", lambda: i)])
        _l_(417115)
        _c_(417123, _n_(417116, "print", lambda: print), _c_(417122, _a_(417117, "x: {}, m: {}, Val: {}", "format"), _n_(417118, "xvals", lambda: xvals)[_n_(417119, "i", lambda: i)], _n_(417120, "j", lambda: j), _n_(417121, "bessel", lambda: bessel)))      #Print statement to check the program is functioning correctly before moving on to the next stage
        _l_(417124)      #Print statement to check the program is functioning correctly before moving on to the next stage