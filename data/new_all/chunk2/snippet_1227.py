# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72690805/python-inheriting-generic-type-typeerror-object-init-takes-exactly-one-a
# sprite.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from typing import TypeVar, Generic
  _l_(438456)

except ImportError:
  pass

T = _c_(438459, _n_(438457, "TypeVar", lambda: TypeVar), 'T', bound=_n_(438458, "Object", lambda: Object))
_l_(438460)

class Sprite(_n_(438461, "Generic", lambda: Generic)[_n_(438462, "T", lambda: T)]):
  _l_(438474)

  def __init__(self, **kwargs):
    _l_(438473)

    _c_(438471, _a_(438466, _n_(438463, "super", lambda: super)(_n_(438464, "Sprite", lambda: Sprite), _n_(438465, "self", lambda: self)), "__init__"), _n_(438467, "self", lambda: self), clickable=True, evt_handler=_a_(438469, _n_(438468, "self", lambda: self), "click_wrapper"), **_n_(438470, "kwargs", lambda: kwargs))
    _l_(438472)