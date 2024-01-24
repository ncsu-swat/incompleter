# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68362936/python-using-classes-as-default-values-of-another-class-attribute-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def getInstanceByString(classStr):
    _l_(464413)

    aux = _c_(464411, _c_(464409, _n_(464408, "globals", lambda: globals))[_n_(464410, "classStr", lambda: classStr)])
    _l_(464412)
    return aux


class RateResponse(_n_(464414, "BaseModel", lambda: BaseModel)):
    _l_(464421)


    def __init__(self, 
        provider=_c_(464416, _n_(464415, "getInstanceByString", lambda: getInstanceByString), 'Provider')
    ):
        _l_(464420)


        _n_(464417, "self", lambda: self).provider = _n_(464418, "provider", lambda: provider)
        _l_(464419)