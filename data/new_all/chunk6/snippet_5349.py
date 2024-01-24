# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63013036/filenotfounderror-errno-2-no-such-file-or-directory-apempe-chunks-txt
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(345002)

except ImportError:
    pass
try:
    import codecs
    _l_(345004)

except ImportError:
    pass
try:
    import string, re
    _l_(345006)

except ImportError:
    pass
try:
    from pathlib import Path
    _l_(345008)

except ImportError:
    pass


path = "C:\\Users\\Desktop\\texts\\dataset"
_l_(345009)
text_files = _c_(345013, _a_(345011, _n_(345010, "os", lambda: os), "listdir"), _n_(345012, "path", lambda: path))
_l_(345014)

documents = [_c_(345019, _a_(345018, _c_(345017, _n_(345015, "open", lambda: open), _n_(345016, "f", lambda: f), encoding="utf-8"), "read")) for f in _n_(345020, "text_files", lambda: text_files)]
_l_(345021)
sparse_matrix = _c_(345025, _a_(345023, _n_(345022, "tfidf_vectorizer", lambda: tfidf_vectorizer), "fit_transform"), _n_(345024, "documents", lambda: documents))
_l_(345026)