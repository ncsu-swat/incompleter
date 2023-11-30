# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test_exception():
    _l_(1538487)

    with _c_(1538477, _a_(1538475, _n_(1538474, "pytest", lambda: pytest), "raises"), _n_(1538476, "Exception", lambda: Exception)) as excinfo:
        _l_(1538481)

        _c_(1538479, _n_(1538478, "function_that_raises_exception", lambda: function_that_raises_exception))   
        _l_(1538480)   
    assert _c_(1538485, _n_(1538482, "str", lambda: str), _a_(1538484, _n_(1538483, "excinfo", lambda: excinfo), "value")) == 'some info' 
    _l_(1538486) 

