# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57535901/pytest-getting-attributeerror-capturefixture-object-has-no-attribute-readou
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pytest
    _l_(406813)

except ImportError:
    pass

def test_can_output_to_stdout(capsys):
    _l_(406824)

    _c_(406815, _n_(406814, "print", lambda: print), "hello")
    _l_(406816)
    capture = _c_(406819, _a_(406818, _n_(406817, "capsys", lambda: capsys), "readouterror"))
    _l_(406820)
    assert "hello" in _a_(406822, _n_(406821, "capture", lambda: capture), "out")
    _l_(406823)