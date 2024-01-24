# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61591232/typeerror-unorderable-types-str-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.ensemble import RandomForestClassifier
    _l_(349755)

except ImportError:
    pass
text_classifier = _c_(349757, _n_(349756, "RandomForestClassifier", lambda: RandomForestClassifier), n_estimators=100, random_state=0)  
_l_(349758)  
_c_(349763, _a_(349760, _n_(349759, "text_classifier", lambda: text_classifier), "fit"), _n_(349761, "X_train", lambda: X_train), _n_(349762, "y_train", lambda: y_train))
_l_(349764)