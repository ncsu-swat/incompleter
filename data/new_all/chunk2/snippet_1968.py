# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74706590/attributeerror-type-object-adminsignupform-has-no-attribute-as-view-why-is
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class StudentSignUpView(_n_(446282, "CreateView", lambda: CreateView)):
    _l_(446308)

    model = User
    _l_(446283)
    form_class = StudentSignUpForm
    _l_(446284)
    template_name = 'registration/signup_form.html'
    _l_(446285)

    def get_context_data(self, **kwargs):
        _l_(446293)

        _n_(446286, "kwargs", lambda: kwargs)['user_type'] = 'student'
        _l_(446287)
        aux = _c_(446291, _a_(446289, _n_(446288, "super", lambda: super)(), "get_context_data"), **_n_(446290, "kwargs", lambda: kwargs))
        _l_(446292)
        return aux

    def form_valid(self, form):
        _l_(446307)

        user = _c_(446296, _a_(446295, _n_(446294, "form", lambda: form), "save"))
        _l_(446297)
        _c_(446302, _n_(446298, "login", lambda: login), _a_(446300, _n_(446299, "self", lambda: self), "request"), _n_(446301, "user", lambda: user))
        _l_(446303)
        aux = _c_(446305, _n_(446304, "redirect", lambda: redirect), 'students:quiz_list')
        _l_(446306)
        return aux
class AdminSignUpView(_n_(446309, "CreateView", lambda: CreateView)):
    _l_(446335)

    model = User
    _l_(446310)
    form_class = AdminSignUpForm
    _l_(446311)
    template_name = 'registration/signup_form.html'
    _l_(446312)
    
    def get_context_data(self, **kwargs):
        _l_(446320)

        _n_(446313, "kwargs", lambda: kwargs)['user_type'] = 'admin'
        _l_(446314)
        aux = _c_(446318, _a_(446316, _n_(446315, "super", lambda: super)(), "get_context_data"), **_n_(446317, "kwargs", lambda: kwargs))
        _l_(446319)
        return aux
    
    def form_valid(self, form):
        _l_(446334)

        user = _c_(446323, _a_(446322, _n_(446321, "form", lambda: form), "save"))
        _l_(446324)
        _c_(446329, _n_(446325, "login", lambda: login), _a_(446327, _n_(446326, "self", lambda: self), "request"), _n_(446328, "user", lambda: user))
        _l_(446330)
        aux = _c_(446332, _n_(446331, "redirect", lambda: redirect), 'home')
        _l_(446333)
        return aux