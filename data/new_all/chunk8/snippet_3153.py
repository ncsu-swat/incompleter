# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36983403/python-attribute-error-when-trying-to-access-thread-owned-variable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(619795)

except ImportError:
    pass
try:
    import threading
    _l_(619797)

except ImportError:
    pass

class mainWindow(_a_(619799, _n_(619798, "threading", lambda: threading), "Thread")):
    _l_(619890)

    def __init__(self, winWidth=500, winHeight=300):
        _l_(619818)

        _c_(619804, _a_(619802, _a_(619801, _n_(619800, "threading", lambda: threading), "Thread"), "__init__"), _n_(619803, "self", lambda: self))
        _l_(619805)
        _n_(619806, "self", lambda: self).winWidth = _n_(619807, "winWidth", lambda: winWidth)
        _l_(619808)
        _n_(619809, "self", lambda: self).winHeight = _n_(619810, "winHeight", lambda: winHeight)
        _l_(619811)

        # Save all drawn objects, to move or delete them later
        _n_(619812, "self", lambda: self).bricks = []
        _l_(619813)

        _c_(619816, _a_(619815, _n_(619814, "self", lambda: self), "start"))                    #start thread
        _l_(619817)                    #start thread

    def run(self):
        _l_(619835)

        # parent object for all windows
        _n_(619819, "self", lambda: self).master = _c_(619822, _a_(619821, _n_(619820, "tk", lambda: tk), "Tk"))
        _l_(619823)
        _c_(619829, _a_(619826, _a_(619825, _n_(619824, "self", lambda: self), "master"), "protocol"), "WM_DELETE_WINDOW", _a_(619828, _n_(619827, "self", lambda: self), "callback"))
        _l_(619830)
        _c_(619833, _a_(619832, _n_(619831, "self", lambda: self), "show"))
        _l_(619834)

    def callback(self):
        _l_(619841)

        _c_(619839, _a_(619838, _a_(619837, _n_(619836, "self", lambda: self), "master"), "quit"))
        _l_(619840)

    # Initialize everything important
    def show(self, tileSize=10):
        _l_(619879)

        # create main window
        _n_(619842, "self", lambda: self).w = _c_(619851, _a_(619844, _n_(619843, "tk", lambda: tk), "Canvas"), _a_(619846, _n_(619845, "self", lambda: self), "master"),
                width=_a_(619848, _n_(619847, "self", lambda: self), "winWidth"),
                height=_a_(619850, _n_(619849, "self", lambda: self), "winHeight"),
                background="white")
        _l_(619852)

        _c_(619856, _a_(619855, _a_(619854, _n_(619853, "self", lambda: self), "w"), "pack"))
        _l_(619857)

        # draw brick
        color = "gray49"
        _l_(619858)
        posX = 200
        _l_(619859)
        posY = 100
        _l_(619860)
        _c_(619873, _a_(619863, _a_(619862, _n_(619861, "self", lambda: self), "bricks"), "append"), _c_(619872, _a_(619866, _a_(619865, _n_(619864, "self", lambda: self), "w"), "create_rectangle"), _n_(619867, "posX", lambda: posX), _n_(619868, "posY", lambda: posY), _n_(619869, "posX", lambda: posX)+20, _n_(619870, "posY", lambda: posY)+20, fill=_n_(619871, "color", lambda: color)))
        _l_(619874)
        _c_(619877, _a_(619876, _n_(619875, "tk", lambda: tk), "mainloop"))
        _l_(619878)

    def move_brick(self, x,y):
        _l_(619889)

        _c_(619887, _a_(619882, _a_(619881, _n_(619880, "self", lambda: self), "w"), "move"), _a_(619884, _n_(619883, "self", lambda: self), "brick"), _n_(619885, "x", lambda: x), _n_(619886, "y", lambda: y))
        _l_(619888)


mainWindow = _c_(619892, _n_(619891, "mainWindow", lambda: mainWindow))
_l_(619893)
_c_(619896, _a_(619895, _n_(619894, "mainWindow", lambda: mainWindow), "move_brick"), 100,100)
_l_(619897)