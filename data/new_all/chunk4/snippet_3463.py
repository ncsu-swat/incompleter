# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73902401/how-to-fix-attribute-error-in-pyomo-model-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
rho = 0.0008
_l_(592609)
model1 = _c_(592614, _n_(592610, "create_model", lambda: create_model), _n_(592611, "rho", lambda: rho),_n_(592612, "R_avg_tolist", lambda: R_avg_tolist),_n_(592613, "Cov_list", lambda: Cov_list))
_l_(592615)

solver = _c_(592617, _n_(592616, "SolverFactory", lambda: SolverFactory), 'ipopt')
_l_(592618)
results = _c_(592622, _a_(592620, _n_(592619, "solver", lambda: solver), "solve"), _n_(592621, "model1", lambda: model1), tee = True)
_l_(592623)