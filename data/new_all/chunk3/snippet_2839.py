# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61298742/why-am-i-getting-a-typeerror-string-indices-must-be-integers-error-on-strings
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(527603, _a_(527602, _n_(527601, "cursor", lambda: cursor), "execute"), "SELECT id, name FROM playlists")
_l_(527604)
lists = _c_(527607, _a_(527606, _n_(527605, "cursor", lambda: cursor), "fetchall"))
_l_(527608)

for index, list in _n_(527609, "lists", lambda: lists):
    _l_(527617)

    _c_(527615, _n_(527610, "print", lambda: print), _c_(527614, _a_(527611, "{0} - {1}", "format"), _n_(527612, "list", lambda: list)['id'], _n_(527613, "list", lambda: list)['name']))
    _l_(527616)