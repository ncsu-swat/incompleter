# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38044773/receiving-typeerror-object-new-takes-no-parameters-when-new-not-chang
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Grid import Grid
    _l_(444353)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(444355)

except ImportError:
    pass

class MainWindow:
    _l_(444437)

    def __init__(self, rows=10, cols=10, wraparound=True, pattern=None):
        _l_(444430)

        _n_(444356, "self", lambda: self).root = _c_(444358, _n_(444357, "Tk", lambda: Tk))
        _l_(444359)

        grid_frame = _c_(444366, _a_(444364, _c_(444363, _n_(444360, "Frame", lambda: Frame), _a_(444362, _n_(444361, "self", lambda: self), "root")), "pack"), side=_n_(444365, "TOP", lambda: TOP))
        _l_(444367)
        _n_(444368, "self", lambda: self).grid = _c_(444375, _n_(444369, "Grid", lambda: Grid), _n_(444370, "grid_frame", lambda: grid_frame), rows=_n_(444371, "rows", lambda: rows), cols=_n_(444372, "cols", lambda: cols), wraparound=_n_(444373, "wraparound", lambda: wraparound), pattern=_n_(444374, "pattern", lambda: pattern))
        _l_(444376)

        button_frame = _c_(444383, _a_(444381, _c_(444380, _n_(444377, "Frame", lambda: Frame), _a_(444379, _n_(444378, "self", lambda: self), "root")), "pack"), side=_n_(444382, "BOTTOM", lambda: BOTTOM))
        _l_(444384)
        _n_(444385, "self", lambda: self).time_interval = 1000
        _l_(444386)
        _n_(444387, "self", lambda: self).start_stop_button = _c_(444395, _a_(444393, _c_(444392, _n_(444388, "Button", lambda: Button), _n_(444389, "button_frame", lambda: button_frame), text='START', command=_a_(444391, _n_(444390, "self", lambda: self), "start_stepper")), "pack"), side=_n_(444394, "LEFT", lambda: LEFT))
        _l_(444396)
        _n_(444397, "self", lambda: self).step_button = _c_(444403, _n_(444398, "Button", lambda: Button), _n_(444399, "button_frame", lambda: button_frame), text='STEP', command=_a_(444402, _a_(444401, _n_(444400, "self", lambda: self), "grid"), "step"))
        _l_(444404)

        _n_(444405, "self", lambda: self).menubar = _c_(444409, _n_(444406, "Menu", lambda: Menu), _a_(444408, _n_(444407, "self", lambda: self), "root"))
        _l_(444410)
        _c_(444416, _a_(444413, _a_(444412, _n_(444411, "self", lambda: self), "menubar"), "add_command"), label='Change Time Interval', command=_a_(444415, _n_(444414, "self", lambda: self), "change_time_interval"))
        _l_(444417)
        _c_(444423, _a_(444420, _a_(444419, _n_(444418, "self", lambda: self), "root"), "config"), menu=_a_(444422, _n_(444421, "self", lambda: self), "menubar"))
        _l_(444424)

        _c_(444428, _a_(444427, _a_(444426, _n_(444425, "self", lambda: self), "root"), "mainloop"))
        _l_(444429)

    def change_time_interval(self):
        _l_(444432)

        # Incomplete
        pass
        _l_(444431)

    def start_stepper(self):
        _l_(444434)

        # Incomplete
        pass
        _l_(444433)

    def stop_stepper(self):
        _l_(444436)

        # Incomplete
        pass
        _l_(444435)