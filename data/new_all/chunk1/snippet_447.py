# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57890868/vscode-pytest-error-typeerror-cannot-read-property-of-undefined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import inc_dec
    _l_(399408)

except ImportError:
    pass

def test_increment():
    _l_(399413)

    assert _c_(399411, _a_(399410, _n_(399409, "inc_dec", lambda: inc_dec), "increment"), 3) == 4
    _l_(399412)

def test_decrement():
    _l_(399418)

    assert _c_(399416, _a_(399415, _n_(399414, "inc_dec", lambda: inc_dec), "decrement"), 3) == 4
    _l_(399417)