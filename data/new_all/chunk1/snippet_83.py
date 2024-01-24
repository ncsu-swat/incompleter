# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/31895302/python3s-super-and-comprehensions-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class A(_n_(381095, "object", lambda: object)):
    _l_(381098)

    def __repr__(self):
        _l_(381097)

        aux = "hi!"  
        _l_(381096)  
        return aux  

class B(_n_(381099, "A", lambda: A)):
    _l_(381109)

    def __repr__(self):
        _l_(381108)

        aux = _c_(381106, _a_(381100, "", "join"), (_c_(381103, _a_(381102, _n_(381101, "super", lambda: super)(), "__repr__")) for i in _c_(381105, _n_(381104, "range", lambda: range), 2)))  
        _l_(381107)  
        return aux  

_c_(381113, _n_(381110, "repr", lambda: repr), _c_(381112, _n_(381111, "B", lambda: B)))
_l_(381114)
#output: <repr(<__main__.B at 0x7f70cf36fcc0>) failed: TypeError: super(type, obj): obj must be an instance or subtype of type>

class C(_n_(381115, "A", lambda: A)):
    _l_(381127)

    def __repr__(self):
        _l_(381126)

        s = ''
        _l_(381116)
        for i in _c_(381118, _n_(381117, "range", lambda: range), 4):
            _l_(381123)

            s += _c_(381121, _a_(381120, _n_(381119, "super", lambda: super)(), "__repr__"))
            _l_(381122)
        aux = _n_(381124, "s", lambda: s)     
        _l_(381125)     
        return aux     

_c_(381131, _n_(381128, "repr", lambda: repr), _c_(381130, _n_(381129, "C", lambda: C)))
_l_(381132)
#output: hi!hi!hi!hi!

class D(_n_(381133, "A", lambda: A)):
    _l_(381145)

    def __repr__(self):
        _l_(381144)

        aux = _c_(381142, _a_(381134, "", "join"), (_c_(381139, _a_(381138, _n_(381135, "super", lambda: super)(_n_(381136, "D", lambda: D),_n_(381137, "self", lambda: self)), "__repr__")) for i in _c_(381141, _n_(381140, "range", lambda: range), 4)))
        _l_(381143)
        return aux

_c_(381149, _n_(381146, "repr", lambda: repr), _c_(381148, _n_(381147, "D", lambda: D)))
_l_(381150)
#output: hi!hi!hi!hi!