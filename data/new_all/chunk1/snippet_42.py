# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39146039/pickle-typeerror-a-bytes-like-object-is-required-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
fname1 = "auth_cache_%s" % _n_(415839, "username", lambda: username)
_l_(415840)
fname=_c_(415843, _a_(415842, _n_(415841, "fname1", lambda: fname1), "encode"), encoding='utf_8')
_l_(415844)
#fname=fname1.encode()
if _c_(415849, _a_(415847, _a_(415846, _n_(415845, "os", lambda: os), "path"), "isfile"), _n_(415848, "fname", lambda: fname),) and _n_(415850, "cached", lambda: cached):
    _l_(415872)

    response = _c_(415856, _a_(415852, _n_(415851, "pickle", lambda: pickle), "load"), _c_(415855, _n_(415853, "open", lambda: open), _n_(415854, "fname", lambda: fname)))
    _l_(415857)
else:
    response = _c_(415860, _a_(415859, _n_(415858, "self", lambda: self), "heartbeat"))
    _l_(415861)
    f = _c_(415864, _n_(415862, "open", lambda: open), _n_(415863, "fname", lambda: fname),"w")
    _l_(415865)
    _c_(415870, _a_(415867, _n_(415866, "pickle", lambda: pickle), "dump"), _n_(415868, "response", lambda: response), _n_(415869, "f", lambda: f))
    _l_(415871)