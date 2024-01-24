# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65144681/attributeerror-nonetype-object-has-no-attribute-group-googletrans-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from googletrans import Translator
    _l_(381209)

except ImportError:
    pass

text = 'hello'
_l_(381210)
translator = _c_(381212, _n_(381211, "Translator", lambda: Translator))
_l_(381213)
result = _a_(381218, _c_(381217, _a_(381215, _n_(381214, "translator", lambda: translator), "translate"), _n_(381216, "text", lambda: text)), "src")
_l_(381219)