# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1823058/how-to-print-a-number-using-commas-as-thousands-separators
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import locale
    _l_(1539194)

except ImportError:
    pass

_c_(1539199, _a_(1539196, _n_(1539195, "locale", lambda: locale), "setlocale"), _a_(1539198, _n_(1539197, "locale", lambda: locale), "LC_ALL"), '' )
_l_(1539200)
_c_(1539203, _a_(1539202, _n_(1539201, "locale", lambda: locale), "currency"), 1234567.89, grouping = True )
_l_(1539204)

'Portuguese_Brazil.1252'
_l_(1539205)
'R$ 1.234.567,89'
_l_(1539206)

