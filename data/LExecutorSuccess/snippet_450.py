# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11218477/how-can-i-use-pickle-to-save-a-dict-or-any-other-python-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pickle
    _l_(1544555)

except ImportError:
    pass

a = {'hello': 'world'}
_l_(1544556)

with _c_(1544558, _n_(1544557, "open", lambda: open), 'filename.pickle', 'wb') as handle:
    _l_(1544565)

    _c_(1544563, _a_(1544560, _n_(1544559, "pickle", lambda: pickle), "dump"), _n_(1544561, "a", lambda: a), _n_(1544562, "handle", lambda: handle))
    _l_(1544564)

with _c_(1544567, _n_(1544566, "open", lambda: open), 'filename.pickle', 'rb') as handle:
    _l_(1544573)

    b = _c_(1544571, _a_(1544569, _n_(1544568, "pickle", lambda: pickle), "load"), _n_(1544570, "handle", lambda: handle))
    _l_(1544572)
try:
    from anycache import anycache
    _l_(1544575)

except ImportError:
    pass

@_c_(1544577, _n_(1544576, "anycache", lambda: anycache), cachedir='path/to/files')
def myfunc(hello):
    _l_(1544580)

    aux = {'hello', _n_(1544578, "hello", lambda: hello)}
    _l_(1544579)
    return aux

