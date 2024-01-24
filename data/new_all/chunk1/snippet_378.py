# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45132060/typeerror-using-telnet-write
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    _l_(398829)

    tn = _c_(398817, _n_(398812, "Telnet", lambda: Telnet), _n_(398813, "host", lambda: host), _c_(398816, _n_(398814, "str", lambda: str), _n_(398815, "port", lambda: port)))
    _l_(398818)
except _n_(398819, "Exception", lambda: Exception) as e:
    _l_(398828)

    _c_(398822, _n_(398820, "print", lambda: print), "Connection cannot be established", _n_(398821, "e", lambda: e))
    _l_(398823)
    _c_(398826, _a_(398825, _n_(398824, "traceback", lambda: traceback), "print_exc"))
    _l_(398827)
_c_(398831, _n_(398830, "print", lambda: print), "You are connected")
_l_(398832)
_c_(398835, _a_(398834, _n_(398833, "tn", lambda: tn), "write"), 'command?'+'\r\n')
_l_(398836)
while True:
    _l_(398841)

    line = _c_(398839, _a_(398838, _n_(398837, "tn", lambda: tn), "read_until"), "\n")
    _l_(398840)