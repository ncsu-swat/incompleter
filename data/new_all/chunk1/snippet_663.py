# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65204523/typeerror-backward-got-an-unexpected-keyword-argument-grad-tensors-in-pytor
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
w = _c_(388036, _a_(388035, _n_(388034, "torch", lambda: torch), "tensor"), [1.], requires_grad=True)
_l_(388037)
x = _c_(388040, _a_(388039, _n_(388038, "torch", lambda: torch), "tensor"), [2.], requires_grad=True)
_l_(388041)

a = _c_(388046, _a_(388043, _n_(388042, "torch", lambda: torch), "add"), _n_(388044, "w", lambda: w), _n_(388045, "x", lambda: x))
_l_(388047)
b = _c_(388051, _a_(388049, _n_(388048, "torch", lambda: torch), "add"), _n_(388050, "w", lambda: w), 1)
_l_(388052)

y0 = _c_(388057, _a_(388054, _n_(388053, "torch", lambda: torch), "mul"), _n_(388055, "a", lambda: a), _n_(388056, "b", lambda: b))    # y0 = (x+w) * (w+1)
_l_(388058)    # y0 = (x+w) * (w+1)
y1 = _c_(388063, _a_(388060, _n_(388059, "torch", lambda: torch), "add"), _n_(388061, "a", lambda: a), _n_(388062, "b", lambda: b))    # y1 = (x+w) + (w+1)     
_l_(388064)    # y1 = (x+w) + (w+1)     


loss = _c_(388069, _a_(388066, _n_(388065, "torch", lambda: torch), "cat"), [_n_(388067, "y0", lambda: y0), _n_(388068, "y1", lambda: y1)], dim=0)       # [y0, y1]
_l_(388070)       # [y0, y1]

weight = _c_(388073, _a_(388072, _n_(388071, "torch", lambda: torch), "tensor"), [1., 2.])
_l_(388074)

_c_(388078, _a_(388076, _n_(388075, "loss", lambda: loss), "backward"), grad_tensors=_n_(388077, "weight", lambda: weight))
_l_(388079)