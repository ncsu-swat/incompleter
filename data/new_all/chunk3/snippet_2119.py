# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62953908/attributeerror-tuple-object-has-no-attribute-get-django
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django import forms
    _l_(567021)

except ImportError:
    pass
try:
    from .models import ModelClas
    _l_(567023)

except ImportError:
    pass

class FormClass(_a_(567025, _n_(567024, "forms", lambda: forms), "ModelForm")):
    _l_(567071)

    passw = _c_(567031, _a_(567027, _n_(567026, "forms", lambda: forms), "CharField"), widget=_c_(567030, _a_(567029, _n_(567028, "forms", lambda: forms), "PasswordInput")))
    _l_(567032)
    repass = _c_(567038, _a_(567034, _n_(567033, "forms", lambda: forms), "CharField"), widget=_c_(567037, _a_(567036, _n_(567035, "forms", lambda: forms), "PasswordInput")))
    _l_(567039)

    def clean(self):
        _l_(567066)

        _c_(567044, _a_(567043, _n_(567040, "super", lambda: super)(_n_(567041, "FormClass", lambda: FormClass), _n_(567042, "self", lambda: self)), "clean"))
        _l_(567045)
        inputpass = _c_(567049, _a_(567048, _a_(567047, _n_(567046, "self", lambda: self), "cleaned_data"), "get"), 'passw')
        _l_(567050)
        inputrepass = _c_(567054, _a_(567053, _a_(567052, _n_(567051, "self", lambda: self), "cleaned_data"), "get"), 'repass')
        _l_(567055)
        if _n_(567056, "inputpass", lambda: inputpass) != _n_(567057, "inputrepass", lambda: inputrepass):
            _l_(567062)

            raise _c_(567060, _a_(567059, _n_(567058, "forms", lambda: forms), "ValidationError"), "Password not matched. please type again.")
            _l_(567061)
        aux = _n_(567063, "inputpass", lambda: inputpass), _n_(567064, "inputrepass", lambda: inputrepass)
        _l_(567065)
        return aux

    class Meta:
        _l_(567070)

        model = _n_(567067, "ModelClas", lambda: ModelClas)
        _l_(567068)
        fields = '__all__'
        _l_(567069)