# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49469481/lpthw-48-nosetest-says-attributeerror-str-object-has-no-attribute-while
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from nose.tools import *
    _l_(697462)

except ImportError:
    pass
try:
    from ex48 import lexicon
    _l_(697464)

except ImportError:
    pass

def test_directions():
    _l_(697471)

    _c_(697469, _n_(697465, "assert_equal", lambda: assert_equal), _c_(697468, _a_(697467, _n_(697466, "lexicon", lambda: lexicon), "scan"), "north"), [('direction', 'north')])
    _l_(697470)