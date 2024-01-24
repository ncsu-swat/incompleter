# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55840738/attributeerror-module-main-has-no-attribute-averagewordlengthextractor
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class AverageWordLengthExtractor(_n_(575410, "BaseEstimator", lambda: BaseEstimator), _n_(575411, "TransformerMixin", lambda: TransformerMixin)):
    _l_(575445)

    
    def __init__(self):
        _l_(575413)

        pass
        _l_(575412)
    def average_word_length(self, text):
        _l_(575426)

        aux = _c_(575424, _a_(575415, _n_(575414, "np", lambda: np), "mean"), [_c_(575418, _n_(575416, "len", lambda: len), _n_(575417, "word", lambda: word)) for word in _c_(575421, _a_(575420, _n_(575419, "text", lambda: text), "split")) if _n_(575422, "word", lambda: word) not in _n_(575423, "stopWords", lambda: stopWords)])
        _l_(575425)
        return aux
    def fit(self, x, y=None):
        _l_(575429)

        aux = _n_(575427, "self", lambda: self)
        _l_(575428)
        return aux
    def transform(self, x , y=None):
        _l_(575444)

        aux = _c_(575442, _a_(575441, _c_(575440, _a_(575431, _n_(575430, "pd", lambda: pd), "DataFrame"), _c_(575439, _a_(575436, _c_(575435, _a_(575433, _n_(575432, "pd", lambda: pd), "Series"), _n_(575434, "x", lambda: x)), "apply"), _a_(575438, _n_(575437, "self", lambda: self), "average_word_length"))), "fillna"), 0)
        _l_(575443)
        return aux