# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77577205/getting-attributeerror-when-running-optuna-study
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
study = _c_(427897, _a_(427891, _n_(427890, "optuna", lambda: optuna), "create_study"), direction='minimize', sampler=_c_(427896, _a_(427894, _a_(427893, _n_(427892, "optuna", lambda: optuna), "samplers"), "GridSampler"), _n_(427895, "search_space", lambda: search_space)))
_l_(427898)
_c_(427902, _a_(427900, _n_(427899, "study", lambda: study), "optimize"), _n_(427901, "objective", lambda: objective), n_trials=20)
_l_(427903)