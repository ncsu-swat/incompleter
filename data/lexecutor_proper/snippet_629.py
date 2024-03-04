# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1303243/how-to-find-out-if-a-python-object-is-a-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def isStr(o):
    _l_(63860)

    aux = _c_(63858, _n_(63856, "repr", lambda: repr), _n_(63857, "o", lambda: o))[-1] in '\'"'
    _l_(63859)
    return aux

_c_(63865, _a_(63864, _c_(63863, _n_(63861, "repr", lambda: repr), _n_(63862, "o", lambda: o))[-1:], "replace"), '"', "'") == "'"
_l_(63866)

