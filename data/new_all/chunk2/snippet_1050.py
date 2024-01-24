# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49852919/python-used-the-decorator-typeerror-bilolgy-missing-1-required-positional-arg
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Base(_n_(442221, "object", lambda: object)):
    _l_(442240)

    """
    base class
    """
    def bilolgy(self, pre):
        _l_(442239)

        def animal(func):
            _l_(442236)

            def color(a):
                _l_(442233)

                _c_(442224, _n_(442222, "print", lambda: print), _n_(442223, "pre", lambda: pre))
                _l_(442225)
                _c_(442227, _n_(442226, "print", lambda: print), "Today is a good day")
                _l_(442228)
                _c_(442231, _n_(442229, "func", lambda: func), _n_(442230, "a", lambda: a))
                _l_(442232)
            aux = _n_(442234, "color", lambda: color)
            _l_(442235)

            return aux
        aux = _n_(442237, "animal", lambda: animal)
        _l_(442238)

        return aux


class Sub(_n_(442241, "Base", lambda: Base)):
    _l_(442250)

    """
    subclass
    """
    @_c_(442244, _a_(442243, _n_(442242, "Base", lambda: Base), "bilolgy"), pre="Cats")
    def cat(self, name):
        _l_(442249)

        _c_(442247, _n_(442245, "print", lambda: print), "This is a " + _n_(442246, "name", lambda: name))
        _l_(442248)


if _n_(442251, "__name__", lambda: __name__) == '__main__':
    _l_(442259)

    sub = _c_(442253, _n_(442252, "Sub", lambda: Sub))
    _l_(442254)
    _c_(442257, _a_(442256, _n_(442255, "sub", lambda: sub), "cat"), "cat")
    _l_(442258)