# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51418152/python-error-when-inserting-data-typeerror-object-of-type-int64-is-not-jso
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _c_(684576, _n_(684574, "len", lambda: len), _n_(684575, "acct", lambda: acct)) > 0:
    _l_(684603)

    list = []
    _l_(684577)
    for i in _c_(684582, _n_(684578, "range", lambda: range), _c_(684581, _n_(684579, "len", lambda: len), _n_(684580, "acct", lambda: acct))):
        _l_(684595)

        update = {'Id': _a_(684584, _n_(684583, "acct", lambda: acct)['Id'], "iloc")[_n_(684585, "i", lambda: i)],
              'name': _a_(684587, _n_(684586, "acct", lambda: acct)['user_count'], "iloc")[_n_(684588, "i", lambda: i)]}
        _l_(684589)

        _c_(684593, _a_(684591, _n_(684590, "list", lambda: list), "append"), _n_(684592, "update", lambda: update))
        _l_(684594)
    _c_(684601, _a_(684599, _a_(684598, _a_(684597, _n_(684596, "sf_data_cursor", lambda: sf_data_cursor), "bulk"), "Account"), "update"), _n_(684600, "list", lambda: list))
    _l_(684602)