# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61559860/getting-typeerror-module-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
       import multiprocessing as mp
       _l_(352970)

except ImportError:
       pass
try:
       import time as t
       _l_(352972)

except ImportError:
       pass

def do_something():
       _l_(352980)

       _c_(352975, _a_(352974, _n_(352973, "t", lambda: t), "sleep"), 1)
       _l_(352976)
       _c_(352978, _n_(352977, "print", lambda: print), "Done Sleeping")
       _l_(352979)

p1 = _c_(352984, _a_(352982, _n_(352981, "mp", lambda: mp), "process"), target=_n_(352983, "do_something", lambda: do_something))
_l_(352985)
p2 = _c_(352989, _a_(352987, _n_(352986, "mp", lambda: mp), "process"), target=_n_(352988, "do_something", lambda: do_something))
_l_(352990)

_c_(352993, _a_(352992, _n_(352991, "p1", lambda: p1), "start"))
_l_(352994)
_c_(352997, _a_(352996, _n_(352995, "p2", lambda: p2), "start"))
_l_(352998)

_c_(353001, _a_(353000, _n_(352999, "p1", lambda: p1), "join"))
_l_(353002)
_c_(353005, _a_(353004, _n_(353003, "p2", lambda: p2), "join"))
_l_(353006)