# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63280083/typeerror-expected-str-bytes-or-os-pathlike-object-not-list-convert
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import txt_to_html
    _l_(387540)

except ImportError:
    pass
try:
    import os
    _l_(387542)

except ImportError:
    pass
path = 'C:\\Users\\Sandy\\PycharmProjects\\untitled1'
_l_(387543)
text_files = [_n_(387544, "f", lambda: f) for f in _c_(387548, _a_(387546, _n_(387545, "os", lambda: os), "listdir"), _n_(387547, "path", lambda: path)) if _c_(387551, _a_(387550, _n_(387549, "f", lambda: f), "endswith"), '.log')]
_l_(387552)
_c_(387556, _a_(387554, _n_(387553, "txt_to_html", lambda: txt_to_html), "parse_txt"), _n_(387555, "text_files", lambda: text_files))
_l_(387557)