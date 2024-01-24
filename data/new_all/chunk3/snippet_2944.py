# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57487356/why-does-functools-cmp-to-key-give-me-a-type-error-on-comparison
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from typing import List
  _l_(568274)

except ImportError:
  pass
try:
  import functools
  _l_(568276)

except ImportError:
  pass

def comparison(a: _n_(568277, "str", lambda: str), b: _n_(568278, "str", lambda: str)):
  _l_(568311)

  _c_(568282, _n_(568279, "print", lambda: print), (_n_(568280, "a", lambda: a), _n_(568281, "b", lambda: b)))
  _l_(568283)
  if _c_(568286, _n_(568284, "len", lambda: len), _n_(568285, "a", lambda: a)) == 0:
    _l_(568310)

    aux = _n_(568287, "b", lambda: b)
    _l_(568288)
    return aux
  elif _c_(568291, _n_(568289, "len", lambda: len), _n_(568290, "b", lambda: b)) == 0:
    _l_(568309)

    aux = _n_(568292, "a", lambda: a)
    _l_(568293)
    return aux
  elif _n_(568294, "a", lambda: a)[0] < _n_(568295, "b", lambda: b)[0]:
    _l_(568308)

    aux = _n_(568296, "a", lambda: a)
    _l_(568297)
    return aux
  elif _n_(568298, "a", lambda: a)[0] > _n_(568299, "b", lambda: b)[0]:
    _l_(568307)

    aux = _n_(568300, "b", lambda: b)
    _l_(568301)
    return aux
  else:
    aux = _c_(568305, _n_(568302, "comparison", lambda: comparison), _n_(568303, "a", lambda: a)[1:], _n_(568304, "b", lambda: b)[1:])
    _l_(568306)
    return aux

class Solution:
  _l_(568333)

  def largestNumber(self, nums: _n_(568312, "List", lambda: List)[_n_(568313, "int", lambda: int)]) -> _n_(568314, "str", lambda: str):
    _l_(568332)

    cmp = _c_(568318, _a_(568316, _n_(568315, "functools", lambda: functools), "cmp_to_key"), _n_(568317, "comparison", lambda: comparison))
    _l_(568319)
    res = _c_(568326, _n_(568320, "sorted", lambda: sorted), [_c_(568323, _n_(568321, "str", lambda: str), _n_(568322, "x", lambda: x)) for x in _n_(568324, "nums", lambda: nums)], key=_n_(568325, "cmp", lambda: cmp), reverse=True)
    _l_(568327)
    aux = _c_(568330, _a_(568328, '', "join"), _n_(568329, "res", lambda: res))
    _l_(568331)
    return aux

sol = _c_(568335, _n_(568334, "Solution", lambda: Solution))
_l_(568336)
assert '232302' == _c_(568339, _a_(568338, _n_(568337, "sol", lambda: sol), "largestNumber"), [230, 23, 2])
_l_(568340)