# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52140360/typeerror-supertype-obj-obj-must-be-an-instance-or-subtype-of-type
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class RequestItem(_a_(463694, _n_(463693, "generic", lambda: generic), "CreateView")):
    _l_(463761)

    model = UserNotification
    _l_(463695)
    fields = ['Name', 'Mobile_No', 'Proof']
    _l_(463696)

    def get_form(self, form_class=None):
        _l_(463727)

        if _n_(463697, "form_class", lambda: form_class) is None:
            _l_(463702)

            form_class = _c_(463700, _a_(463699, _n_(463698, "self", lambda: self), "get_form_class"))
            _l_(463701)
        form = _c_(463708, _a_(463706, _n_(463703, "super", lambda: super)(_n_(463704, "UserNotification", lambda: UserNotification), _n_(463705, "self", lambda: self)), "get_form"), _n_(463707, "form_class", lambda: form_class))
        _l_(463709)
        _a_(463711, _n_(463710, "form", lambda: form), "fields")['Name'].widget = _c_(463713, _n_(463712, "TextInput", lambda: TextInput), attrs={'placeholder': '*Enter your name'})
        _l_(463714)
        _a_(463716, _n_(463715, "form", lambda: form), "fields")['Mobile_No'].widget = _c_(463718, _n_(463717, "TextInput", lambda: TextInput), attrs={'placeholder': "*Enter your's mobile number to get a call back from angel"})
        _l_(463719)
        _a_(463721, _n_(463720, "form", lambda: form), "fields")['Proof'].widget = _c_(463723, _n_(463722, "TextInput", lambda: TextInput), attrs={'placeholder': '*enter proof you have for your lost item'})
        _l_(463724)
        aux = _n_(463725, "form", lambda: form)
        _l_(463726)
        return aux

    def form_valid(self, form):
        _l_(463760)

        _c_(463731, _n_(463728, "print", lambda: print), _a_(463730, _n_(463729, "self", lambda: self), "kwargs"))
        _l_(463732)

        _n_(463733, "self", lambda: self).object = _c_(463736, _a_(463735, _n_(463734, "form", lambda: form), "save"), commit=False)
        _l_(463737)
        qs = _c_(463745, _a_(463740, _a_(463739, _n_(463738, "Report_item", lambda: Report_item), "objects"), "filter"), id=_c_(463744, _a_(463743, _a_(463742, _n_(463741, "self", lambda: self), "kwargs"), "get"), "pk"))
        _l_(463746)
        _a_(463748, _n_(463747, "self", lambda: self), "object").user = _a_(463750, _n_(463749, "qs", lambda: qs)[0], "owner")
        _l_(463751)
        _c_(463755, _a_(463754, _a_(463753, _n_(463752, "self", lambda: self), "object"), "save"))
        _l_(463756)
        aux = _c_(463758, _n_(463757, "HttpResponse", lambda: HttpResponse), "<h1>Your request has been processed</h1>")
        _l_(463759)
        return aux