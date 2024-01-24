# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54897849/circular-issue-attempt-to-send-form-url-encoded-data-causes-typeerror-cant-co
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
req = _c_(469730, _n_(469727, "Request", lambda: Request), _n_(469728, "url", lambda: url), method='POST', data={"ID": _n_(469729, "theId", lambda: theId)})
_l_(469731)
r = _c_(469734, _n_(469732, "urlopen", lambda: urlopen), _n_(469733, "req", lambda: req))
_l_(469735)