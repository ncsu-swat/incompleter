# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73640902/smartsheet-python-sdk-attributeerror-module-smartsheet-has-no-attribute-she
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import smartsheet
    _l_(642991)

except ImportError:
    pass
try:
    import logging
    _l_(642993)

except ImportError:
    pass

TOKEN = '<<suppressed for security>>'
_l_(642994)

_c_(643001, _a_(642998, _c_(642997, _a_(642996, _n_(642995, "logging", lambda: logging), "getLogger"), 'smartsheet'), "setLevel"), _a_(643000, _n_(642999, "logging", lambda: logging), "CRITICAL"))
_l_(643002)
smart = _c_(643006, _a_(643004, _n_(643003, "smartsheet", lambda: smartsheet), "Smartsheet"), access_token=_n_(643005, "TOKEN", lambda: TOKEN))
_l_(643007)
action = _c_(643011, _a_(643010, _a_(643009, _n_(643008, "smartsheet", lambda: smartsheet), "Sheets"), "list_sheets"), include_all=True)
_l_(643012)
_c_(643015, _n_(643013, "print", lambda: print), _n_(643014, "action", lambda: action)) # Just a placeholder to set a breakpoint
_l_(643016) # Just a placeholder to set a breakpoint