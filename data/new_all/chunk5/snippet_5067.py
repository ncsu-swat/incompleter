# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55894445/using-dataclass-and-getting-attributeerror-int-object-has-no-attribute-x
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from dataclasses import dataclass, field, InitVar
    _l_(677777)

except ImportError:
    pass

@_n_(677778, "dataclass", lambda: dataclass)
class XYPoint:
    _l_(677817)

    last_serial_no = 0
    _l_(677779)
    x: _n_(677780, "float", lambda: float)
    _l_(677781)
    y: _n_(677782, "float", lambda: float) = 0
    _l_(677783)
    skip: _n_(677784, "InitVar", lambda: InitVar)[_n_(677785, "int", lambda: int)] = 1
    _l_(677786)
    serial_no: _n_(677787, "int", lambda: int) = _c_(677789, _n_(677788, "field", lambda: field), init=False)
    _l_(677790)

    def __post_init__(self, skip):
        _l_(677802)

        _n_(677791, "self", lambda: self).serial_no = _a_(677793, _n_(677792, "self", lambda: self), "last_serial_no") + _a_(677795, _n_(677794, "self", lambda: self), "skip")
        _l_(677796)
        _a_(677798, _n_(677797, "self", lambda: self), "__class__").last_serial_no = _a_(677800, _n_(677799, "self", lambda: self), "serial_no")
        _l_(677801)

    def __add__(self, other):
        _l_(677816)

        new = _c_(677808, _n_(677803, "XYPoint", lambda: XYPoint), _a_(677805, _n_(677804, "self", lambda: self), "x"), _a_(677807, _n_(677806, "self", lambda: self), "y"))
        _l_(677809)
        _n_(677810, "new", lambda: new).x += _n_(677811, "other", lambda: other).x
        _l_(677812)
        _n_(677813, "new", lambda: new).y += _n_(677814, "other", lambda: other).y
        _l_(677815)