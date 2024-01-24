# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53947049/attributeerror-at-login-type-object-super-has-no-attribute-save
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class PostCreateView(_n_(427873, "LoginRequiredMixin", lambda: LoginRequiredMixin), _n_(427874, "CreateView", lambda: CreateView)):
    _l_(427889)

    model = Post
    _l_(427875)
    fields = ['title', 'content']
    _l_(427876)

    def form_valid(self, form):
        _l_(427888)

        _a_(427878, _n_(427877, "form", lambda: form), "instance").author = _a_(427881, _a_(427880, _n_(427879, "self", lambda: self), "request"), "user")
        _l_(427882)
        aux = _c_(427886, _a_(427884, _n_(427883, "super", lambda: super)(), "form_valid"), _n_(427885, "form", lambda: form))
        _l_(427887)
        return aux