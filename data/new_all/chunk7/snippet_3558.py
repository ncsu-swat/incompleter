# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72245924/re-search-typeerror-cannot-use-a-string-pattern-on-a-bytes-like-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import subprocess
    _l_(608538)

except ImportError:
    pass
try:
    import re
    _l_(608540)

except ImportError:
    pass

interface = _c_(608542, _n_(608541, "input", lambda: input), " interface : ")
_l_(608543)
new_mac = _c_(608545, _n_(608544, "input", lambda: input), "new MAC : ")
_l_(608546)

_c_(608550, _n_(608547, "print", lambda: print), "Changing " + _n_(608548, "interface", lambda: interface) + " to " + _n_(608549, "new_mac", lambda: new_mac))
_l_(608551)

_c_(608555, _a_(608553, _n_(608552, "subprocess", lambda: subprocess), "call"), ["ifconfig", _n_(608554, "interface", lambda: interface), "down"])
_l_(608556)
_c_(608561, _a_(608558, _n_(608557, "subprocess", lambda: subprocess), "call"), ["ifconfig", _n_(608559, "interface", lambda: interface), "hw", "ether", _n_(608560, "new_mac", lambda: new_mac)])
_l_(608562)
_c_(608566, _a_(608564, _n_(608563, "subprocess", lambda: subprocess), "call"), ["ifconfig", _n_(608565, "interface", lambda: interface), "up"])
_l_(608567)
_c_(608570, _a_(608569, _n_(608568, "subprocess", lambda: subprocess), "call"), ["ifconfig"])
_l_(608571)

ifconfig_result = _c_(608574, _a_(608573, _n_(608572, "subprocess", lambda: subprocess), "check_output"), ["ifconfig", "eth0",])
_l_(608575)
_c_(608578, _n_(608576, "print", lambda: print), _n_(608577, "ifconfig_result", lambda: ifconfig_result))
_l_(608579)

mac_addr_searchresult = _c_(608583, _a_(608581, _n_(608580, "re", lambda: re), "search"), r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", _n_(608582, "ifconfig_result", lambda: ifconfig_result))
_l_(608584)
_c_(608589, _n_(608585, "print", lambda: print), _c_(608588, _a_(608587, _n_(608586, "mac_addr_searchresult", lambda: mac_addr_searchresult), "group"), 0))
_l_(608590)