# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59536926/typeerror-module-takes-at-most-2-arguments-3-given-code-taken-from-pluralsi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import student as student
    _l_(410515)

except ImportError:
    pass

students = []
_l_(410516)


class HighSchoolStudent(_n_(410517, "student", lambda: student)):
    _l_(410528)


    school_name = "Springfield High School"
    _l_(410518)

    def get_school_name(self):
        _l_(410520)

        aux = "This is a High School student"
        _l_(410519)
        return aux

    def get_name_capitalize(self):
        _l_(410527)

        original_value = _c_(410523, _a_(410522, _n_(410521, "super", lambda: super)(), "get_name_capitalize"))
        _l_(410524)
        aux = _n_(410525, "original_value", lambda: original_value) + "-HS"
        _l_(410526)
        return aux

...
_l_(410529)