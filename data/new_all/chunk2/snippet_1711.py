# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61432536/nameerror-name-pi-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math
    _l_(435103)

except ImportError:
    pass
try:
    from math import pi,cos,sin,tan,atan
    _l_(435105)

except ImportError:
    pass

# eval('a + sin(p/2)', bindings)    # 'sin' not defined

def Formula(expression):
    _l_(435161)

    class F:
        _l_(435158)


        def __init__(self,kwargs):
            _l_(435150)

            s = _c_(435108, _a_(435107, _n_(435106, "kwargs", lambda: kwargs), "replace"), ',','')
            _l_(435109)
            l=_c_(435114, _a_(435113, _c_(435112, _a_(435111, _n_(435110, "s", lambda: s), "replace"), '=',' '), "split"))
            _l_(435115)

            it = _c_(435118, _n_(435116, "iter", lambda: iter), _n_(435117, "l", lambda: l))
            _l_(435119)

            _n_(435120, "self", lambda: self).res_dct = _c_(435126, _n_(435121, "dict", lambda: dict), _c_(435125, _n_(435122, "zip", lambda: zip), _n_(435123, "it", lambda: it),_n_(435124, "it", lambda: it)))
            _l_(435127)
            _n_(435128, "self", lambda: self).res_dct=  {_n_(435129, "k", lambda: k):_c_(435132, _n_(435130, "float", lambda: float), _n_(435131, "v", lambda: v)) for k, v in _c_(435136, _a_(435135, _a_(435134, _n_(435133, "self", lambda: self), "res_dct"), "items"))}
            _l_(435137)

            class Foo:
                _l_(435149)

                def setAllWithKwArgs(self, **kwargs):
                    _l_(435148)

                    for key, value in _c_(435140, _a_(435139, _n_(435138, "kwargs", lambda: kwargs), "items")):
                        _l_(435147)

                        _c_(435145, _n_(435141, "setattr", lambda: setattr), _n_(435142, "self", lambda: self), _n_(435143, "key", lambda: key), _n_(435144, "value", lambda: value))
                        _l_(435146)

        def calc(self):
            _l_(435157)

            aux = _c_(435155, _n_(435151, "eval", lambda: eval), _n_(435152, "expression", lambda: expression),_a_(435154, _n_(435153, "self", lambda: self), "res_dct"))
            _l_(435156)

            return aux
    aux = _n_(435159, "F", lambda: F)
    _l_(435160)

    return aux

triangle_hypotenuse = _c_(435163, _n_(435162, "Formula", lambda: Formula), '(a*a + b*b)**0.5')
_l_(435164)
_c_(435170, _n_(435165, "print", lambda: print), _c_(435169, _a_(435168, _c_(435167, _n_(435166, "triangle_hypotenuse", lambda: triangle_hypotenuse), 'a=3, b=4'), "calc")))
_l_(435171)

cylinder_volume = _c_(435173, _n_(435172, "Formula", lambda: Formula), 'PI * r**2 * h')
_l_(435174)
_c_(435178, _a_(435177, _c_(435176, _n_(435175, "cylinder_volume", lambda: cylinder_volume), 'r= 1, h=2'), "calc"))
_l_(435179)