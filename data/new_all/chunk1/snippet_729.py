# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30230380/attributeerror-str-object-has-no-attribute-words
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from textblob import TextBlob as tb
    _l_(378328)

except ImportError:
    pass
try:
    import math
    _l_(378330)

except ImportError:
    pass

words={}
_l_(378331)
def tfidf(word, blob, bloblist):
    _l_(378341)

    aux = _c_(378335, _n_(378332, "tf", lambda: tf), _n_(378333, "word", lambda: word), _n_(378334, "blob", lambda: blob)) * _c_(378339, _n_(378336, "idf", lambda: idf), _n_(378337, "word", lambda: word), _n_(378338, "bloblist", lambda: bloblist))
    _l_(378340)
    return aux

def tf(word, blob):
    _l_(378352)

    aux = _c_(378346, _a_(378344, _a_(378343, _n_(378342, "blob", lambda: blob), "words"), "count"), _n_(378345, "word", lambda: word)) / _c_(378350, _n_(378347, "len", lambda: len), _a_(378349, _n_(378348, "blob", lambda: blob), "words"))
    _l_(378351)
    return aux

def n_containing(word, bloblist):
    _l_(378359)

    aux = _c_(378357, _n_(378353, "sum", lambda: sum), (1 for blob in _n_(378354, "bloblist", lambda: bloblist) if _n_(378355, "word", lambda: word) in _n_(378356, "blob", lambda: blob)))
    _l_(378358)
    return aux

def idf(word, bloblist):
    _l_(378371)

    aux = _c_(378369, _a_(378361, _n_(378360, "math", lambda: math), "log"), _c_(378364, _n_(378362, "len", lambda: len), _n_(378363, "bloblist", lambda: bloblist)) / (1 + _c_(378368, _n_(378365, "n_containing", lambda: n_containing), _n_(378366, "words", lambda: words), _n_(378367, "bloblist", lambda: bloblist))))
    _l_(378370)
    return aux

bloblist = _c_(378375, _a_(378374, _c_(378373, _n_(378372, "open", lambda: open), 'afterstopwords.csv', 'r'), "read"))
_l_(378376)

for i, blob in _c_(378379, _n_(378377, "enumerate", lambda: enumerate), _n_(378378, "bloblist", lambda: bloblist)):
    _l_(378413)

    _c_(378384, _n_(378380, "print", lambda: print), _c_(378383, _a_(378381, "Top words in document {}", "format"), _n_(378382, "i", lambda: i) + 1))
    _l_(378385)
    scores = {_n_(378386, "word", lambda: word): _c_(378391, _n_(378387, "tfidf", lambda: tfidf), _n_(378388, "word", lambda: word), _n_(378389, "blob", lambda: blob), _n_(378390, "bloblist", lambda: bloblist)) for word in _a_(378393, _n_(378392, "blob", lambda: blob), "words")}
    _l_(378394)
    sorted_words = _c_(378400, _n_(378395, "sorted", lambda: sorted), _c_(378398, _a_(378397, _n_(378396, "scores", lambda: scores), "items")), key=lambda x: _n_(378399, "x", lambda: x)[1], reverse=True)
    _l_(378401)
    for word, score in _n_(378402, "sorted_words", lambda: sorted_words)[:3]:
        _l_(378412)

        _c_(378410, _n_(378403, "print", lambda: print), _c_(378409, _a_(378404, "\tWord: {}, TF-IDF: {}", "format"), _n_(378405, "word", lambda: word), _c_(378408, _n_(378406, "round", lambda: round), _n_(378407, "score", lambda: score), 5)))
        _l_(378411)