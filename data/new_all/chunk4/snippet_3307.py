# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75928026/facing-a-typeerror-unsupported-operand-types-for-gurobipy-linexpr-and
# Define the objective function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
obj = _c_(609105, _a_(609090, _n_(609089, "gp", lambda: gp), "quicksum"), (_c_(609103, _a_(609092, _n_(609091, "gp", lambda: gp), "quicksum"), (_c_(609101, _a_(609094, _n_(609093, "gp", lambda: gp), "abs_"), _n_(609095, "pp", lambda: pp)[_n_(609096, "i", lambda: i)] * _n_(609097, "x", lambda: x)[_n_(609098, "i", lambda: i), _n_(609099, "j", lambda: j)] - _n_(609100, "targ", lambda: targ)) for i in _n_(609102, "set_I", lambda: set_I))) for j in _n_(609104, "set_J", lambda: set_J))) + _c_(609129, _a_(609107, _n_(609106, "gp", lambda: gp), "quicksum"), (_c_(609127, _a_(609109, _n_(609108, "gp", lambda: gp), "quicksum"), (_c_(609125, _a_(609111, _n_(609110, "gp", lambda: gp), "abs_"), _n_(609112, "l", lambda: l)[_n_(609113, "i", lambda: i)] * _n_(609114, "x", lambda: x)[_n_(609115, "i", lambda: i), _n_(609116, "j", lambda: j)] / _c_(609123, _a_(609118, _n_(609117, "gp", lambda: gp), "quicksum"), (_n_(609119, "x", lambda: x)[_n_(609120, "i", lambda: i), _n_(609121, "j", lambda: j)] for i in _n_(609122, "set_I", lambda: set_I))) - _n_(609124, "actual_proportion", lambda: actual_proportion)
        )
        for i in _n_(609126, "set_I", lambda: set_I)))
    for j in _n_(609128, "set_J", lambda: set_J)))
_l_(609130)

_c_(609136, _a_(609132, _n_(609131, "model", lambda: model), "setObjective"), _n_(609133, "obj", lambda: obj), _a_(609135, _n_(609134, "GRB", lambda: GRB), "MINIMIZE"))
_l_(609137)