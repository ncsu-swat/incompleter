# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67732898/what-is-this-error-and-how-to-get-rid-of-it-typeerror-argument-of-type-nonety
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def color_red(val):
  _l_(549699)

  color= 'red' if '|' in _n_(549695, "val", lambda: val) else 'black'
  _l_(549696)
  aux = 'color: %s' % _n_(549697, "color", lambda: color)
  _l_(549698)
  return aux
s = _c_(549704, _a_(549702, _a_(549701, _n_(549700, "df", lambda: df), "style"), "applymap"), _n_(549703, "color_red", lambda: color_red))
_l_(549705)
st = _c_(549708, _a_(549707, _n_(549706, "s", lambda: s), "render"))
_l_(549709)