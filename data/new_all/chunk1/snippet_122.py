# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/12518594/get-typeerror-when-trying-to-get-all-rows-from-mysql
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
query = _c_(383032, _a_(383031, _n_(383030, "conn", lambda: conn), "cursor"))
_l_(383033)
_c_(383036, _a_(383035, _n_(383034, "query", lambda: query), "execute"), "SELECT * FROM wp_options")
_l_(383037)
for row in _n_(383038, "query", lambda: query):
    _l_(383043)

    _c_(383041, _n_(383039, "print", lambda: print), _n_(383040, "row", lambda: row))
    _l_(383042)
_c_(383046, _a_(383045, _n_(383044, "query", lambda: query), "close"))
_l_(383047)