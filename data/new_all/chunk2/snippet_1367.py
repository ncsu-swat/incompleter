# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68815246/typeerror-fit-missing-1-required-positional-argument-y
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for name, estimator in _c_(438428, _a_(438427, _a_(438426, _n_(438425, "sklearn", lambda: sklearn), "utils"), "all_estimators"), type_filter='regressor'):
    _l_(438454)

    model =  _c_(438433, _n_(438429, "make_pipeline", lambda: make_pipeline), _c_(438431, _n_(438430, "StandardScaler", lambda: StandardScaler)), _n_(438432, "estimator", lambda: estimator))
    _l_(438434)
    try:
        _l_(438453)

        scores =  _c_(438439, _n_(438435, "cross_validate", lambda: cross_validate), _n_(438436, "model", lambda: model), _n_(438437, "X", lambda: X), _n_(438438, "y", lambda: y), scoring='r2')
        _l_(438440)
        _c_(438447, _n_(438441, "print", lambda: print), _n_(438442, "name", lambda: name), ': ', _c_(438446, _a_(438444, _n_(438443, "np", lambda: np), "mean"), _n_(438445, "scores", lambda: scores)['test_score']))
        _l_(438448)
    except:
        _l_(438452)

        _c_(438450, _n_(438449, "print", lambda: print), 'Does not get printed.')
        _l_(438451)