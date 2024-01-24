# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42866418/using-absolute-path-filenotfounderror
#!/usr/bin/env python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from os import system
  _l_(599423)

except ImportError:
  pass

def text_to_speech(word):
  _l_(599428)

  _c_(599426, _n_(599424, "system", lambda: system), 'say %s' % _n_(599425, "word", lambda: word))
  _l_(599427)

with _c_(599432, _n_(599429, "open", lambda: open), _c_(599431, _n_(599430, "input", lambda: input), "Input File Path: ")) as fin:
  _l_(599439)

  for line in _n_(599433, "fin", lambda: fin):
    _l_(599438)

    _c_(599436, _n_(599434, "text_to_speech", lambda: text_to_speech), _n_(599435, "line", lambda: line))
    _l_(599437)