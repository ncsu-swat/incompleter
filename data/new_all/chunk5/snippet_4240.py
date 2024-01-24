# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60902295/error-when-trying-to-override-init-typeerror-init-takes-1-positio
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def main():
   _l_(705684)

   child = _c_(705678, _n_(705677, "Child", lambda: Child), 2, first=1)
   _l_(705679)
   _c_(705682, _a_(705681, _n_(705680, "child", lambda: child), "display"))
   _l_(705683)


class Base():
   _l_(705692)


   def __init__(self, **kwargs):
      _l_(705691)

      _c_(705689, _n_(705685, "print", lambda: print), _c_(705688, _a_(705687, _n_(705686, "kwargs", lambda: kwargs), "get"), "first", "nice try"))
      _l_(705690)


class Child(_n_(705693, "Base", lambda: Base)):
   _l_(705710)


   def __init__(self, value, **kwargs):
      _l_(705703)

      _c_(705698, _a_(705695, _n_(705694, "super", lambda: super)(), "__init__"), _n_(705696, "self", lambda: self), **_n_(705697, "kwargs", lambda: kwargs))
      _l_(705699)
      _n_(705700, "self", lambda: self).value = _n_(705701, "value", lambda: value)
      _l_(705702)

   def display(self):
      _l_(705709)

      _c_(705707, _n_(705704, "print", lambda: print), _a_(705706, _n_(705705, "self", lambda: self), "value"))
      _l_(705708)


_c_(705712, _n_(705711, "main", lambda: main))
_l_(705713)