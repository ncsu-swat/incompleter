# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55775131/nltk-package-returns-typeerror-lazycorpusloader-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import nltk.corpus as stopwords
    _l_(563405)

except ImportError:
    pass
try:
    import nltk
    _l_(563407)

except ImportError:
    pass
_c_(563410, _a_(563409, _n_(563408, "nltk", lambda: nltk), "download"), "stopwords")
_l_(563411)
sw = _c_(563414, _a_(563413, _n_(563412, "stopwords", lambda: stopwords), "words"), 'english')
_l_(563415)