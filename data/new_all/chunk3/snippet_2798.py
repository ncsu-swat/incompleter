# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62872059/typeerror-init-takes-3-positional-arguments-but-4-were-given-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from abc import ABCMeta, abstractmethod
    _l_(527051)

except ImportError:
    pass
class Book(_n_(527052, "object", lambda: object), metaclass=_n_(527053, "ABCMeta", lambda: ABCMeta)):
    _l_(527063)

    def __init__(self,title,author):
        _l_(527060)

        _n_(527054, "self", lambda: self).title=_n_(527055, "title", lambda: title)
        _l_(527056)
        _n_(527057, "self", lambda: self).author=_n_(527058, "author", lambda: author)   
        _l_(527059)   
    @_n_(527061, "abstractmethod", lambda: abstractmethod)
    def display():
        _l_(527062)

passclass MyBook(_n_(527064, "Book", lambda: Book)):
    _l_(527097)

    def __innit__(self,title,author,price):
        _l_(527074)

        _n_(527065, "self", lambda: self).title = _n_(527066, "title", lambda: title)
        _l_(527067)
        _n_(527068, "self", lambda: self).author = _n_(527069, "author", lambda: author)
        _l_(527070)
        _n_(527071, "self", lambda: self).price = _n_(527072, "price", lambda: price)    
        _l_(527073)    
    def display(self):
        _l_(527096)

        _c_(527080, _n_(527075, "print", lambda: print), _c_(527079, _a_(527076, "Title: {0}", "format"), _a_(527078, _n_(527077, "self", lambda: self), "title")))
        _l_(527081)
        _c_(527087, _n_(527082, "print", lambda: print), _c_(527086, _a_(527083, "Author: {0}", "format"), _a_(527085, _n_(527084, "self", lambda: self), "author")))
        _l_(527088)
        _c_(527094, _n_(527089, "print", lambda: print), _c_(527093, _a_(527090, "Price: {0}", "format"), _a_(527092, _n_(527091, "self", lambda: self), "price")))
        _l_(527095)
title=_c_(527099, _n_(527098, "input", lambda: input))
_l_(527100)
author=_c_(527102, _n_(527101, "input", lambda: input))
_l_(527103)
price=_c_(527107, _n_(527104, "int", lambda: int), _c_(527106, _n_(527105, "input", lambda: input)))
_l_(527108)
new_novel = _c_(527113, _n_(527109, "MyBook", lambda: MyBook), _n_(527110, "title", lambda: title),_n_(527111, "author", lambda: author),_n_(527112, "price", lambda: price))
_l_(527114)
_c_(527117, _a_(527116, _n_(527115, "new_novel", lambda: new_novel), "display"))
_l_(527118)