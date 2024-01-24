# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/9539156/typeerror-in-python-3-x
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Student:
    _l_(414997)

    '''Student class'''
    _l_(414968)

    name = None
    _l_(414969)
    id = 0
    _l_(414970)
    address = None
    _l_(414971)
    cgpa = None
    _l_(414972)

    def get_name():
        _l_(414975)

        aux = _n_(414973, "name", lambda: name)
        _l_(414974)
        return aux

    def set_name(n):
        _l_(414978)

        name = _n_(414976, "n", lambda: n)
        _l_(414977)

    def get_id():
        _l_(414981)

        aux = _n_(414979, "id", lambda: id)
        _l_(414980)
        return aux

    def set_id(i):
        _l_(414984)

        id = _n_(414982, "i", lambda: i)
        _l_(414983)

    def get_address():
        _l_(414987)

        aux = _n_(414985, "address", lambda: address)
        _l_(414986)
        return aux

    def set_address(a):
        _l_(414990)

        address = _n_(414988, "a", lambda: a)
        _l_(414989)

    def get_cgpa():
        _l_(414993)

        aux = _n_(414991, "cgpa", lambda: cgpa)
        _l_(414992)
        return aux

    def set_cgpa(c):
        _l_(414996)

        cgpa = _n_(414994, "c", lambda: c)
        _l_(414995)


#An object of Student class
jack = _c_(414999, _n_(414998, "Student", lambda: Student))
_l_(415000)

_c_(415003, _a_(415002, _n_(415001, "jack", lambda: jack), "set_name"), 'jacky')
_l_(415004)
_c_(415009, _n_(415005, "print", lambda: print), _c_(415008, _a_(415007, _n_(415006, "jack", lambda: jack), "get_name")))
_l_(415010)