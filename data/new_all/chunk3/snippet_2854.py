# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60878353/reading-json-object-typeerror-io-textiowrapper-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
feeds = []
_l_(553479)
i = 0
_l_(553480)
for feed in _n_(553481, "output", lambda: output)['posts']:
    _l_(553498)

    _n_(553482, "feed", lambda: feed)['id'] = _n_(553483, "i", lambda: i)
    _l_(553484)
    _c_(553490, _n_(553485, "print", lambda: print), _n_(553486, "feed", lambda: feed)['id'], _c_(553489, _n_(553487, "str", lambda: str), _n_(553488, "feed", lambda: feed)['title']))
    _l_(553491)
    i += 1
    _l_(553492)
    _c_(553496, _a_(553494, _n_(553493, "feeds", lambda: feeds), "append"), _n_(553495, "feed", lambda: feed))
    _l_(553497)