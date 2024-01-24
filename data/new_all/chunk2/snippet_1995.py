# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71549880/panda3d-simplepbr-running-problemfilenotfounderror-errno-2-no-such-file-or-d
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(436869)

except ImportError:
    pass
try:
    import simplepbr
    _l_(436871)

except ImportError:
    pass
try:
    from direct.showbase.ShowBase import ShowBase
    _l_(436873)

except ImportError:
    pass


class MyApp(_n_(436874, "ShowBase", lambda: ShowBase)):
    _l_(436914)

    def __init__(self):
        _l_(436913)

        _c_(436878, _a_(436876, _n_(436875, "ShowBase", lambda: ShowBase), "__init__"), _n_(436877, "self", lambda: self))
        _l_(436879)

        _c_(436882, _a_(436881, _n_(436880, "simplepbr", lambda: simplepbr), "init"))
        _l_(436883)

        _c_(436888, _a_(436885, _n_(436884, "self", lambda: self), "accept"), 'escape', _a_(436887, _n_(436886, "sys", lambda: sys), "exit"))
        _l_(436889)

        # base.disableMouse()

        _n_(436890, "self", lambda: self).jack = _c_(436894, _a_(436893, _a_(436892, _n_(436891, "self", lambda: self), "loader"), "loadModel"), "jack")
        _l_(436895)
        _c_(436901, _a_(436898, _a_(436897, _n_(436896, "self", lambda: self), "jack"), "reparentTo"), _a_(436900, _n_(436899, "self", lambda: self), "render"))
        _l_(436902)
        _c_(436906, _a_(436905, _a_(436904, _n_(436903, "self", lambda: self), "jack"), "setScale"), 2.0, 2.0, 2.0)
        _l_(436907)
        _c_(436911, _a_(436910, _a_(436909, _n_(436908, "self", lambda: self), "jack"), "setPos"), 8, 50, 0)
        _l_(436912)



if _n_(436915, "__name__", lambda: __name__) == '__main__':
    _l_(436923)

    app = _c_(436917, _n_(436916, "MyApp", lambda: MyApp))
    _l_(436918)
    _c_(436921, _a_(436920, _n_(436919, "app", lambda: app), "run"))
    _l_(436922)