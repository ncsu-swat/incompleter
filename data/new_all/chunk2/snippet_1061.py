# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47360506/typeerror-object-init-takes-no-parameters-trying-to-subclass-torch-floatt
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import inspect
    _l_(447626)

except ImportError:
    pass
try:
    import torch
    _l_(447628)

except ImportError:
    pass

x = [[1, 2], [3, 4]]
_l_(447629)

_c_(447635, _n_(447630, "print", lambda: print), _c_(447634, _a_(447632, _n_(447631, "torch", lambda: torch), "FloatTensor"), _n_(447633, "x", lambda: x)))
_l_(447636)
'''
 1  2
 3  4
[torch.FloatTensor of size 2x2]
'''
_l_(447637)

_c_(447645, _n_(447638, "print", lambda: print), _c_(447644, _a_(447640, _n_(447639, "inspect", lambda: inspect), "signature"), _a_(447643, _a_(447642, _n_(447641, "torch", lambda: torch), "FloatTensor"), "__init__")))
_l_(447646)
'''
(self, /, *args, **kwargs)
'''
_l_(447647)

class Image(_a_(447649, _n_(447648, "torch", lambda: torch), "FloatTensor")):
    _l_(447664)

    def __init__(self, arg):
        _l_(447663)

        _c_(447656, _n_(447650, "print", lambda: print), _c_(447655, _a_(447652, _n_(447651, "inspect", lambda: inspect), "signature"), _a_(447654, _n_(447653, "super", lambda: super)(), "__init__")))
        _l_(447657)
        _c_(447661, _a_(447659, _n_(447658, "super", lambda: super)(), "__init__"), _n_(447660, "arg", lambda: arg))
        _l_(447662)

_c_(447667, _n_(447665, "Image", lambda: Image), _n_(447666, "x", lambda: x))
_l_(447668)
'''
(*args, **kwargs)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-369-4b1aee6414f6> in <module>()
     21         super().__init__(arg)
     22 
---> 23 Image(x)

<ipython-input-369-4b1aee6414f6> in __init__(self, arg)
     19     def __init__(self, arg):
     20         print(inspect.signature(super().__init__))
---> 21         super().__init__(arg)
     22 
     23 Image(x)

TypeError: object.__init__() takes no parameters
'''
_l_(447669)