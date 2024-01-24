# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56842427/python-robobrowser-typeerror-nonetype
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(425196)

except ImportError:
    pass
try:
    import config
    _l_(425198)

except ImportError:
    pass
try:
    from robobrowser import RoboBrowser
    _l_(425200)

except ImportError:
    pass
br = _c_(425202, _n_(425201, "RoboBrowser", lambda: RoboBrowser), history=True)
_l_(425203)

_c_(425206, _a_(425205, _n_(425204, "br", lambda: br), "open"), "https://www.tessco.com/login")
_l_(425207)
form = _c_(425210, _a_(425209, _n_(425208, "br", lambda: br), "get_form"))
_l_(425211)
_n_(425212, "form", lambda: form)['userID'] = _a_(425214, _n_(425213, "config", lambda: config), "TESSCO_USERNAME")
_l_(425215)
_n_(425216, "form", lambda: form)['password'] = _a_(425218, _n_(425217, "config", lambda: config), "TESSCO_PASSWORD")
_l_(425219)
_c_(425223, _a_(425221, _n_(425220, "br", lambda: br), "submit_form"), _n_(425222, "form", lambda: form))
_l_(425224)