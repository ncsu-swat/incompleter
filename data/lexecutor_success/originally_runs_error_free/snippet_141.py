# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
_l_(1548766)
_n_(1548767, "t", lambda: t)
_l_(1548768)
[1, 2, 3, 1, 2, 5, 6, 7, 8]
_l_(1548769)
s = []
_l_(1548770)
for i in _n_(1548771, "t", lambda: t):
       _l_(1548780)

       if _n_(1548772, "i", lambda: i) not in _n_(1548773, "s", lambda: s):
              _l_(1548779)

              _c_(1548777, _a_(1548775, _n_(1548774, "s", lambda: s), "append"), _n_(1548776, "i", lambda: i))
              _l_(1548778)
_n_(1548781, "s", lambda: s)
_l_(1548782)
[1, 2, 3, 5, 6, 7, 8]
_l_(1548783)

