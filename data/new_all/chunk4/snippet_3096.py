# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46750783/why-does-django-assertformerror-throw-a-typeerror-argument-of-type-property-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class SessID(_a_(609139, _n_(609138, "forms", lambda: forms), "Field")):
    _l_(609168)


    def validate(self, session_id):
        _l_(609167)

        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        _c_(609143, _a_(609141, _n_(609140, "super", lambda: super)(), "validate"), _n_(609142, "session_id", lambda: session_id))
        _l_(609144)
        if _c_(609147, _n_(609145, "len", lambda: len), _n_(609146, "session_id", lambda: session_id)) < 32 > _c_(609150, _n_(609148, "len", lambda: len), _n_(609149, "session_id", lambda: session_id)):
            _l_(609156)

            raise _c_(609154, _n_(609151, "ValidationError", lambda: ValidationError), _c_(609153, _n_(609152, "_", lambda: _), 'The Session ID needs to be exactly 32 characters long'),
                                  code = 'sessid wrong length'
                                  )
            _l_(609155)
        if not _c_(609160, _a_(609158, _n_(609157, "re", lambda: re), "match"), "^[A-Za-z0-9]*$", _n_(609159, "session_id", lambda: session_id)):
            _l_(609166)

            raise _c_(609164, _n_(609161, "ValidationError", lambda: ValidationError), _c_(609163, _n_(609162, "_", lambda: _), 'The Session ID should only have letters and numbers, no special characters'),
                                  code = 'sessid not alphanumeric'
                                  )        
            _l_(609165)        


class ResetSessID(_a_(609170, _n_(609169, "forms", lambda: forms), "ModelForm")):
    _l_(609216)

    new_sessid = _c_(609172, _n_(609171, "SessID", lambda: SessID))
    _l_(609173)
    #forms.CharField(widget=forms.TextInput(attrs={'class':'special', 'size': '32'})                        )

    def __init__(self, *args, **kwargs):
        _l_(609205)

        _c_(609180, _a_(609177, _n_(609174, "super", lambda: super)(_n_(609175, "ResetSessID", lambda: ResetSessID), _n_(609176, "self", lambda: self)), "__init__"), *_n_(609178, "args", lambda: args), **_n_(609179, "kwargs", lambda: kwargs))
        _l_(609181)
        _c_(609184, _a_(609183, _n_(609182, "stdlogger", lambda: stdlogger), "info"), "init of ResetSessID")
        _l_(609185)
        #print("dir")#, self.fields.items['new_sessid'])
        if _c_(609188, _a_(609187, _n_(609186, "kwargs", lambda: kwargs), "get"), 'instance'):
            _l_(609196)

            new_sessid = _a_(609190, _n_(609189, "kwargs", lambda: kwargs)['instance'], "new_essid")
            _l_(609191)
            _c_(609194, _a_(609193, _n_(609192, "stdlogger", lambda: stdlogger), "info"), "inner kwargs loop")
            _l_(609195)
        aux = _c_(609203, _a_(609200, _n_(609197, "super", lambda: super)(_n_(609198, "ResetSessID", lambda: ResetSessID), _n_(609199, "self", lambda: self)), "__init__"), *_n_(609201, "args", lambda: args), **_n_(609202, "kwargs", lambda: kwargs))
        _l_(609204)
        return aux

    class Meta:
        _l_(609208)

        model = PoeAccount
        _l_(609206)
        exclude = ("acc_name", "sessid")
        _l_(609207)

    def clean(self):
        _l_(609215)

        if 'reg_button' in _a_(609210, _n_(609209, "self", lambda: self), "data"):
            _l_(609214)

            _c_(609212, _n_(609211, "print", lambda: print), "amazing")
            _l_(609213)