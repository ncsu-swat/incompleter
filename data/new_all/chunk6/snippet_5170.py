# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68197818/typeerror-all-intermediate-steps-should-be-transformers-and-implement-fit-and-t
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.base import BaseEstimator, TransformerMixin
    _l_(347368)

except ImportError:
    pass
rooms_ix, bedrooms_ix, population_ix, household_ix = 3,4,5,6
_l_(347369)
class CombineAttributesAdder(_n_(347370, "BaseEstimator", lambda: BaseEstimator), _n_(347371, "TransformerMixin", lambda: TransformerMixin)):
    _l_(347411)

    def __init__(self, add_bedrooms_per_room = True):
        _l_(347375)

        _n_(347372, "self", lambda: self).add_bedrooms_per_room = _n_(347373, "add_bedrooms_per_room", lambda: add_bedrooms_per_room)
        _l_(347374)
    def fit(self, X, y=None):
        _l_(347378)

        aux = _n_(347376, "self", lambda: self)
        _l_(347377)
        return aux
    def transfrom(self, X, y=None):
        _l_(347410)

        rooms_per_househond = _n_(347379, "X", lambda: X)[:,_n_(347380, "rooms_ix", lambda: rooms_ix)]/_n_(347381, "X", lambda: X)[:,_n_(347382, "household_ix", lambda: household_ix)]
        _l_(347383)
        population_per_household = _n_(347384, "X", lambda: X)[:,_n_(347385, "population_ix", lambda: population_ix)]/ _n_(347386, "X", lambda: X)[:, _n_(347387, "household_ix", lambda: household_ix)]
        _l_(347388)
        if _a_(347390, _n_(347389, "self", lambda: self), "add_bedrooms_per_room"):
            _l_(347409)

            bedrooms_per_room = _n_(347391, "X", lambda: X)[:,_n_(347392, "bedrooms_ix", lambda: bedrooms_ix)]/_n_(347393, "X", lambda: X)[:_n_(347394, "rooms_ix", lambda: rooms_ix)]
            _l_(347395)
            aux = _a_(347397, _n_(347396, "np", lambda: np), "c_")[_n_(347398, "X", lambda: X), _n_(347399, "rooms_per_househond", lambda: rooms_per_househond), _n_(347400, "population_per_household", lambda: population_per_household), _n_(347401, "bedrooms_per_room", lambda: bedrooms_per_room)]
            _l_(347402)
            return aux
        else:
            aux = _a_(347404, _n_(347403, "np", lambda: np), "c_")[_n_(347405, "X", lambda: X), _n_(347406, "rooms_per_househond", lambda: rooms_per_househond), _n_(347407, "population_per_household", lambda: population_per_household)]
            _l_(347408)
            return aux