# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46559020/typeerror-string-indices-must-be-integers-what-should-i-do-to-avoid-this-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
lat = []
_l_(665718)
lng = []
_l_(665719)
for x in _n_(665720, "sd", lambda: sd):
    _l_(665730)

    for y in _n_(665721, "sd", lambda: sd):
        _l_(665729)

        for z in _n_(665722, "y", lambda: y)["geometry"]:
            _l_(665728)

            _c_(665726, _a_(665724, _n_(665723, "lat", lambda: lat), "append"), _n_(665725, "z", lambda: z)["location"]["lat"])
            _l_(665727)

for x in _n_(665731, "sd", lambda: sd):
    _l_(665741)

    for y in _n_(665732, "sd", lambda: sd):
        _l_(665740)

        for z in _n_(665733, "y", lambda: y)["geometry"]:
            _l_(665739)

            _c_(665737, _a_(665735, _n_(665734, "lng", lambda: lng), "append"), _n_(665736, "z", lambda: z)["location"]["lng"])
            _l_(665738)

_c_(665745, _n_(665742, "print", lambda: print), _n_(665743, "lat", lambda: lat), _n_(665744, "lng", lambda: lng))
_l_(665746)