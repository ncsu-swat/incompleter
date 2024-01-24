# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63729685/how-to-differentiate-between-unexpected-keyword-argument-and-missing-positional
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test_method(a):
    _l_(465247)

    _c_(465245, _n_(465243, "print", lambda: print), _n_(465244, "a", lambda: a))
    _l_(465246)

_c_(465249, _n_(465248, "test_method", lambda: test_method), a=1) # 'a'
_l_(465250) # 'a'
_c_(465252, _n_(465251, "test_method", lambda: test_method)) # TypeError: test_method() missing 1 required positional argument: 'a'
_l_(465253) # TypeError: test_method() missing 1 required positional argument: 'a'
_c_(465255, _n_(465254, "test_method", lambda: test_method), a=1, b=2) # TypeError: test_method() got an unexpected keyword argument 'b'
_l_(465256) # TypeError: test_method() got an unexpected keyword argument 'b'