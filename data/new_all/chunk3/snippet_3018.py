# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54144305/type-error-missing-required-positional-arguments-with-multiple-py-files
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from gui_backup import Display
    _l_(576030)

except ImportError:
    pass
class Baustein:
    _l_(576064)

    x1, y1, x2, y2 = 10,10,20,20
    _l_(576031)
    color = "red"
    _l_(576032)
    def __init__(self, x1, y1, x2, y2, color):
        _l_(576048)

        _n_(576033, "self", lambda: self).x1 = _n_(576034, "x1", lambda: x1)
        _l_(576035)
        _n_(576036, "self", lambda: self).x2 = _n_(576037, "x2", lambda: x2)
        _l_(576038)
        _n_(576039, "self", lambda: self).y1 = _n_(576040, "y1", lambda: y1)
        _l_(576041)
        _n_(576042, "self", lambda: self).y2 = _n_(576043, "y2", lambda: y2)
        _l_(576044)
        _n_(576045, "self", lambda: self).color = _n_(576046, "color", lambda: color)
        _l_(576047)
    def show_new_object(self):
        _l_(576063)

        quadrat2 = _c_(576052, _a_(576050, _n_(576049, "Display", lambda: Display), "create_rectangle"), 40, 50, 60, 70, fill = _n_(576051, "color", lambda: color))
        _l_(576053)
        _c_(576061, _a_(576055, _n_(576054, "Display", lambda: Display), "coords"), _n_(576056, "quadrat2", lambda: quadrat2), _n_(576057, "x1", lambda: x1), _n_(576058, "y1", lambda: y1), _n_(576059, "x2", lambda: x2), _n_(576060, "y2", lambda: y2))
        _l_(576062)