# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/5440485/typeerror-post-data-should-be-bytes-or-an-iterable-of-bytes-it-cannot-be-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
url = "http://example.com/index.php?app=core&module=global&section=login&do=process"
_l_(383619)
values = {"username" : _n_(383620, "USERNAME", lambda: USERNAME), 
          "password" : _n_(383621, "PASSWORD", lambda: PASSWORD)}
_l_(383622)
data = _c_(383627, _a_(383625, _a_(383624, _n_(383623, "urllib", lambda: urllib), "parse"), "urlencode"), _n_(383626, "values", lambda: values))
_l_(383628)
req = _c_(383634, _a_(383631, _a_(383630, _n_(383629, "urllib", lambda: urllib), "request"), "Request"), _n_(383632, "url", lambda: url), _n_(383633, "data", lambda: data))
_l_(383635)
_c_(383640, _a_(383638, _a_(383637, _n_(383636, "urllib", lambda: urllib), "request"), "urlopen"), _n_(383639, "req", lambda: req))
_l_(383641)