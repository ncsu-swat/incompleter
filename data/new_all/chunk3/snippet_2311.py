# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52285972/unexpected-typeerror-nonetype-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
A = _c_(575380, _a_(575379, _a_(575378, _n_(575377, "np", lambda: np), "random"), "randint"), 0,100,size=(100, 100))
_l_(575381)
B = _c_(575385, _a_(575384, _a_(575383, _n_(575382, "np", lambda: np), "random"), "randint"), 0,100,size=(100, 100))
_l_(575386)
def contrast(a, b):
    _l_(575400)

    res = _c_(575394, _a_(575388, _n_(575387, "np", lambda: np), "sum"), _c_(575393, _a_(575390, _n_(575389, "np", lambda: np), "equal"), _n_(575391, "a", lambda: a), _n_(575392, "b", lambda: b)))/_a_(575396, _n_(575395, "A", lambda: A), "size")
    _l_(575397)
    aux = _n_(575398, "res", lambda: res)
    _l_(575399)
    return aux

res = _c_(575404, _n_(575401, "contrast", lambda: contrast), _n_(575402, "A", lambda: A), _n_(575403, "B", lambda: B))
_l_(575405)
_c_(575408, _n_(575406, "print", lambda: print), "The correct rate is: %f"%_n_(575407, "res", lambda: res))
_l_(575409)