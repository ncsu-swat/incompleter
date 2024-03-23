# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76879501/tkinter-super-init-produces-attributeerror-while-tk-entry-init-do
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(613212)

except ImportError:
    pass
try:
    import tkinter.filedialog as f
    _l_(613214)

except ImportError:
    pass

class DirEntry(_a_(613216, _n_(613215, "tk", lambda: tk), "Entry")):
    _l_(613226)

    def __init__(self, parent, *args, **kwargs):
        _l_(613225)

        _c_(613223, _a_(613218, _n_(613217, "super", lambda: super)(), "__init__"), _n_(613219, "self", lambda: self), _n_(613220, "parent", lambda: parent), *_n_(613221, "args", lambda: args), **_n_(613222, "kwargs", lambda: kwargs))
        _l_(613224)


class GUI:
    _l_(613295)


    def __init__(self):
        _l_(613285)

        _n_(613227, "self", lambda: self).main_window = _c_(613230, _a_(613229, _n_(613228, "tk", lambda: tk), "Tk"))
        _l_(613231)
        _c_(613235, _a_(613234, _a_(613233, _n_(613232, "self", lambda: self), "main_window"), "geometry"), '500x200')
        _l_(613236)

        _n_(613237, "self", lambda: self).input_dir_string = _c_(613240, _a_(613239, _n_(613238, "tk", lambda: tk), "StringVar"))
        _l_(613241)

        _n_(613242, "self", lambda: self).input_frame = _c_(613247, _a_(613244, _n_(613243, "tk", lambda: tk), "LabelFrame"), _a_(613246, _n_(613245, "self", lambda: self), "main_window"),
                                         text='Input Directory')
        _l_(613248)

        _n_(613249, "self", lambda: self).input_dir = _c_(613255, _n_(613250, "DirEntry", lambda: DirEntry), _a_(613252, _n_(613251, "self", lambda: self), "input_frame"),
                                  textvariable=_a_(613254, _n_(613253, "self", lambda: self), "input_dir_string"),
                                  width=40)
        _l_(613256)

        _n_(613257, "self", lambda: self).button = _c_(613264, _a_(613259, _n_(613258, "tk", lambda: tk), "Button"), _a_(613261, _n_(613260, "self", lambda: self), "input_frame"),
                                text='Choose',
                                command=_a_(613263, _n_(613262, "self", lambda: self), "ask_dir"))
        _l_(613265)

        _c_(613269, _a_(613268, _a_(613267, _n_(613266, "self", lambda: self), "input_frame"), "pack"))
        _l_(613270)
        _c_(613274, _a_(613273, _a_(613272, _n_(613271, "self", lambda: self), "input_dir"), "pack"), side='left')
        _l_(613275)
        _c_(613279, _a_(613278, _a_(613277, _n_(613276, "self", lambda: self), "button"), "pack"), side='left')
        _l_(613280)

        _c_(613283, _a_(613282, _n_(613281, "tk", lambda: tk), "mainloop"))
        _l_(613284)

    def ask_dir(self):
        _l_(613294)

        _c_(613292, _a_(613288, _a_(613287, _n_(613286, "self", lambda: self), "input_dir_string"), "set"), _c_(613291, _a_(613290, _n_(613289, "fd", lambda: fd), "askdirectory")))
        _l_(613293)


if _n_(613296, "__name__", lambda: __name__) == '__main__':
    _l_(613300)

    gui = _c_(613298, _n_(613297, "GUI", lambda: GUI))
    _l_(613299)