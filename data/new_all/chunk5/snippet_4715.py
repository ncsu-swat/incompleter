# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51418152/python-error-when-inserting-data-typeerror-object-of-type-int64-is-not-jso
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _c_(659640, _n_(659638, "len", lambda: len), _n_(659639, "acct", lambda: acct)) > 0:
    _l_(659667)

    list = []
    _l_(659641)
    for i in _c_(659646, _n_(659642, "range", lambda: range), _c_(659645, _n_(659643, "len", lambda: len), _n_(659644, "acct", lambda: acct))):
        _l_(659659)

        update = {'Id': _a_(659648, _n_(659647, "acct", lambda: acct)['Id'], "iloc")[_n_(659649, "i", lambda: i)],
              'name': _a_(659651, _n_(659650, "acct", lambda: acct)['user_count'], "iloc")[_n_(659652, "i", lambda: i)]}
        _l_(659653)

        _c_(659657, _a_(659655, _n_(659654, "list", lambda: list), "append"), _n_(659656, "update", lambda: update))
        _l_(659658)
    _c_(659665, _a_(659663, _a_(659662, _a_(659661, _n_(659660, "sf_data_cursor", lambda: sf_data_cursor), "bulk"), "Account"), "update"), _n_(659664, "list", lambda: list))
    _l_(659666)