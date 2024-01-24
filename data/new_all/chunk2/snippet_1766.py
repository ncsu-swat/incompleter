# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57375527/success-redirect-to-profile-form-gives-typeerror-at-profile-join-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class UserProfileView(_n_(468845, "LoginRequiredMixin", lambda: LoginRequiredMixin), _n_(468846, "SuccessMessageMixin", lambda: SuccessMessageMixin), _n_(468847, "UpdateView", lambda: UpdateView)):
    _l_(468886)

    model = UserProfile
    _l_(468848)
    form_class = UserProfileChangeForm
    _l_(468849)
    success_url = _c_(468850, reverse_lazy, "user_profile:profile")
    _l_(468851)
    # success_url = "/success/"
    success_message = "Profile updated"
    _l_(468852)

    def get_object(self, *args, **kwargs):
        _l_(468857)

        aux = _a_(468855, _a_(468854, _n_(468853, "self", lambda: self), "request"), "user")
        _l_(468856)
        return aux

    def post(self, request, *args, **kwargs):
        _l_(468885)

        form = _c_(468864, _a_(468859, _n_(468858, "self", lambda: self), "form_class"), _a_(468861, _n_(468860, "request", lambda: request), "POST"), instance=_a_(468863, _n_(468862, "request", lambda: request), "user"))
        _l_(468865)
        if _c_(468868, _a_(468867, _n_(468866, "form", lambda: form), "is_valid")):
            _l_(468877)

            profile = _c_(468871, _a_(468870, _n_(468869, "form", lambda: form), "save"), commit=False)
            _l_(468872)
            _c_(468875, _a_(468874, _n_(468873, "profile", lambda: profile), "save"))
            _l_(468876)
        aux = _c_(468883, _n_(468878, "render", lambda: render), _n_(468879, "request", lambda: request), _a_(468881, _n_(468880, "self", lambda: self), "template_name"), {"form": _n_(468882, "form", lambda: form)})
        _l_(468884)

        return aux