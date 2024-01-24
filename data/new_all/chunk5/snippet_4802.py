# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47715318/typeerror-iter-returned-non-iterator-of-type-layer-for-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
net = _c_(666558, _a_(666557, _n_(666556, "nx", lambda: nx), "DiGraph"))
_l_(666559)
_c_(666562, _n_(666560, "print", lambda: print), _n_(666561, "path", lambda: path))
_l_(666563)
shp = _c_(666567, _a_(666565, _n_(666564, "ogr", lambda: ogr), "Open"), _n_(666566, "path", lambda: path))
_l_(666568)
for lyr in _n_(666569, "shp", lambda: shp):
    _l_(666601)

    _c_(666574, _n_(666570, "print", lambda: print), _c_(666573, _n_(666571, "type", lambda: type), _n_(666572, "lyr", lambda: lyr)))
    _l_(666575)
    _c_(666578, _n_(666576, "print", lambda: print), _n_(666577, "lyr", lambda: lyr))
    _l_(666579)
    fields = [_c_(666582, _a_(666581, _n_(666580, "x", lambda: x), "GetName")) for x in _a_(666584, _n_(666583, "lyr", lambda: lyr), "schema")]
    _l_(666585)
    _c_(666589, _n_(666586, "print", lambda: print), _a_(666588, _n_(666587, "lyr", lambda: lyr), "schema"))
    _l_(666590)
    _c_(666593, _n_(666591, "print", lambda: print), _n_(666592, "fields", lambda: fields))
    _l_(666594)
    for f in _n_(666595, "lyr", lambda: lyr):
        _l_(666600)

        _c_(666598, _n_(666596, "print", lambda: print), _n_(666597, "f", lambda: f))
        _l_(666599)