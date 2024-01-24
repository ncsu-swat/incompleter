# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61327187/error-in-python3-typeerror-module-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
 import pyperclip
 _l_(668704)

except ImportError:
 pass
try:
 import tkinter as Tk
 _l_(668706)

except ImportError:
 pass
while True:
 _l_(668749)

 r = _c_(668708, _n_(668707, "Tk", lambda: Tk))
 _l_(668709)
 _c_(668712, _a_(668711, _n_(668710, "r", lambda: r), "withdraw"))
 _l_(668713)
 try:
  _l_(668726)

  selection = _c_(668717, _a_(668716, _a_(668715, _n_(668714, "r", lambda: r), "selection"), "get"), selection="CLIPBOARD")
  _l_(668718)
 except _a_(668720, _n_(668719, "tk", lambda: tk), "TclError"):
  _l_(668725)

  selection = None
  _l_(668721)
  _c_(668723, _n_(668722, "sleep", lambda: sleep), 0.1)
  _l_(668724)

 try:
  _l_(668748)

  selection = _c_(668730, _a_(668729, _a_(668728, _n_(668727, "r", lambda: r), "selection"), "get"), selection="CLIPBOARD")
  _l_(668731)
 except _a_(668733, _n_(668732, "tk", lambda: tk), "TclError"):
  _l_(668747)

  selection = None
  _l_(668734)
  _c_(668737, _a_(668736, _n_(668735, "r", lambda: r), "clipboard_clear"))
  _l_(668738)
  if _c_(668741, _n_(668739, "len", lambda: len), _n_(668740, "result", lambda: result)) > 10:
   _l_(668746)

   _c_(668744, _a_(668743, _n_(668742, "pyperclip", lambda: pyperclip), "copy"), "aaa")
   _l_(668745)