# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64582633/typeerror-missing-required-positional-arguments-using-getattr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from testc import TestClass
    _l_(440925)

except ImportError:
    pass

args = 'earth,moon,mars'
_l_(440926)
d = {'key':'value'}    
_l_(440927)    
#v = getattr(TestClass, 'test')(args, d) #how do I get this to work?
v = _c_(440932, _c_(440930, _n_(440928, "getattr", lambda: getattr), _n_(440929, "TestClass", lambda: TestClass), 'test'), "earth", "moon", "mars", _n_(440931, "d", lambda: d))
_l_(440933)
_c_(440936, _n_(440934, "print", lambda: print), _n_(440935, "v", lambda: v))
_l_(440937)