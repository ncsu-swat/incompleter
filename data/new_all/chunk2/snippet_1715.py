# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60975722/attributeerror-bytes-object-has-no-attribute-encode-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _n_(431178, "_charset", lambda: _charset) is None:
        _l_(431188)

        try:
                _l_(431187)

                _c_(431181, _a_(431180, _n_(431179, "_text", lambda: _text), "encode"), 'us-ascii')
                _l_(431182)
                _charset = 'us-ascii'
                _l_(431183)
        except _n_(431184, "UnicodeEncodeError", lambda: UnicodeEncodeError):
                _l_(431186)

                _charset = 'utf-8'
                _l_(431185)