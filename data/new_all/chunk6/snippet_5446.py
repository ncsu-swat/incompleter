# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49762971/attributeerror-tuple-object-has-no-attribute-lower
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.feature_extraction.text import CountVectorizer
    _l_(344199)

except ImportError:
    pass
cv = _c_(344201, _n_(344200, "CountVectorizer", lambda: CountVectorizer))
_l_(344202)
text_train_cv = _c_(344206, _a_(344204, _n_(344203, "cv", lambda: cv), "fit_transform"), _n_(344205, "train", lambda: train))
_l_(344207)
_a_(344209, _n_(344208, "text_train_cv", lambda: text_train_cv), "shape")
_l_(344210)