# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76137381/attributeerror-window-object-has-no-attribute-tk
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import tkinter as tk
  _l_(632223)

except ImportError:
  pass
try:
  from tkinter import *
  _l_(632225)

except ImportError:
  pass


class window(_n_(632226, "Toplevel", lambda: Toplevel)):
  _l_(632243)

  def __init__(self, master=None):
    _l_(632242)

    _n_(632227, "self", lambda: self).master=_n_(632228, "master", lambda: master)
    _l_(632229)
    _c_(632232, _a_(632231, _n_(632230, "self", lambda: self), "title"), "Add Customer Record")
    _l_(632233)
    window= _c_(632236, _a_(632235, _n_(632234, "tk", lambda: tk), "Tk"))
    _l_(632237)
    _c_(632240, _a_(632239, _n_(632238, "window", lambda: window), "geometry"), "500x400")
    _l_(632241)


class MainWindow:
  _l_(632266)

  def __init__(self, master=None):
    _l_(632265)

    _n_(632244, "self", lambda: self).master = _n_(632245, "master", lambda: master)
    _l_(632246)
    _c_(632249, _a_(632248, _n_(632247, "self", lambda: self), "title"), "Shopping Mall Management")
    _l_(632250)
    _c_(632254, _a_(632253, _a_(632252, _n_(632251, "self", lambda: self), "master"), "geometry"), "500x300")
    _l_(632255)
    _c_(632263, _a_(632262, _c_(632261, _n_(632256, "Button", lambda: Button), _a_(632258, _n_(632257, "self", lambda: self), "master"), text="Add customer record", command=_a_(632260, _n_(632259, "self", lambda: self), "open_save_record_window")), "pack"), pady=20)
    _l_(632264)


root = _c_(632268, _n_(632267, "window", lambda: window))
_l_(632269)
main_window = _c_(632272, _n_(632270, "MainWindow", lambda: MainWindow), _n_(632271, "root", lambda: root))
_l_(632273)
_c_(632276, _a_(632275, _n_(632274, "root", lambda: root), "mainloop"))
_l_(632277)