# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/31284240/typeerror-type-str-doesnt-support-the-buffer-api-in-asserttrue-in-testcase
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.test import TestCase
    _l_(473613)

except ImportError:
    pass
try:
    from .models import Artists
    _l_(473615)

except ImportError:
    pass

class TestArtist(_n_(473616, "TestCase", lambda: TestCase)):
    _l_(473645)

    def setUp(self):
        _l_(473623)

        _n_(473617, "self", lambda: self).artist = _c_(473621, _a_(473620, _a_(473619, _n_(473618, "Artists", lambda: Artists), "objects"), "create"), first_name = 'Ricky', 
        last_name ='Martin')
        _l_(473622)

    def test_existe_vista(self):
        _l_(473644)

        #print (self.client.get('/artists/%d' % self.artist.id))
        res = _c_(473630, _a_(473626, _a_(473625, _n_(473624, "self", lambda: self), "client"), "get"), '/artists/%d' % _a_(473629, _a_(473628, _n_(473627, "self", lambda: self), "artist"), "id"))
        _l_(473631)
        _c_(473636, _a_(473633, _n_(473632, "self", lambda: self), "assertEqual"), _a_(473635, _n_(473634, "res", lambda: res), "status_code"), 200)
        _l_(473637)
        _c_(473642, _a_(473639, _n_(473638, "self", lambda: self), "assertTrue"), 'Ricky' in _a_(473641, _n_(473640, "res", lambda: res), "content"))
        _l_(473643)