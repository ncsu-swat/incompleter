# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66085361/i-am-getting-an-error-when-i-try-to-use-a-setter-the-error-message-is-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
raise_amt = 1.04
_l_(597530)

def __init__(self, first, last, pay):
    _l_(597540)

    _n_(597531, "self", lambda: self).first = _n_(597532, "first", lambda: first)
    _l_(597533)
    _n_(597534, "self", lambda: self).last = _n_(597535, "last", lambda: last)
    _l_(597536)

    _n_(597537, "self", lambda: self).pay = _n_(597538, "pay", lambda: pay)
    _l_(597539)

def fullname(self):
    _l_(597548)

    aux = _c_(597546, _a_(597541, '{} {}', "format"), _a_(597543, _n_(597542, "self", lambda: self), "first"), _a_(597545, _n_(597544, "self", lambda: self), "last"))
    _l_(597547)
    return aux

@_n_(597549, "property", lambda: property)
def email(self):
    _l_(597557)

    aux = _c_(597555, _a_(597550, '{}.{}@email.com', "format"), _a_(597552, _n_(597551, "self", lambda: self), "first"), _a_(597554, _n_(597553, "self", lambda: self), "last"))
    _l_(597556)
    return aux

@_a_(597559, _n_(597558, "fullname", lambda: fullname), "setter")
def fullname(self,name):
    _l_(597570)

    first,last=_c_(597562, _a_(597561, _n_(597560, "name", lambda: name), "split"), " ")
    _l_(597563)
    _n_(597564, "self", lambda: self).first=_n_(597565, "first", lambda: first)
    _l_(597566)
    _n_(597567, "self", lambda: self).last=_n_(597568, "last", lambda: last)
    _l_(597569)