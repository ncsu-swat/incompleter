# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52789603/typeerror-int-object-is-not-callable-in-python-3-when-calling-logging-info
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import logging
    _l_(381159)

except ImportError:
    pass
_c_(381164, _a_(381161, _n_(381160, "logging", lambda: logging), "basicConfig"), level=_a_(381163, _n_(381162, "logging", lambda: logging), "INFO"), format='%(asctime)s-%(message)s')
_l_(381165)

class employee:
    _l_(381201)


    def __init__(self,first,last):
        _l_(381182)

        _n_(381166, "self", lambda: self).first=_n_(381167, "first", lambda: first)
        _l_(381168)
        _n_(381169, "self", lambda: self).last=_n_(381170, "last", lambda: last)
        _l_(381171)

        _c_(381180, _a_(381173, _n_(381172, "logging", lambda: logging), "INFO"), _c_(381179, _a_(381174, 'Employee created: {} - {} ', "format"), _a_(381176, _n_(381175, "self", lambda: self), "fullname"), _a_(381178, _n_(381177, "self", lambda: self), "email")))
        _l_(381181)

    @_n_(381183, "property", lambda: property)
    def email(self):
        _l_(381191)

        aux = _c_(381189, _a_(381184, '{}.{}@email.com', "format"), _a_(381186, _n_(381185, "self", lambda: self), "first"),_a_(381188, _n_(381187, "self", lambda: self), "last"))
        _l_(381190)
        return aux
    @_n_(381192, "property", lambda: property)
    def fullname(self):
        _l_(381200)

        aux = _c_(381198, _a_(381193, '{} {}', "format"), _a_(381195, _n_(381194, "self", lambda: self), "first"),_a_(381197, _n_(381196, "self", lambda: self), "last"))
        _l_(381199)
        return aux

emp_1=_c_(381203, _n_(381202, "employee", lambda: employee), 'John','Doe')
_l_(381204)
emp_2=_c_(381206, _n_(381205, "employee", lambda: employee), 'John','Smith')
_l_(381207)