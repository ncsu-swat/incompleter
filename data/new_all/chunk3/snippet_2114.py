# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63105190/how-to-resolve-typeerror-init-got-an-unexpected-keyword-argument-attrs
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django import forms
    _l_(522687)

except ImportError:
    pass
try:
    from phonenumber_field.formfields import PhoneNumberField
    _l_(522689)

except ImportError:
    pass



class UserAccount(_a_(522691, _n_(522690, "forms", lambda: forms), "Form")):
    _l_(522733)


    name = _c_(522697, _a_(522693, _n_(522692, "forms", lambda: forms), "CharField"), widget=_c_(522696, _a_(522695, _n_(522694, "forms", lambda: forms), "TextInput"), attrs={'class':'form-control',     'placeholder':'First Name'}))
    _l_(522698)
    last_name = _c_(522704, _a_(522700, _n_(522699, "forms", lambda: forms), "CharField"), widget=_c_(522703, _a_(522702, _n_(522701, "forms", lambda: forms), "TextInput"), attrs={'class':'form-control', 'placeholder':'Surname'}))
    _l_(522705)
    phone = _c_(522710, _n_(522706, "PhoneNumberField", lambda: PhoneNumberField), widget=_c_(522709, _a_(522708, _n_(522707, "forms", lambda: forms), "TextInput"), attrs={'class':'form-control', 'placeholder':'Phone Number'}))
    _l_(522711)
    email = _c_(522717, _a_(522713, _n_(522712, "forms", lambda: forms), "CharField"), widget=_c_(522716, _a_(522715, _n_(522714, "forms", lambda: forms), "EmailField"), attrs={'class':'form-control', 'placeholder':'Email'}))
    _l_(522718)
    password = _c_(522724, _a_(522720, _n_(522719, "forms", lambda: forms), "CharField"), widget=_c_(522723, _a_(522722, _n_(522721, "forms", lambda: forms), "PasswordInput"), attrs={'class':'form-control', 'placeholder':'Password'}))
    _l_(522725)
    verify_password = _c_(522731, _a_(522727, _n_(522726, "forms", lambda: forms), "CharField"), widget=_c_(522730, _a_(522729, _n_(522728, "forms", lambda: forms), "PasswordInput"), attrs={'class':'form-control', 'placeholder':'verify password'}))
    _l_(522732)