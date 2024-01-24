# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72978255/typeerror-unsupported-operand-types-for-list-and-list-when-using-quive
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(630998)

except ImportError:
    pass

x1 = [ 0.5, 0.6, 0.3, 0.2 ]
_l_(630999)
x2 = [ 0.5, 0.6, 0.3, 0.2 ]
_l_(631000)
x3 = [ 0.2, 0.3, 0.5, 0.6 ]
_l_(631001)
x4 = [ 0.4, 0.3, 0.2, 0.1 ]
_l_(631002)

y1 = [ 0.7, 0.9, 0.1, 0.2 ]
_l_(631003)
y2 = [ 0.8, 0.5, 0.9, 0.2 ]
_l_(631004)
y3 = [ 0.6, 0.9, 0.1, 0.2 ]
_l_(631005)
y4 = [ 0.8, 0.2, 0.3, 0.5 ]
_l_(631006)

deltaX1, deltaX2, deltaX3, deltaX4 = [_n_(631007, "x", lambda: x)[1:] - _n_(631008, "x", lambda: x)[:-1] for x in [_n_(631009, "x1", lambda: x1), _n_(631010, "x2", lambda: x2), _n_(631011, "x3", lambda: x3), _n_(631012, "x4", lambda: x4)]]
_l_(631013)
deltaY1, deltaY2, deltaY3, deltaY4 = [_n_(631014, "y", lambda: y)[1:] - _n_(631015, "y", lambda: y)[:-1] for y in [_n_(631016, "y1", lambda: y1), _n_(631017, "y2", lambda: y2), _n_(631018, "y3", lambda: y3), _n_(631019, "y4", lambda: y4)]]
_l_(631020)

line1 = _c_(631025, _a_(631022, _n_(631021, "plt", lambda: plt), "plot"), _n_(631023, "x1", lambda: x1), _n_(631024, "y1", lambda: y1),'bo-',label='apple') 
_l_(631026) 
line2 = _c_(631031, _a_(631028, _n_(631027, "plt", lambda: plt), "plot"), _n_(631029, "x2", lambda: x2), _n_(631030, "y2", lambda: y2),'go-',label='banana') 
_l_(631032) 
line3 = _c_(631037, _a_(631034, _n_(631033, "plt", lambda: plt), "plot"), _n_(631035, "x3", lambda: x3), _n_(631036, "y3", lambda: y3),'ko-',label='orange')
_l_(631038)
line4 = _c_(631043, _a_(631040, _n_(631039, "plt", lambda: plt), "plot"), _n_(631041, "x4", lambda: x4), _n_(631042, "y4", lambda: y4),'ro-',label='tomato') 
_l_(631044) 

arrows1 = _c_(631051, _a_(631046, _n_(631045, "plt", lambda: plt), "quiver"), _n_(631047, "x1", lambda: x1)[:-1], _n_(631048, "y1", lambda: y1)[:-1], _n_(631049, "deltaX1", lambda: deltaX1), _n_(631050, "deltaY1", lambda: deltaY1), scale_units='xy', angles='xy', scale=1)
_l_(631052)
arrows2 = _c_(631059, _a_(631054, _n_(631053, "plt", lambda: plt), "quiver"), _n_(631055, "x2", lambda: x2)[:-1], _n_(631056, "y2", lambda: y2)[:-1], _n_(631057, "deltaX2", lambda: deltaX2), _n_(631058, "deltaY2", lambda: deltaY2), scale_units='xy', angles='xy', scale=1)
_l_(631060)
arrows3 = _c_(631067, _a_(631062, _n_(631061, "plt", lambda: plt), "quiver"), _n_(631063, "x3", lambda: x3)[:-1], _n_(631064, "y3", lambda: y3)[:-1], _n_(631065, "deltaX3", lambda: deltaX3), _n_(631066, "deltaY3", lambda: deltaY3), scale_units='xy', angles='xy', scale=1)
_l_(631068)
arrows4 = _c_(631075, _a_(631070, _n_(631069, "plt", lambda: plt), "quiver"), _n_(631071, "x4", lambda: x4)[:-1], _n_(631072, "y4", lambda: y4)[:-1], _n_(631073, "deltaX4", lambda: deltaX4), _n_(631074, "deltaY4", lambda: deltaY4), scale_units='xy', angles='xy', scale=1)
_l_(631076)


_c_(631079, _a_(631078, _n_(631077, "plt", lambda: plt), "title"), "Fruits")
_l_(631080)
_c_(631083, _a_(631082, _n_(631081, "plt", lambda: plt), "ylabel"), "Tastiness")
_l_(631084)
_c_(631087, _a_(631086, _n_(631085, "plt", lambda: plt), "xlabel"), "Benefit")
_l_(631088)

_c_(631095, _a_(631090, _n_(631089, "plt", lambda: plt), "legend"), bbox_to_anchor=(1.5, 1),
           bbox_transform=_a_(631094, _c_(631093, _a_(631092, _n_(631091, "plt", lambda: plt), "gcf")), "transFigure"))
_l_(631096)