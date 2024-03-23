# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53765719/filenotfounderror-in-python-during-arabic-text-analysis
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    _l_(393201)

except ImportError:
    pass
try:
    import os
    _l_(393203)

except ImportError:
    pass

text_files= _c_(393206, _a_(393205, _n_(393204, "os", lambda: os), "listdir"), r"C:\Users\Nujou\Desktop\Master\thesis\corpora\modified Corpora\Training set\5K\ST")
_l_(393207)

documents= []
_l_(393208)
for f in _n_(393209, "text_files", lambda: text_files):
    _l_(393221)

    file= _c_(393212, _n_(393210, "open", lambda: open), _n_(393211, "f", lambda: f), 'r', 'utf-8-sig')
    _l_(393213)
    _c_(393219, _a_(393215, _n_(393214, "documents", lambda: documents), "append"), _c_(393218, _a_(393217, _n_(393216, "file", lambda: file), "read")))
    _l_(393220)
tfidf = _c_(393226, _a_(393224, _c_(393223, _n_(393222, "TfidfVectorizer", lambda: TfidfVectorizer)), "fit_transform"), _n_(393225, "documents", lambda: documents))
_l_(393227)
# no need to normalize, since Vectorizer will return normalized tf-idf
pairwise_similarity = _n_(393228, "tfidf", lambda: tfidf) * _a_(393230, _n_(393229, "tfidf", lambda: tfidf), "T")
_l_(393231)