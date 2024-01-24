# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76654972/filenotfound-error-in-python-3-even-though-i-see-the-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import nltk
    _l_(610040)

except ImportError:
    pass
try:
    from nltk.stem.porter import PorterStemmer
    _l_(610042)

except ImportError:
    pass
ps = _c_(610044, _n_(610043, "PorterStemmer", lambda: PorterStemmer))
_l_(610045)

list_stemmed_files = []
_l_(610046)
for i in _n_(610047, "filenames", lambda: filenames):
    _l_(610075)

    with _c_(610052, _n_(610048, "open", lambda: open), _c_(610051, _n_(610049, "str", lambda: str), _n_(610050, "i", lambda: i)),'r') as file:
        _l_(610074)

        readFile = _c_(610055, _a_(610054, _n_(610053, "file", lambda: file), "read"))
        _l_(610056)
        tokenized_file = _c_(610061, _a_(610059, _a_(610058, _n_(610057, "nltk", lambda: nltk), "tokenize"), "word_tokenize"), _n_(610060, "readFile", lambda: readFile))
        _l_(610062)
        stemmed_file = [_c_(610066, _a_(610064, _n_(610063, "ps", lambda: ps), "stem"), _n_(610065, "word", lambda: word)) for word in _n_(610067, "tokenized_file", lambda: tokenized_file)]
        _l_(610068)
        _c_(610072, _a_(610070, _n_(610069, "list_stemmed_files", lambda: list_stemmed_files), "append"), _n_(610071, "stemmed_file", lambda: stemmed_file))
        _l_(610073)