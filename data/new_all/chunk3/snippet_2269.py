# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54145421/typeerror-cant-concat-str-to-bytes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def create_set(feature, value):
  _l_(544864)

  aux = b'{"type":"set","feature":'+_n_(544861, "feature", lambda: feature)+',"value":'+_n_(544862, "value", lambda: value)+'}'
  _l_(544863)
  return aux

on = _c_(544866, _n_(544865, "create_set", lambda: create_set), "main.power", "on")
_l_(544867)