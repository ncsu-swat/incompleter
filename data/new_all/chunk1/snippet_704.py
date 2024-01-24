# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53765719/filenotfounderror-in-python-during-arabic-text-analysis
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    _l_(408311)

except ImportError:
    pass

documents = [_c_(408314, _n_(408312, "open", lambda: open), _n_(408313, "f", lambda: f)) for f in _n_(408315, "text_files", lambda: text_files)]
_l_(408316)
tfidf = _c_(408321, _a_(408319, _c_(408318, _n_(408317, "TfidfVectorizer", lambda: TfidfVectorizer)), "fit_transform"), _n_(408320, "documents", lambda: documents))
_l_(408322)
# no need to normalize, since Vectorizer will return normalized tf-idf
pairwise_similarity = _n_(408323, "tfidf", lambda: tfidf) * _a_(408325, _n_(408324, "tfidf", lambda: tfidf), "T")
_l_(408326)