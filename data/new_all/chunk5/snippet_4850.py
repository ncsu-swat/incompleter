# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45955106/why-do-i-get-an-attributeerror-on-str-sort
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
bands = []
_l_(695780)
band = []
_l_(695781)
headline = _c_(695783, _n_(695782, "input", lambda: input), 'Headline: ')
_l_(695784)
while _n_(695785, "band", lambda: band) != "":
  _l_(695794)

  _c_(695789, _a_(695787, _n_(695786, "bands", lambda: bands), "append"), _n_(695788, "band", lambda: band))
  _l_(695790)
  band = _c_(695792, _n_(695791, "input", lambda: input), 'Band: ')
  _l_(695793)
_c_(695797, _a_(695796, _n_(695795, "band", lambda: band), "sort"))
_l_(695798)
_c_(695801, _n_(695799, "print", lambda: print), _n_(695800, "headline", lambda: headline))
_l_(695802)
for band in _n_(695803, "bands", lambda: bands):
  _l_(695808)

  _c_(695806, _n_(695804, "print", lambda: print), _n_(695805, "band", lambda: band))
  _l_(695807)