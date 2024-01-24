# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54171455/how-to-fix-the-typeerror-g-must-be-a-d-matrix
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.datasets import make_classification
    _l_(420249)

except ImportError:
    pass
try:
    from sklearn.ensemble import RandomForestClassifier
    _l_(420251)

except ImportError:
    pass
try:
    from sklearn.model_selection import train_test_split
    _l_(420253)

except ImportError:
    pass
try:
    import numpy as np
    _l_(420255)

except ImportError:
    pass
try:
    import cvxpy
    _l_(420257)

except ImportError:
    pass

X, y = _c_(420259, _n_(420258, "make_classification", lambda: make_classification), n_samples=1000, n_features=20, n_classes=8,n_informative=5,
                           class_sep=0.2, random_state=2)
_l_(420260)

X_train, X_test, y_train, y_test = _c_(420264, _n_(420261, "train_test_split", lambda: train_test_split), _n_(420262, "X", lambda: X), _n_(420263, "y", lambda: y), test_size=0.2,random_state=1)
_l_(420265)

model = _c_(420267, _n_(420266, "RandomForestClassifier", lambda: RandomForestClassifier), random_state=1)
_l_(420268)
_c_(420273, _a_(420270, _n_(420269, "model", lambda: model), "fit"), _n_(420271, "X_train", lambda: X_train), _n_(420272, "y_train", lambda: y_train))
_l_(420274)
test_probs = _c_(420278, _a_(420276, _n_(420275, "model", lambda: model), "predict_proba"), _n_(420277, "X_test", lambda: X_test))
_l_(420279)

#clipping so that we don't take log of 0 or 1
test_probs = _c_(420283, _a_(420281, _n_(420280, "np", lambda: np), "clip"), _n_(420282, "test_probs", lambda: test_probs), 0.0001, 0.9999)
_l_(420284)

#turning into costs
model_costs = -_c_(420288, _a_(420286, _n_(420285, "np", lambda: np), "log10"), _n_(420287, "test_probs", lambda: test_probs))
_l_(420289)

# Our allocation cannot exceed our supply
# 150 flyers, 80 pamphlets, 25 bumper stickers
supply = _c_(420292, _a_(420291, _n_(420290, "np", lambda: np), "atleast_2d"), [150, 80, 25])
_l_(420293)

# Creating our cvxpy variable of assignments
selection = _c_(420298, _a_(420295, _n_(420294, "cvxpy", lambda: cvxpy), "Bool"), *_a_(420297, _n_(420296, "test_probs", lambda: test_probs), "shape"))
_l_(420299)

# Constant matrix that counts how many of each 
# material we sent to each constituent
TRANSFORMER = _c_(420302, _a_(420301, _n_(420300, "np", lambda: np), "array"), [[1,0,0],
                        [0,1,0],
                        [0,0,1],
                        [1,1,0],
                        [1,0,1],
                        [0,1,1],
                        [1,1,1],
                        [0,0,0]])
_l_(420303)

supply_constraint = _c_(420308, _a_(420305, _n_(420304, "cvxpy", lambda: cvxpy), "sum_entries"), _n_(420306, "selection", lambda: selection) * _n_(420307, "TRANSFORMER", lambda: TRANSFORMER), axis=0) <= _n_(420309, "supply", lambda: supply)
_l_(420310)

# We must make our choice per constituent
# remember that the last column is for "no materials"
feasibility_constraint = _c_(420314, _a_(420312, _n_(420311, "cvxpy", lambda: cvxpy), "sum_entries"), _n_(420313, "selection", lambda: selection), axis=1) == 1
_l_(420315)
constraints = [_n_(420316, "supply_constraint", lambda: supply_constraint), _n_(420317, "feasibility_constraint", lambda: feasibility_constraint)]
_l_(420318)

# Take the negative log of our probabilities to turn them into costs
cost = _c_(420326, _a_(420320, _n_(420319, "cvxpy", lambda: cvxpy), "sum_entries"), _c_(420325, _a_(420322, _n_(420321, "cvxpy", lambda: cvxpy), "mul_elemwise"), _n_(420323, "model_costs", lambda: model_costs), _n_(420324, "selection", lambda: selection)))
_l_(420327)

# Solving the problem
problem = _c_(420335, _a_(420329, _n_(420328, "cvxpy", lambda: cvxpy), "Problem"), _c_(420333, _a_(420331, _n_(420330, "cvxpy", lambda: cvxpy), "Minimize"), _n_(420332, "cost", lambda: cost)), constraints=_n_(420334, "constraints", lambda: constraints))
_l_(420336)
_c_(420341, _a_(420338, _n_(420337, "problem", lambda: problem), "solve"), solver=_a_(420340, _n_(420339, "cvxpy", lambda: cvxpy), "GLPK_MI"))
_l_(420342)