# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45250605/typeerror-object-takes-no-parameters-when-creating-an-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Human:
    _l_(441055)

    __name = None
    _l_(441053)
    __height = 0
    _l_(441054)

def __init__(self, name, height):
    _l_(441062)

    _n_(441056, "self", lambda: self).__name = _n_(441057, "name", lambda: name)
    _l_(441058)
    _n_(441059, "self", lambda: self).__height = _n_(441060, "height", lambda: height)
    _l_(441061)

def set_name(self, name):
    _l_(441066)

    _n_(441063, "self", lambda: self).__name = _n_(441064, "name", lambda: name)
    _l_(441065)

def get_name(self):
    _l_(441070)

    aux = _a_(441068, _n_(441067, "self", lambda: self), "__name")
    _l_(441069)
    return aux

def set_height(self, height):
    _l_(441074)

    _n_(441071, "self", lambda: self).__height = _n_(441072, "height", lambda: height)
    _l_(441073)

def get_height(self):
    _l_(441078)

    aux = _a_(441076, _n_(441075, "self", lambda: self), "__height")
    _l_(441077)
    return aux

def get_type(self):
    _l_(441082)

    _c_(441080, _n_(441079, "print", lambda: print), 'Human')
    _l_(441081)

def toString(self):
    _l_(441090)

    aux = _c_(441088, _a_(441083, '{} is {} cm tall.', "format"), _a_(441085, _n_(441084, "self", lambda: self), "__name"),
                                      _a_(441087, _n_(441086, "self", lambda: self), "__height"))
    _l_(441089)
    return aux

person = _c_(441092, _n_(441091, "Human", lambda: Human), 'Corey', 180)
_l_(441093)