# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68362936/python-using-classes-as-default-values-of-another-class-attribute-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class RateResponse(_n_(468113, "BaseModel", lambda: BaseModel)):
    _l_(468120)


    def __init__(self, 
        provider=_c_(468115, _n_(468114, "Provider", lambda: Provider))
    ):
        _l_(468119)


        _n_(468116, "self", lambda: self).provider = _n_(468117, "provider", lambda: provider)
        _l_(468118)


class Provider(_n_(468121, "ObjectListModel", lambda: ObjectListModel)):
    _l_(468135)


    def __init__(self):
        _l_(468129)


        _c_(468127, _a_(468125, _n_(468122, "super", lambda: super)(_n_(468123, "Provider", lambda: Provider), _n_(468124, "self", lambda: self)), "__init__"), list=[], listObject=_n_(468126, "ProviderItem", lambda: ProviderItem))
        _l_(468128)

    @_n_(468130, "property", lambda: property)
    def providerItems(self):
        _l_(468134)

        aux = _a_(468132, _n_(468131, "self", lambda: self), "list")
        _l_(468133)
        return aux

class ProviderItem(_n_(468136, "BaseModel", lambda: BaseModel)):
    _l_(468149)


    def __init__(self,
        code=None,
        notification=_c_(468137, Notification),
        service=_c_(468138, Service)
    ):
        _l_(468148)


        _n_(468139, "self", lambda: self).code = _n_(468140, "code", lambda: code)
        _l_(468141)
        _n_(468142, "self", lambda: self).notification = _n_(468143, "notification", lambda: notification)
        _l_(468144)
        _n_(468145, "self", lambda: self).service = _n_(468146, "service", lambda: service)
        _l_(468147)