#Source: https://stackoverflow.com/questions/68197818/typeerror-all-intermediate-steps-should-be-transformers-and-implement-fit-and-t
from sklearn.base import BaseEstimator, TransformerMixin
rooms_ix, bedrooms_ix, population_ix, household_ix = 3,4,5,6
class CombineAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True):
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self, X, y=None):
        return self
    def transfrom(self, X, y=None):
        rooms_per_househond = X[:,rooms_ix]/X[:,household_ix]
        population_per_household = X[:,population_ix]/ X[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:,bedrooms_ix]/X[:rooms_ix]
            return np.c_[X, rooms_per_househond, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_househond, population_per_household]