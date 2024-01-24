# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75196015/typeerror-raised-even-if-the-variable-seems-to-be-of-the-right-type
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
txt = 'Some text, dude!'
_l_(611042)
with _c_(611044, _n_(611043, "open", lambda: open), 'to_load', mode='wb') as f:
   _l_(611054)

   raw = _c_(611047, _a_(611046, _n_(611045, "txt", lambda: txt), "encode"), 'ascii')
   _l_(611048)
   _c_(611052, _n_(611049, "print", lambda: print), _n_(611050, "raw", lambda: raw), file=_n_(611051, "f", lambda: f))
   _l_(611053)