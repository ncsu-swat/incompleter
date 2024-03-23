# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53765719/filenotfounderror-in-python-during-arabic-text-analysis
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    _l_(398671)

except ImportError:
    pass

text_files= r"C:\Users\Nujou\Desktop\Master\thesis\corpora\modified Corpora\Training set\5K\ST"
_l_(398672)
for f in _n_(398673, "text_files", lambda: text_files):
    _l_(398680)

    documents= _c_(398678, _a_(398677, _c_(398676, _n_(398674, "open", lambda: open), _n_(398675, "f", lambda: f), 'r', encoding='utf-8-sig'), "read"))
    _l_(398679)
tfidf = _c_(398685, _a_(398683, _c_(398682, _n_(398681, "TfidfVectorizer", lambda: TfidfVectorizer)), "fit_transform"), _n_(398684, "documents", lambda: documents))
_l_(398686)
# no need to normalize, since Vectorizer will return normalized tf-idf
pairwise_similarity = _n_(398687, "tfidf", lambda: tfidf) * _a_(398689, _n_(398688, "tfidf", lambda: tfidf), "T")
_l_(398690)