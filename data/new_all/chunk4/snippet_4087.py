# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63044534/subprocess-call-in-python-getting-error-typeerror-expected-str-bytes-or-os-p
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import subprocess
    _l_(596093)

except ImportError:
    pass
try:
    import optparse
    _l_(596095)

except ImportError:
    pass

def ChangeMac(interface, new_mac):
    _l_(596115)

    _c_(596097, _n_(596096, "print", lambda: print), "mac changed")
    _l_(596098)

    _c_(596102, _a_(596100, _n_(596099, "subprocess", lambda: subprocess), "call"), ["ifconfig", _n_(596101, "interface", lambda: interface), "down"])
    _l_(596103)
    _c_(596108, _a_(596105, _n_(596104, "subprocess", lambda: subprocess), "call"), ["ifconfig", _n_(596106, "interface", lambda: interface), "hw", "ether", _n_(596107, "new_mac", lambda: new_mac)])
    _l_(596109)
    _c_(596113, _a_(596111, _n_(596110, "subprocess", lambda: subprocess), "call"), ["ifconfig", _n_(596112, "interface", lambda: interface), "up"])
    _l_(596114)

parser =_c_(596118, _a_(596117, _n_(596116, "optparse", lambda: optparse), "OptionParser"))
_l_(596119)

_c_(596122, _a_(596121, _n_(596120, "parser", lambda: parser), "add_option"), "-i", "--interface", dest="interface", help="Interface to change its MAC address")
_l_(596123)
_c_(596126, _a_(596125, _n_(596124, "parser", lambda: parser), "add_option"), "-m", "--mac", dest="new_mac", help="new MAC address")
_l_(596127)

(options, arguments) = _c_(596130, _a_(596129, _n_(596128, "parser", lambda: parser), "parse_args"))
_l_(596131)

interface = _a_(596133, _n_(596132, "options", lambda: options), "interface")
_l_(596134)
new_mac = _a_(596136, _n_(596135, "options", lambda: options), "new_mac")
_l_(596137)

_c_(596143, _n_(596138, "ChangeMac", lambda: ChangeMac), _a_(596140, _n_(596139, "optoins", lambda: optoins), "interface"), _a_(596142, _n_(596141, "options", lambda: options), "new_mac"))
_l_(596144)