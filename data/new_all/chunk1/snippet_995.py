# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58131330/solving-attributeerror-while-loading-tfidfvectorizer-with-pickle
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pickle
    _l_(399537)

except ImportError:
    pass

vectorizer = _c_(399539, _n_(399538, "TfidfVectorizer", lambda: TfidfVectorizer), ...)
_l_(399540)
doc_mat = _c_(399544, _a_(399542, _n_(399541, "vectorizer", lambda: vectorizer), "fit_transform"), _n_(399543, "corpus", lambda: corpus))
_l_(399545)
with _c_(399547, _n_(399546, "open", lambda: open), "vectorizer.pickle", "wb") as f:
    _l_(399554)

    _c_(399552, _a_(399549, _n_(399548, "pickle", lambda: pickle), "dump"), _n_(399550, "vectorizer", lambda: vectorizer), _n_(399551, "f", lambda: f))
    _l_(399553)

with _c_(399556, _n_(399555, "open", lambda: open), "docmat.pickle", "wb") as f:
    _l_(399563)

    _c_(399561, _a_(399558, _n_(399557, "pickle", lambda: pickle), "dump"), _n_(399559, "doc_mat", lambda: doc_mat), _n_(399560, "f", lambda: f))
    _l_(399562)