# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/15005488/python3-3-typeerror-embedded-nul-character
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Page(_n_(443209, "Base", lambda: Base)):
    _l_(443226)

    """ The SQLAlchemy declarative model class for a Page object. """
    __tablename__ = 'pages'
    _l_(443210)
    id = _c_(443211, Column, Integer, primary_key=True)
    _l_(443212)
    name = _c_(443214, Column, _c_(443213, String, 40, convert_unicode=True), unique=True)
    _l_(443215)
    data = _c_(443217, Column, _c_(443216, String, 40, convert_unicode=True))
    _l_(443218)

    def __init__(self, name, data):
        _l_(443225)

        _n_(443219, "self", lambda: self).name = _n_(443220, "name", lambda: name)
        _l_(443221)
        _n_(443222, "self", lambda: self).data = _n_(443223, "data", lambda: data)
        _l_(443224)


class RootFactory(_n_(443227, "object", lambda: object)):
    _l_(443231)

    __acl__ = [ (Allow, Everyone, 'view'),
                (Allow, 'group:editors', 'edit') ]
    _l_(443228)
    def __init__(self, request):
        _l_(443230)

        pass
        _l_(443229)