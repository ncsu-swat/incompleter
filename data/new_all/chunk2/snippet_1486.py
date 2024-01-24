# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74504499/typeerror-function-missing-1-required-positional-argument-y
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from names import names
    _l_(475541)

except ImportError:
    pass

def greet(x,y):
    _l_(475551)

    template = _c_(475545, _a_(475542, "Hi {}, Hi {} ", "format"), _n_(475543, "x", lambda: x),_n_(475544, "y", lambda: y))
    _l_(475546)
    _c_(475549, _n_(475547, "print", lambda: print), _n_(475548, "template", lambda: template))
    _l_(475550)


_c_(475555, _n_(475552, "greet", lambda: greet), _c_(475554, _n_(475553, "names", lambda: names)))
_l_(475556)