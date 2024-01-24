# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49465554/try-to-build-webserver-and-read-html-file-with-typeerror-must-be-str-not-byte
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
file = _c_(705328, _n_(705327, "open", lambda: open), 'index.html', 'r')
_l_(705329)
index_content += _c_(705332, _a_(705331, _n_(705330, "file", lambda: file), "read"))
_l_(705333)
_c_(705336, _a_(705335, _n_(705334, "file", lambda: file), "close"))
_l_(705337)