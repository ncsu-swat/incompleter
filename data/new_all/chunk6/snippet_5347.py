# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63013036/filenotfounderror-errno-2-no-such-file-or-directory-apempe-chunks-txt
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(354241)

except ImportError:
    pass
try:
    import codecs
    _l_(354243)

except ImportError:
    pass
try:
    import string, re
    _l_(354245)

except ImportError:
    pass
try:
    from pathlib import Path
    _l_(354247)

except ImportError:
    pass


path = "C:\\Users\\Desktop\\texts\\dataset"
_l_(354248)
text_files = _c_(354252, _a_(354250, _n_(354249, "os", lambda: os), "listdir"), _n_(354251, "path", lambda: path))
_l_(354253)

documents = [_c_(354258, _a_(354257, _c_(354256, _n_(354254, "open", lambda: open), _n_(354255, "f", lambda: f), encoding="utf-8"), "read")) for f in _n_(354259, "text_files", lambda: text_files)]
_l_(354260)
sparse_matrix = _c_(354264, _a_(354262, _n_(354261, "tfidf_vectorizer", lambda: tfidf_vectorizer), "fit_transform"), _n_(354263, "documents", lambda: documents))
_l_(354265)