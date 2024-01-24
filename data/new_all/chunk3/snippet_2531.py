# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73118140/attributeerror-obj-2-object-has-no-attribute-var-1-getattr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class obj_1:
    _l_(561130)

    def __init__(self):
        _l_(561115)

        _n_(561111, "self", lambda: self).var_1 = 'Hello'
        _l_(561112)
        _n_(561113, "self", lambda: self).var_2 = 'World'
        _l_(561114)


    def get_id(self):
        _l_(561125)

        i = _a_(561117, _n_(561116, "self", lambda: self), "var_1")
        _l_(561118)
        j = _a_(561120, _n_(561119, "self", lambda: self), "var_2")       
        _l_(561121)       
        aux = _n_(561122, "i", lambda: i), _n_(561123, "j", lambda: j)
        _l_(561124)
        return aux

    def vw(self):
        _l_(561129)

        _c_(561127, _n_(561126, "print", lambda: print), 'Hello..')
        _l_(561128)

class obj_2:
    _l_(561158)

    def __init__(self):
        _l_(561132)

        pass
        _l_(561131)


    def r_data(self):
        _l_(561150)

        _c_(561134, _n_(561133, "print", lambda: print), 'called r_data')
        _l_(561135)
        x, y = _c_(561140, _c_(561138, _n_(561136, "getattr", lambda: getattr), _n_(561137, "obj_1", lambda: obj_1), "get_id"), _n_(561139, "self", lambda: self))
        _l_(561141)

        _c_(561144, _n_(561142, "print", lambda: print), 'x > ', _n_(561143, "x", lambda: x))
        _l_(561145)
        _c_(561148, _n_(561146, "print", lambda: print), 'y > ', _n_(561147, "y", lambda: y))
        _l_(561149)

    def rd(self):
        _l_(561157)

        _c_(561155, _c_(561153, _n_(561151, "getattr", lambda: getattr), _n_(561152, "obj_1", lambda: obj_1), 'vw'), _n_(561154, "self", lambda: self))
        _l_(561156)

if _n_(561159, "__name__", lambda: __name__) == '__main__':
    _l_(561167)

    ob = _c_(561161, _n_(561160, "obj_2", lambda: obj_2))
    _l_(561162)
    _c_(561165, _a_(561164, _n_(561163, "ob", lambda: ob), "r_data"))
    _l_(561166)