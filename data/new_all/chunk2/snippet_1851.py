# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50669942/typeerror-at-accounts-register-init-got-an-unexpected-keyword-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class UserRegisterForm(_a_(469321, _n_(469320, "forms", lambda: forms), "ModelForm")):
    _l_(469402)


    password1 = _c_(469325, _a_(469322, forms, "CharField"), widget=_c_(469324, _a_(469323, forms, "PasswordInput"), attrs={'class': 'form-control', 'placeholder': 'Email'}))
    _l_(469326)
    password2 = _c_(469330, _a_(469327, forms, "CharField"), widget=_c_(469329, _a_(469328, forms, "PasswordInput"), attrs={'class': 'form-control', 'placeholder': 'Email'}))
    _l_(469331)

    class Meta:
        _l_(469334)

        model = User
        _l_(469332)
        fields = ['email', 'full_name']
        _l_(469333)

    def clean_password2(self):
        _l_(469356)

        password1 = _c_(469338, _a_(469337, _a_(469336, _n_(469335, "self", lambda: self), "cleaned_data"), "get"), 'password1')
        _l_(469339)
        password2 = _c_(469343, _a_(469342, _a_(469341, _n_(469340, "self", lambda: self), "cleaned_data"), "get"), 'password2')
        _l_(469344)

        if _n_(469345, "password1", lambda: password1) and _n_(469346, "password2", lambda: password2) and _n_(469347, "password1", lambda: password1) != _n_(469348, "password2", lambda: password2):
            _l_(469355)

            raise _c_(469351, _a_(469350, _n_(469349, "forms", lambda: forms), "ValidationError"), "Passwords do not match.")
            _l_(469352)
        else:
            aux = _n_(469353, "password2", lambda: password2)
            _l_(469354)
            return aux

    def clean_email(self):
        _l_(469378)

        email = _c_(469360, _a_(469359, _a_(469358, _n_(469357, "self", lambda: self), "cleaned_data"), "get"), 'email')
        _l_(469361)
        qs = _c_(469366, _a_(469364, _a_(469363, _n_(469362, "User", lambda: User), "objects"), "get"), email__iexact=_n_(469365, "email", lambda: email))
        _l_(469367)
        if _c_(469370, _a_(469369, _n_(469368, "qs", lambda: qs), "exists")):
            _l_(469377)

            raise _c_(469373, _a_(469372, _n_(469371, "forms", lambda: forms), "ValidationError"), "A user with this email already exists.")
            _l_(469374)
        else:
            aux = _n_(469375, "email", lambda: email)
            _l_(469376)
            return aux

    def save(self, commit=True):
        _l_(469401)

        user = _c_(469383, _a_(469382, _n_(469379, "super", lambda: super)(_n_(469380, "UserRegisterForm", lambda: UserRegisterForm), _n_(469381, "self", lambda: self)), "save"), commit=False)
        _l_(469384)
        _c_(469389, _a_(469386, _n_(469385, "user", lambda: user), "set_password"), _a_(469388, _n_(469387, "self", lambda: self), "cleaned_data")['password1'])
        _l_(469390)
        _n_(469391, "user", lambda: user).is_active = False
        _l_(469392)

        if _n_(469393, "commit", lambda: commit):
            _l_(469398)

            _c_(469396, _a_(469395, _n_(469394, "user", lambda: user), "save"))
            _l_(469397)
        aux = _n_(469399, "user", lambda: user)
        _l_(469400)
        return aux