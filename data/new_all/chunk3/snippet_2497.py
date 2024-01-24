# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74920325/dtreeviz-attributeerror-dataframe-object-has-no-attribute-dtype-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(553726)

except ImportError:
    pass
try:
    from sklearn.model_selection import train_test_split
    _l_(553728)

except ImportError:
    pass
try:
    from sklearn import tree
    _l_(553730)

except ImportError:
    pass
try:
    from dtreeviz.trees import *
    _l_(553732)

except ImportError:
    pass


#fit the classifier
clf = _c_(553735, _a_(553734, _n_(553733, "tree", lambda: tree), "DecisionTreeClassifier"), max_depth=3, random_state=42)
_l_(553736)
_c_(553741, _a_(553738, _n_(553737, "clf", lambda: clf), "fit"), _n_(553739, "X_train", lambda: X_train), _n_(553740, "y_train", lambda: y_train))
_l_(553742)