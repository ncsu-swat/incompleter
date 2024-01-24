# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67422146/attributeerror-module-urllib-response-has-no-attribute-status-code
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(605088)

except ImportError:
    pass
try:
    import urllib.request
    _l_(605090)

except ImportError:
    pass
try:
    import urllib
    _l_(605092)

except ImportError:
    pass
try:
    import requests
    _l_(605094)

except ImportError:
    pass

url = "https://ubisoftconnect.com/en-US/profile/"
_l_(605095)
response = _c_(605099, _a_(605098, _a_(605097, _n_(605096, "urllib", lambda: urllib), "response"), "status_code"), "https://ubisoftconnect.com/en-US/profile/")
_l_(605100)

_c_(605104, _n_(605101, "print", lambda: print), _a_(605103, _n_(605102, "r", lambda: r), "status_code"))
_l_(605105)

url = 'https://ubisoftconnect.com/en-US/profile/'
_l_(605106)
available = "available.txt"
_l_(605107)
users = "usernames.txt"
_l_(605108)
now = _c_(605112, _a_(605111, _a_(605110, _n_(605109, "datetime", lambda: datetime), "datetime"), "now"))
_l_(605113)
if _a_(605115, _n_(605114, "response", lambda: response), "status_code") == 200:
    _l_(605125)

    _c_(605117, _n_(605116, "print", lambda: print), 'Available')
    _l_(605118)
elif _a_(605120, _n_(605119, "response", lambda: response), "status_code") == 404:
    _l_(605124)

    _c_(605122, _n_(605121, "print", lambda: print), 'Unavailable')
    _l_(605123)


def initialize():
    _l_(605148)

    ascii_banner = _c_(605128, _a_(605127, _n_(605126, "pyfiglet", lambda: pyfiglet), "figlet_format"), "Made  By  Gxzs!!")
    _l_(605129)
    _c_(605132, _n_(605130, "print", lambda: print), _n_(605131, "ascii_banner", lambda: ascii_banner))
    _l_(605133)
    _c_(605137, _n_(605134, "print", lambda: print), f"{_c_(605136, _n_(605135, 'count', lambda: count))} usernames detected")
    _l_(605138)
    _c_(605140, _n_(605139, "print", lambda: print), "Press ENTER to begin checking")
    _l_(605141)
    _c_(605143, _n_(605142, "input", lambda: input), "")
    _l_(605144)
    _c_(605146, _n_(605145, "check", lambda: check))
    _l_(605147)