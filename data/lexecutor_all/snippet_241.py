# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = [1, 2, 1, 3, 1, 4]
_l_(1544700)

# brute force method
arr = []
_l_(1544701)
for i in _n_(1544702, "x", lambda: x):
  _l_(1544713)

  if not _n_(1544703, "i", lambda: i) in _n_(1544704, "arr", lambda: arr):
    _l_(1544712)

    _c_(1544710, _a_(1544706, _n_(1544705, "arr", lambda: arr), "insert"), _n_(1544707, "x", lambda: x)[_n_(1544708, "i", lambda: i)],_n_(1544709, "i", lambda: i))
    _l_(1544711)

# recursive method
tmp = []
_l_(1544714)
def remove_duplicates(j=0):
  _l_(1544736)

  if _n_(1544715, "j", lambda: j) < _c_(1544718, _n_(1544716, "len", lambda: len), _n_(1544717, "x", lambda: x)):
    _l_(1544735)

    if not _n_(1544719, "x", lambda: x)[_n_(1544720, "j", lambda: j)] in _n_(1544721, "tmp", lambda: tmp):
      _l_(1544728)

      _c_(1544726, _a_(1544723, _n_(1544722, "tmp", lambda: tmp), "append"), _n_(1544724, "x", lambda: x)[_n_(1544725, "j", lambda: j)])
      _l_(1544727)
    i = _n_(1544729, "j", lambda: j)+1  
    _l_(1544730)  
    _c_(1544733, _n_(1544731, "remove_duplicates", lambda: remove_duplicates), _n_(1544732, "i", lambda: i))
    _l_(1544734)

_c_(1544738, _n_(1544737, "remove_duplicates", lambda: remove_duplicates))
_l_(1544739)

