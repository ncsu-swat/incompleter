# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/16712612/use-codecs-to-read-file-with-correct-encoding-typeerror
#!/bin/bash

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import codecs
  _l_(432603)

except ImportError:
  pass

filename = "something.x10"
_l_(432604)

f = _c_(432607, _n_(432605, "open", lambda: open), _n_(432606, "filename", lambda: filename), 'r')
_l_(432608)
fEncoded = _c_(432613, _c_(432611, _a_(432610, _n_(432609, "codecs", lambda: codecs), "getreader"), "ISO-8859-15"), _n_(432612, "f", lambda: f))
_l_(432614)

totalLength = 0
_l_(432615)
for line in _n_(432616, "fEncoded", lambda: fEncoded):
  _l_(432621)

  totalLength+=_c_(432619, _n_(432617, "len", lambda: len), _n_(432618, "line", lambda: line))
  _l_(432620)

_c_(432624, _n_(432622, "print", lambda: print), "Total Length is "+_n_(432623, "totalLength", lambda: totalLength))
_l_(432625)