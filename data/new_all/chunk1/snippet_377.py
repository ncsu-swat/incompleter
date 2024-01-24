# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46052925/python3-multiple-inheritance-typeerror-object-init-takes-no-parameters
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ContactList(_n_(416759, "list", lambda: list)):
    _l_(416775)

    def search(self, name):
        _l_(416774)

        """Return all contacts that contain the search value
        in their name."""
        matching_contacts = []
        _l_(416760)
        for contact in _n_(416761, "self", lambda: self):
            _l_(416771)

            if _n_(416762, "name", lambda: name) in _a_(416764, _n_(416763, "contact", lambda: contact), "name"):
                _l_(416770)

                _c_(416768, _a_(416766, _n_(416765, "matching_contacts", lambda: matching_contacts), "append"), _n_(416767, "contact", lambda: contact))
                _l_(416769)
        aux = _n_(416772, "matching_contacts", lambda: matching_contacts)
        _l_(416773)
        return aux


class Contact:
    _l_(416800)

    all_contacts = _c_(416777, _n_(416776, "ContactList", lambda: ContactList))
    _l_(416778)

    def __init__(self, name="", email="", **kwargs):
        _l_(416799)

        _c_(416782, _a_(416780, _n_(416779, "super", lambda: super)(), "__init__"), **_n_(416781, "kwargs", lambda: kwargs))
        _l_(416783)
        _n_(416784, "self", lambda: self).name = _n_(416785, "name", lambda: name)
        _l_(416786)
        _n_(416787, "self", lambda: self).email = _n_(416788, "email", lambda: email)
        _l_(416789)
        _c_(416794, _a_(416792, _a_(416791, _n_(416790, "Contact", lambda: Contact), "all_contacts"), "append"), _n_(416793, "self", lambda: self))
        _l_(416795)
        _c_(416797, _n_(416796, "print", lambda: print), "Cotact")
        _l_(416798)


class AddressHolder:
    _l_(416822)

    def __init__(self, street="", city="", state="", code="", **kwargs):
        _l_(416821)

        _c_(416804, _a_(416802, _n_(416801, "super", lambda: super)(), "__init__"), **_n_(416803, "kwargs", lambda: kwargs))
        _l_(416805)
        _n_(416806, "self", lambda: self).street = _n_(416807, "street", lambda: street)
        _l_(416808)
        _n_(416809, "self", lambda: self).city = _n_(416810, "city", lambda: city)
        _l_(416811)
        _n_(416812, "self", lambda: self).state = _n_(416813, "state", lambda: state)
        _l_(416814)
        _n_(416815, "self", lambda: self).code = _n_(416816, "code", lambda: code)
        _l_(416817)
        _c_(416819, _n_(416818, "print", lambda: print), "AddressHolder")
        _l_(416820)


class Friend(_n_(416823, "Contact", lambda: Contact), _n_(416824, "AddressHolder", lambda: AddressHolder)):
    _l_(416837)

    # case# 1
    # def __init__(self, phone="", **kwargs):
    #     self.phone = phone
    #     super().__init__(**kwargs)
    #     print("Friend")

    # case# 2
    def __init__(self, **kwargs):
        _l_(416836)

        _n_(416825, "self", lambda: self).phone = _n_(416826, "kwargs", lambda: kwargs)["phone"]
        _l_(416827)
        _c_(416831, _a_(416829, _n_(416828, "super", lambda: super)(), "__init__"), **_n_(416830, "kwargs", lambda: kwargs))
        _l_(416832)
        _c_(416834, _n_(416833, "print", lambda: print), "Friend")
        _l_(416835)


if _n_(416838, "__name__", lambda: __name__) == "__main__":
    _l_(416842)

    friend = _c_(416840, _n_(416839, "Friend", lambda: Friend), phone="01234567",
        name="My Friend",
        email="myfriend@example.net",
        street="Street",
        city="City",
        state="State",
        code="0123")
    _l_(416841)