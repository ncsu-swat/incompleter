# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57096886/why-typeerror-str-object-is-not-callable-error-has-occurred-in-my-code
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def uppercase(func_one):
    _l_(372782)

    func_one = _c_(372776, _n_(372775, "func_one", lambda: func_one))
    _l_(372777)
    aux = _c_(372780, _a_(372779, _n_(372778, "func_one", lambda: func_one), "upper"))
    _l_(372781)
    return aux

def split(func_two):
    _l_(372790)

    func_two = _c_(372784, _n_(372783, "func_two", lambda: func_two))
    _l_(372785)
    aux = _c_(372788, _a_(372787, _n_(372786, "func_two", lambda: func_two), "split"))
    _l_(372789)
    return aux

@_n_(372791, "split", lambda: split)

@_n_(372792, "uppercase", lambda: uppercase)    
def CallFunction():
    _l_(372794)

    aux = "my string was in lower case"
    _l_(372793)
    return aux

res = _c_(372796, _n_(372795, "CallFunction", lambda: CallFunction))
_l_(372797)
_c_(372800, _n_(372798, "print", lambda: print), _n_(372799, "res", lambda: res))
_l_(372801)