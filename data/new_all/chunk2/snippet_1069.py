# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47081700/fitting-tfidfvectorizer-attributeerror-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import nltk
    _l_(472374)

except ImportError:
    pass
try:
    import numpy as np
    _l_(472376)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(472378)

except ImportError:
    pass
try:
    from sklearn.feature_extraction.text import CountVectorizer
    _l_(472380)

except ImportError:
    pass
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    _l_(472382)

except ImportError:
    pass

# Make tokens per line

dataset = _c_(472385, _a_(472384, _n_(472383, "pd", lambda: pd), "read_csv"), 'Cleansed Data.csv', delimiter=';', encoding='latin1')
_l_(472386)
tokens = _c_(472391, _a_(472388, _n_(472387, "dataset", lambda: dataset)['Description'], "apply"), _a_(472390, _n_(472389, "nltk", lambda: nltk), "word_tokenize"))
_l_(472392)
tokens_line = _c_(472404, _a_(472394, _n_(472393, "pd", lambda: pd), "DataFrame"), _c_(472403, _a_(472399, _c_(472398, _a_(472396, _n_(472395, "np", lambda: np), "array"), _n_(472397, "tokens", lambda: tokens)), "reshape"), _c_(472402, _n_(472400, "len", lambda: len), _n_(472401, "tokens", lambda: tokens)), 1), 
columns=['tokens'])
_l_(472405)
tokens_line_lists = _c_(472409, _a_(472408, _a_(472407, _n_(472406, "tokens_line", lambda: tokens_line), "values"), "tolist"))    
_l_(472410)    

# Get unique tokens

Filename = _c_(472412, _n_(472411, "open", lambda: open), 'descriptions for tokens.txt')
_l_(472413)
vectorizer = _c_(472415, _n_(472414, "CountVectorizer", lambda: CountVectorizer))
_l_(472416)
dtm = _c_(472420, _a_(472418, _n_(472417, "vectorizer", lambda: vectorizer), "fit_transform"), _n_(472419, "Filename", lambda: Filename))
_l_(472421)
vocab = _c_(472424, _a_(472423, _n_(472422, "vectorizer", lambda: vectorizer), "get_feature_names"))
_l_(472425)
tokens_unique = _c_(472437, _a_(472427, _n_(472426, "pd", lambda: pd), "DataFrame"), _c_(472436, _a_(472432, _c_(472431, _a_(472429, _n_(472428, "np", lambda: np), "array"), _n_(472430, "vocab", lambda: vocab)), "reshape"), _c_(472435, _n_(472433, "len", lambda: len), _n_(472434, "vocab", lambda: vocab)), 1), 
columns=['tokens'])
_l_(472438)

#TF-IDF Vectoriser

tfidf_vectoriser = _c_(472441, _n_(472439, "TfidfVectorizer", lambda: TfidfVectorizer), max_df=0.8, max_features=20000, 
min_df=0.2, use_idf=True, tokenizer=_n_(472440, "tokens_unique", lambda: tokens_unique), ngram_range=(1,3))
_l_(472442)

tfidf_matrix = _c_(472446, _a_(472444, _n_(472443, "tfidf_vectoriser", lambda: tfidf_vectoriser), "fit_transform"), _n_(472445, "tokens_line", lambda: tokens_line))
_l_(472447)