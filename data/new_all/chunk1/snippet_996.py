# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58131330/solving-attributeerror-while-loading-tfidfvectorizer-with-pickle
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pickle
    _l_(394204)

except ImportError:
    pass

# This load generates the error below
with _c_(394206, _n_(394205, "open", lambda: open), "vectorizer.pickle", 'rb') as f:
    _l_(394212)

    vectorizer = _c_(394210, _a_(394208, _n_(394207, "pickle", lambda: pickle), "load"), _n_(394209, "f", lambda: f))
    _l_(394211)

# This load works:
with _c_(394214, _n_(394213, "open", lambda: open), "docmat.pickle", 'rb') as f:
    _l_(394220)

    doc_mat = _c_(394218, _a_(394216, _n_(394215, "pickle", lambda: pickle), "load"), _n_(394217, "f", lambda: f))
    _l_(394219)