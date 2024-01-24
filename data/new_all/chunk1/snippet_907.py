# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45860455/bottlepy-throws-typeerror-after-changing-server-to-cheroot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bottle import Bottle, run
    _l_(396826)

except ImportError:
    pass
app = _c_(396828, _n_(396827, "Bottle", lambda: Bottle))
_l_(396829)

options = {
'certfile':'cacert.pem',
'keyfile':'privkey.pem',
}
_l_(396830)

_c_(396834, _n_(396831, "run", lambda: run), _n_(396832, "app", lambda: app), host='localhost', port=8080, debug=True, server='cheroot', options=_n_(396833, "options", lambda: options))
_l_(396835)