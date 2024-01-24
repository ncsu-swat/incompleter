# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70147078/attributeerror-type-object-student-has-no-attribute-name
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Student:
    _l_(620579)

    
    def __init__(self, name, uci_name, semester):
        _l_(620555)

        _n_(620546, "self", lambda: self).name = _n_(620547, "name", lambda: name)
        _l_(620548)
        _n_(620549, "self", lambda: self).uci_name = _n_(620550, "uci_name", lambda: uci_name)
        _l_(620551)
        _n_(620552, "self", lambda: self).semester = _n_(620553, "semester", lambda: semester)
        _l_(620554)
    
    def get_name(self) -> _n_(620556, "str", lambda: str):
        _l_(620560)

        aux = _a_(620558, _n_(620557, "self", lambda: self), "name")
        _l_(620559)
        return aux
    
    def get_uci_name(self) -> _n_(620561, "str", lambda: str):
        _l_(620565)

        aux = _a_(620563, _n_(620562, "self", lambda: self), "uci_name")
        _l_(620564)
        return aux
    
    def get_semester(self) -> _n_(620566, "int", lambda: int):
        _l_(620570)

        aux = _a_(620568, _n_(620567, "self", lambda: self), "semester")
        _l_(620569)
        return aux
    
    def __str__(self):
        _l_(620578)

        aux = f"{_a_(620572, _n_(620571, 'self', lambda: self), 'name')} [{_a_(620574, _n_(620573, 'self', lambda: self), 'uci_name')}] in Semester {_a_(620576, _n_(620575, 'self', lambda: self), 'semester')}"
        _l_(620577)
        return aux

student_tom = _c_(620581, _n_(620580, "Student", lambda: Student), "Tom", "tom55", 3)
_l_(620582)
    
assert _c_(620588, _n_(620583, "isinstance", lambda: isinstance), _c_(620586, _n_(620584, "getattr", lambda: getattr), _n_(620585, "Student", lambda: Student), "name"), _n_(620587, "property", lambda: property))
_l_(620589)
assert _c_(620595, _n_(620590, "isinstance", lambda: isinstance), _c_(620593, _n_(620591, "getattr", lambda: getattr), _n_(620592, "Student", lambda: Student), "uci_name"), _n_(620594, "property", lambda: property))
_l_(620596)
assert _c_(620602, _n_(620597, "isinstance", lambda: isinstance), _c_(620600, _n_(620598, "getattr", lambda: getattr), _n_(620599, "Student", lambda: Student), "semester"), _n_(620601, "property", lambda: property))
_l_(620603)