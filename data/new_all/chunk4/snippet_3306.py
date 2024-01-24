# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75928026/facing-a-typeerror-unsupported-operand-types-for-gurobipy-linexpr-and
# Partisan lean (WLOG, lean to a party) of each precinct; binary variable l_i == 1 if the precinct leans towards a party, 0 otherwise
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
l  = {_n_(599183, "i", lambda: (i)):_c_(599192, _a_(599185, _n_(599184, "opt_model", lambda: opt_model), "addVar"), vtype=_a_(599188, _a_(599187, _n_(599186, "gp", lambda: gp), "GRB"), "BINARY"),
                        name=_c_(599191, _a_(599189, "l_{0}", "format"), _n_(599190, "i", lambda: i))) 
for i in _n_(599193, "set_I", lambda: set_I)}
_l_(599194)

# Decision variable for n precincts assigned to m districts; binary variable x_i_j == 1 means ith precinct assigned to jth district 
x  = {(_n_(599195, "i", lambda: i),_n_(599196, "j", lambda: j)):_c_(599206, _a_(599198, _n_(599197, "opt_model", lambda: opt_model), "addVar"), vtype=_a_(599201, _a_(599200, _n_(599199, "gp", lambda: gp), "GRB"), "BINARY"),
                        name=_c_(599205, _a_(599202, "x_{0}_{1}", "format"), _n_(599203, "i", lambda: i),_n_(599204, "j", lambda: j))) 
for i in _n_(599207, "set_I", lambda: set_I) for j in _n_(599208, "set_J", lambda: set_J)}
_l_(599209)

# Population for each of n precincts; integer variable pp_i
pp  ={_n_(599210, "i", lambda: (i)):_c_(599219, _a_(599212, _n_(599211, "opt_model", lambda: opt_model), "addVar"), vtype=_a_(599215, _a_(599214, _n_(599213, "gp", lambda: gp), "GRB"), "INTEGER"),
                        lb=0, 
                        name=_c_(599218, _a_(599216, "pp_{0}", "format"), _n_(599217, "i", lambda: i))) 
for i in _n_(599220, "set_I", lambda: set_I)}
_l_(599221)

# Target population
V = 9900
_l_(599222)
targ = _c_(599227, _a_(599224, _n_(599223, "math", lambda: math), "floor"), _n_(599225, "V", lambda: V) // _n_(599226, "m", lambda: m))
_l_(599228)

# actual proportion of lean
actual_proportion = _c_(599234, _a_(599230, _n_(599229, "gp", lambda: gp), "quicksum"), (_n_(599231, "l", lambda: l)[_n_(599232, "i", lambda: i)] for i in _n_(599233, "set_I", lambda: set_I)))/_n_(599235, "n", lambda: n)
_l_(599236)