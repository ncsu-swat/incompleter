# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45955106/why-do-i-get-an-attributeerror-on-str-sort
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
bands = []
_l_(674377)
band = []
_l_(674378)
headline = _c_(674380, _n_(674379, "input", lambda: input), 'Headline: ')
_l_(674381)
while _n_(674382, "band", lambda: band) != "":
  _l_(674391)

  _c_(674386, _a_(674384, _n_(674383, "bands", lambda: bands), "append"), _n_(674385, "band", lambda: band))
  _l_(674387)
  band = _c_(674389, _n_(674388, "input", lambda: input), 'Band: ')
  _l_(674390)
_c_(674394, _a_(674393, _n_(674392, "band", lambda: band), "sort"))
_l_(674395)
_c_(674398, _n_(674396, "print", lambda: print), _n_(674397, "headline", lambda: headline))
_l_(674399)
for band in _n_(674400, "bands", lambda: bands):
  _l_(674405)

  _c_(674403, _n_(674401, "print", lambda: print), _n_(674402, "band", lambda: band))
  _l_(674404)