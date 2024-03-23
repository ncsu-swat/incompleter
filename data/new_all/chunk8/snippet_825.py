# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64010698/typeerror-edit-undo-takes-1-positional-argument-but-2-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   from tkinter import *
   _l_(393997)

except ImportError:
   pass

class UI:
   _l_(394027)

   def __init__(self):
      _l_(394026)

      _n_(393998, "self", lambda: self).root = _c_(394000, _n_(393999, "Tk", lambda: Tk))
      _l_(394001)
      _n_(394002, "self", lambda: self).text= _c_(394006, _n_(394003, "Text", lambda: Text), _a_(394005, _n_(394004, "self", lambda: self), "root"))
      _l_(394007)
      _c_(394011, _a_(394010, _a_(394009, _n_(394008, "self", lambda: self), "text"), "pack"))
      _l_(394012)
      _c_(394019, _a_(394015, _a_(394014, _n_(394013, "self", lambda: self), "text"), "bind"), "<Return>", _a_(394018, _a_(394017, _n_(394016, "self", lambda: self), "entry"), "edit_undo"))
      _l_(394020)
      _c_(394024, _a_(394023, _a_(394022, _n_(394021, "self", lambda: self), "text"), "mainloop"))
      _l_(394025)

_c_(394029, _n_(394028, "UI", lambda: UI))
_l_(394030)