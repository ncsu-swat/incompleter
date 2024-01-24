# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46795862/constrained-optimization-for-word2vec-giving-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
optimizer = _c_(526040, _a_(526034, _a_(526033, _a_(526032, _n_(526031, "tf", lambda: tf), "contrib"), "opt"), "ScipyOptimizerInterface"), _n_(526035, "loss", lambda: loss), options={'max_iter': 5}, 
                                                    var_to_bounds = {_a_(526037, _n_(526036, "self", lambda: self), "_emb"): (-1., 1.), _a_(526039, _n_(526038, "self", lambda: self), "_sm_w_t"): (-1., 1.)},
                                                    method = 'SLSQP')
_l_(526041)
_n_(526042, "self", lambda: self)._optimizer = _n_(526043, "optimizer", lambda: optimizer)
_l_(526044)