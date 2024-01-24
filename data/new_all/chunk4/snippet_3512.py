# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72978255/typeerror-unsupported-operand-types-for-list-and-list-when-using-quive
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(583015)

except ImportError:
    pass

x1 = [ 0.5, 0.6, 0.3, 0.2 ]
_l_(583016)
x2 = [ 0.5, 0.6, 0.3, 0.2 ]
_l_(583017)
x3 = [ 0.2, 0.3, 0.5, 0.6 ]
_l_(583018)
x4 = [ 0.4, 0.3, 0.2, 0.1 ]
_l_(583019)

y1 = [ 0.7, 0.9, 0.1, 0.2 ]
_l_(583020)
y2 = [ 0.8, 0.5, 0.9, 0.2 ]
_l_(583021)
y3 = [ 0.6, 0.9, 0.1, 0.2 ]
_l_(583022)
y4 = [ 0.8, 0.2, 0.3, 0.5 ]
_l_(583023)

deltaX1, deltaX2, deltaX3, deltaX4 = [_n_(583024, "x", lambda: x)[1:] - _n_(583025, "x", lambda: x)[:-1] for x in [_n_(583026, "x1", lambda: x1), _n_(583027, "x2", lambda: x2), _n_(583028, "x3", lambda: x3), _n_(583029, "x4", lambda: x4)]]
_l_(583030)
deltaY1, deltaY2, deltaY3, deltaY4 = [_n_(583031, "y", lambda: y)[1:] - _n_(583032, "y", lambda: y)[:-1] for y in [_n_(583033, "y1", lambda: y1), _n_(583034, "y2", lambda: y2), _n_(583035, "y3", lambda: y3), _n_(583036, "y4", lambda: y4)]]
_l_(583037)

line1 = _c_(583042, _a_(583039, _n_(583038, "plt", lambda: plt), "plot"), _n_(583040, "x1", lambda: x1), _n_(583041, "y1", lambda: y1),'bo-',label='apple') 
_l_(583043) 
line2 = _c_(583048, _a_(583045, _n_(583044, "plt", lambda: plt), "plot"), _n_(583046, "x2", lambda: x2), _n_(583047, "y2", lambda: y2),'go-',label='banana') 
_l_(583049) 
line3 = _c_(583054, _a_(583051, _n_(583050, "plt", lambda: plt), "plot"), _n_(583052, "x3", lambda: x3), _n_(583053, "y3", lambda: y3),'ko-',label='orange')
_l_(583055)
line4 = _c_(583060, _a_(583057, _n_(583056, "plt", lambda: plt), "plot"), _n_(583058, "x4", lambda: x4), _n_(583059, "y4", lambda: y4),'ro-',label='tomato') 
_l_(583061) 

arrows1 = _c_(583068, _a_(583063, _n_(583062, "plt", lambda: plt), "quiver"), _n_(583064, "x1", lambda: x1)[:-1], _n_(583065, "y1", lambda: y1)[:-1], _n_(583066, "deltaX1", lambda: deltaX1), _n_(583067, "deltaY1", lambda: deltaY1), scale_units='xy', angles='xy', scale=1)
_l_(583069)
arrows2 = _c_(583076, _a_(583071, _n_(583070, "plt", lambda: plt), "quiver"), _n_(583072, "x2", lambda: x2)[:-1], _n_(583073, "y2", lambda: y2)[:-1], _n_(583074, "deltaX2", lambda: deltaX2), _n_(583075, "deltaY2", lambda: deltaY2), scale_units='xy', angles='xy', scale=1)
_l_(583077)
arrows3 = _c_(583084, _a_(583079, _n_(583078, "plt", lambda: plt), "quiver"), _n_(583080, "x3", lambda: x3)[:-1], _n_(583081, "y3", lambda: y3)[:-1], _n_(583082, "deltaX3", lambda: deltaX3), _n_(583083, "deltaY3", lambda: deltaY3), scale_units='xy', angles='xy', scale=1)
_l_(583085)
arrows4 = _c_(583092, _a_(583087, _n_(583086, "plt", lambda: plt), "quiver"), _n_(583088, "x4", lambda: x4)[:-1], _n_(583089, "y4", lambda: y4)[:-1], _n_(583090, "deltaX4", lambda: deltaX4), _n_(583091, "deltaY4", lambda: deltaY4), scale_units='xy', angles='xy', scale=1)
_l_(583093)


_c_(583096, _a_(583095, _n_(583094, "plt", lambda: plt), "title"), "Fruits")
_l_(583097)
_c_(583100, _a_(583099, _n_(583098, "plt", lambda: plt), "ylabel"), "Tastiness")
_l_(583101)
_c_(583104, _a_(583103, _n_(583102, "plt", lambda: plt), "xlabel"), "Benefit")
_l_(583105)

_c_(583112, _a_(583107, _n_(583106, "plt", lambda: plt), "legend"), bbox_to_anchor=(1.5, 1),
           bbox_transform=_a_(583111, _c_(583110, _a_(583109, _n_(583108, "plt", lambda: plt), "gcf")), "transFigure"))
_l_(583113)