# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50669942/typeerror-at-accounts-register-init-got-an-unexpected-keyword-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class RegisterView(_n_(465563, "CreateView", lambda: CreateView)):
    _l_(465584)

    form_class = UserRegistrationForm
    _l_(465564)
    template_name = 'registration/register.html'
    _l_(465565)
    success_url = '/'
    _l_(465566)

    def dispatch(self, *args, **kwargs):
        _l_(465583)

        if _a_(465570, _a_(465569, _a_(465568, _n_(465567, "self", lambda: self), "request"), "user"), "is_authenticated"):
            _l_(465582)

            aux = _c_(465572, _n_(465571, "redirect", lambda: redirect), '/login')
            _l_(465573)
            return aux
        else:
            aux = _c_(465580, _a_(465577, _n_(465574, "super", lambda: super)(_n_(465575, "RegisterView", lambda: RegisterView), _n_(465576, "self", lambda: self)), "dispatch"), *_n_(465578, "args", lambda: args), **_n_(465579, "kwargs", lambda: kwargs))
            _l_(465581)
            return aux