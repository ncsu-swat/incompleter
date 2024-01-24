# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/5184483/python-typeerror-on-regex
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
url = 'http://google.com'
_l_(383943)
linkregex = _c_(383946, _a_(383945, _n_(383944, "re", lambda: re), "compile"), '<a\s*href=[\'|"](.*?)[\'"].*?>')
_l_(383947)
m = _c_(383952, _a_(383950, _a_(383949, _n_(383948, "urllib", lambda: urllib), "request"), "urlopen"), _n_(383951, "url", lambda: url))
_l_(383953)
msg = _c_(383956, _a_(383955, _n_(383954, "m", lambda: m), "read"))
_l_(383957)
links = _c_(383961, _a_(383959, _n_(383958, "linkregex", lambda: linkregex), "findall"), _n_(383960, "msg", lambda: msg))
_l_(383962)