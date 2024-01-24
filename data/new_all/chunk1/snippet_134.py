# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43881184/typeerror-init-got-an-unexpected-keyword-argument-no-builder-kivy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class PlayerImage(_n_(419625, "Image", lambda: Image)):
    _l_(419661)

    angle = _c_(419626, NumericProperty, 0)
    _l_(419627)

    def __init__(self):
        _l_(419632)

        _c_(419630, _a_(419629, _n_(419628, "super", lambda: super)(), "__init__"))
        _l_(419631)


    def on_touch_down(self, touch):
        _l_(419660)

        # self.currentstate = self.states["person.zip/"]
        _c_(419636, _a_(419634, _n_(419633, "Animation", lambda: Animation), "cancel_all"), _n_(419635, "self", lambda: self))
        _l_(419637)
        angle = _c_(419649, _n_(419638, "degrees", lambda: degrees), _c_(419648, _n_(419639, "atan2", lambda: atan2), _a_(419641, _n_(419640, "touch", lambda: touch), "y") - _a_(419643, _n_(419642, "self", lambda: self), "center_y"),
                              _a_(419645, _n_(419644, "touch", lambda: touch), "x") - _a_(419647, _n_(419646, "self", lambda: self), "center_x")))
        _l_(419650)

        _c_(419658, _a_(419656, _c_(419655, _n_(419651, "Animation", lambda: Animation), center=_a_(419653, _n_(419652, "touch", lambda: touch), "pos"), angle=_n_(419654, "angle", lambda: angle)), "start"), _n_(419657, "self", lambda: self))
        _l_(419659)