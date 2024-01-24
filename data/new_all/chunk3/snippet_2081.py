# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65269486/attributeerror-float-object-has-no-attribute-append-when-trying-to-append-v
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collection import defaultdict
    _l_(572584)

except ImportError:
    pass

new_dict= _c_(572587, _n_(572585, "defaultdict", lambda: defaultdict), _n_(572586, "list", lambda: list))
_l_(572588)

for row in _n_(572589, "list_dict", lambda: list_dict):
    _l_(572611)

    acct=_n_(572590, "row", lambda: row)[_n_(572591, "acct", lambda: acct)]
    _l_(572592)
    time_spent= _c_(572596, _n_(572593, "float", lambda: float), _n_(572594, "row", lambda: row)[_n_(572595, "time_spent", lambda: time_spent)])
    _l_(572597)

    if (_n_(572598, "acct", lambda: acct) not in _n_(572599, "new_dict", lambda: new_dict)):
        _l_(572610)

        _n_(572600, "new_dict", lambda: new_dict)[_n_(572601, "acct", lambda: acct)] = _n_(572602, "time_spent", lambda: time_spent)
        _l_(572603)
    else:
        _c_(572608, _a_(572606, _n_(572604, "new_dict", lambda: new_dict)[_n_(572605, "acct", lambda: acct)], "append"), _n_(572607, "time_spent", lambda: time_spent))
        _l_(572609)