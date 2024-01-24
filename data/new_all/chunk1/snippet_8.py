# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/19877306/nameerror-global-name-unicode-is-not-defined-in-python-3
# utf-8 ? we need unicode
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _c_(417784, _n_(417781, "isinstance", lambda: isinstance), _n_(417782, "unicode_or_str", lambda: unicode_or_str), _n_(417783, "unicode", lambda: unicode)):
    _l_(417794)

    text = _n_(417785, "unicode_or_str", lambda: unicode_or_str)
    _l_(417786)
    decoded = False
    _l_(417787)
else:
    text = _c_(417791, _a_(417789, _n_(417788, "unicode_or_str", lambda: unicode_or_str), "decode"), _n_(417790, "encoding", lambda: encoding))
    _l_(417792)
    decoded = True
    _l_(417793)