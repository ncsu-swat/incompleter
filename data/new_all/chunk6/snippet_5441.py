# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49762971/attributeerror-tuple-object-has-no-attribute-lower
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.feature_extraction.text import CountVectorizer
    _l_(367055)

except ImportError:
    pass
cv = _c_(367057, _n_(367056, "CountVectorizer", lambda: CountVectorizer))
_l_(367058)
text_train_cv = _c_(367062, _a_(367060, _n_(367059, "cv", lambda: cv), "fit_transform"), _n_(367061, "train", lambda: train))
_l_(367063)
_a_(367065, _n_(367064, "text_train_cv", lambda: text_train_cv), "shape")
_l_(367066)