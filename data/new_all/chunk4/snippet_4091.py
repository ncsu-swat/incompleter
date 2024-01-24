# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63044534/subprocess-call-in-python-getting-error-typeerror-expected-str-bytes-or-os-p
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import subprocess
    _l_(643247)

except ImportError:
    pass
try:
    import optparse
    _l_(643249)

except ImportError:
    pass

def ChangeMac(interface, new_mac):
    _l_(643269)

    _c_(643251, _n_(643250, "print", lambda: print), "mac changed")
    _l_(643252)

    _c_(643256, _a_(643254, _n_(643253, "subprocess", lambda: subprocess), "call"), ["ifconfig", _n_(643255, "interface", lambda: interface), "down"])
    _l_(643257)
    _c_(643262, _a_(643259, _n_(643258, "subprocess", lambda: subprocess), "call"), ["ifconfig", _n_(643260, "interface", lambda: interface), "hw", "ether", _n_(643261, "new_mac", lambda: new_mac)])
    _l_(643263)
    _c_(643267, _a_(643265, _n_(643264, "subprocess", lambda: subprocess), "call"), ["ifconfig", _n_(643266, "interface", lambda: interface), "up"])
    _l_(643268)

parser =_c_(643272, _a_(643271, _n_(643270, "optparse", lambda: optparse), "OptionParser"))
_l_(643273)

_c_(643276, _a_(643275, _n_(643274, "parser", lambda: parser), "add_option"), "-i", "--interface", dest="interface", help="Interface to change its MAC address")
_l_(643277)
_c_(643280, _a_(643279, _n_(643278, "parser", lambda: parser), "add_option"), "-m", "--mac", dest="new_mac", help="new MAC address")
_l_(643281)

(options, arguments) = _c_(643284, _a_(643283, _n_(643282, "parser", lambda: parser), "parse_args"))
_l_(643285)

interface = _a_(643287, _n_(643286, "options", lambda: options), "interface")
_l_(643288)
new_mac = _a_(643290, _n_(643289, "options", lambda: options), "new_mac")
_l_(643291)

_c_(643297, _n_(643292, "ChangeMac", lambda: ChangeMac), _a_(643294, _n_(643293, "optoins", lambda: optoins), "interface"), _a_(643296, _n_(643295, "options", lambda: options), "new_mac"))
_l_(643298)