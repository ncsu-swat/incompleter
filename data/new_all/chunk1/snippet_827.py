# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70548682/python-for-loop-typeerror-int-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
heights = [165, 154, 156, 143, 168, 170, 163, 153, 167]
_l_(402586)
ages = [18, 16, 11, 34, 25, 9, 32, 45, 23]
_l_(402587)

heights_and_ages = _c_(402593, _n_(402588, "list", lambda: list), _c_(402592, _n_(402589, "zip", lambda: zip), _n_(402590, "heights", lambda: heights), _n_(402591, "ages", lambda: ages)))
_l_(402594)
heights_and_ages = [_c_(402597, _n_(402595, "list", lambda: list), _n_(402596, "info", lambda: info)) for info in _n_(402598, "heights_and_ages", lambda: heights_and_ages)]
_l_(402599)

can_ride_coaster = []
_l_(402600)
for info in _n_(402601, "heights_and_ages", lambda: heights_and_ages):
  _l_(402612)

  for height, age in _n_(402602, "info", lambda: info):
    _l_(402611)

    if _n_(402603, "height", lambda: height) > 161 and _n_(402604, "age", lambda: age) > 12:
      _l_(402610)

      _c_(402608, _a_(402606, _n_(402605, "can_ride_coaster", lambda: can_ride_coaster), "append"), _n_(402607, "info", lambda: info))
      _l_(402609)