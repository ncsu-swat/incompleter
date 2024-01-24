# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50119091/typeerror-unhashable-type-list-in-python-nltk
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from nltk.corpus import stopwords
    _l_(385240)

except ImportError:
    pass
try:
    from nltk.tokenize import word_tokenize
    _l_(385242)

except ImportError:
    pass
try:
    from nltk.stem import PorterStemmer
    _l_(385244)

except ImportError:
    pass
try:
    import re
    _l_(385246)

except ImportError:
    pass

fo = _c_(385248, _n_(385247, "open", lambda: open), 'cran.all.1400', 'r+')
_l_(385249)
contents = _c_(385252, _a_(385251, _n_(385250, "fo", lambda: fo), "read"))
_l_(385253)
docs = _c_(385256, _a_(385255, _n_(385254, "re", lambda: re), "split"), r'\.I[\s][\d]*')
_l_(385257)

stop_words = _c_(385262, _n_(385258, "set", lambda: set), _c_(385261, _a_(385260, _n_(385259, "stopwords", lambda: stopwords), "words"), 'english'))
_l_(385263)

tokens = []
_l_(385264)
for each in _n_(385265, "docs", lambda: docs):
    _l_(385273)

    _c_(385271, _a_(385267, _n_(385266, "tokens", lambda: tokens), "append"), _c_(385270, _n_(385268, "word_tokenize", lambda: word_tokenize), _n_(385269, "eac", lambda: eac)))
    _l_(385272)

s_words = [_n_(385274, "w", lambda: w) for w in _n_(385275, "tokens", lambda: tokens) if not _n_(385276, "w", lambda: w) in _n_(385277, "stop_words", lambda: stop_words)]
_l_(385278)
_c_(385281, _n_(385279, "print", lambda: print), _n_(385280, "s_words", lambda: s_words))
_l_(385282)