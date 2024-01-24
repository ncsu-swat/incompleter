# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63704863/attributeerror-at-str-object-has-no-attribute-get-in-danjo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Meta:
    _l_(348121)

    model = HomePageModel
    _l_(348119)
    fields = "__all__"
    _l_(348120)

def clean(self):
    _l_(348181)

    _c_(348126, _a_(348125, _n_(348122, "super", lambda: super)(_n_(348123, "HomePageForm", lambda: HomePageForm), _n_(348124, "self", lambda: self)), "clean"))
    _l_(348127)
    first_name = _c_(348131, _a_(348130, _a_(348129, _n_(348128, "self", lambda: self), "cleaned_data"), "get"), 'first_name')
    _l_(348132)
    try:
        _l_(348180)

        regex = _c_(348135, _a_(348134, _n_(348133, "re", lambda: re), "compile"), '[@_!#$%^&*()<>?/\|}{~:]')
        _l_(348136)
        flag_decimal = 0
        _l_(348137)
        flag_alpha = 0
        _l_(348138)
        if _c_(348141, _n_(348139, "len", lambda: len), _n_(348140, "first_name", lambda: first_name)) > 20:
            _l_(348145)

            raise _c_(348143, _n_(348142, "ValidationError", lambda: ValidationError), 'Fisrt Name can not be more than 20 characters')
            _l_(348144)
        if (_c_(348149, _a_(348147, _n_(348146, "regex", lambda: regex), "search"), _n_(348148, "first_name", lambda: first_name)) != None):
            _l_(348171)

            raise _c_(348151, _n_(348150, "ValidationError", lambda: ValidationError), 'Fisrt Name can not have a special character')
            _l_(348152)
        else:
            for char in _n_(348153, "first_name", lambda: first_name):
                _l_(348164)

                if _c_(348156, _a_(348155, _n_(348154, "char", lambda: char), "isdecimal")):
                    _l_(348158)

                    flag_decimal = 1
                    _l_(348157)
                if _c_(348161, _a_(348160, _n_(348159, "char", lambda: char), "isalpha")):
                    _l_(348163)

                    flag_alpha = 1
                    _l_(348162)
            if _n_(348165, "flag_decimal", lambda: flag_decimal) == 1 or _n_(348166, "flag_alpha", lambda: flag_alpha) == 0:
                _l_(348170)

                raise _c_(348168, _n_(348167, "ValidationError", lambda: ValidationError), 'Fisrt Name can not have a number')
                _l_(348169)
        aux = _n_(348172, "first_name", lambda: first_name)
        _l_(348173)
        return aux
    except _n_(348174, "ValidationError", lambda: ValidationError) as e:
        _l_(348179)

        _c_(348177, _n_(348175, "print", lambda: print), _n_(348176, "e", lambda: e))
        _l_(348178)