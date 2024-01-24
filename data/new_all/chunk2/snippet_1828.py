# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51426359/django-typeerror-nonetype-object-is-not-iterable-dont-understand-why-obje
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib.auth.mixins import LoginRequiredMixin
    _l_(446337)

except ImportError:
    pass
try:
    from django.http import Http404, HttpResponseForbidden
    _l_(446339)

except ImportError:
    pass
try:
    from django.shortcuts import render
    _l_(446341)

except ImportError:
    pass
try:
    from django.urls import reverse
    _l_(446343)

except ImportError:
    pass
try:
    from django.views.generic.edit import FormMixin
    _l_(446345)

except ImportError:
    pass
try:
    from django.views.generic import DetailView, ListView
    _l_(446347)

except ImportError:
    pass
try:
    from .forms import ComposeForm
    _l_(446349)

except ImportError:
    pass
try:
    from .models import Thread, ChatMessage
    _l_(446351)

except ImportError:
    pass


class InboxView(_n_(446352, "LoginRequiredMixin", lambda: LoginRequiredMixin), _n_(446353, "ListView", lambda: ListView)):
    _l_(446364)

    template_name = 'qkchat/inbox.html'
    _l_(446354)
    def get_queryset(self):
        _l_(446363)

        aux = _c_(446361, _a_(446357, _a_(446356, _n_(446355, "Thread", lambda: Thread), "objects"), "by_user"), _a_(446360, _a_(446359, _n_(446358, "self", lambda: self), "request"), "user"))
        _l_(446362)
        return aux

class ThreadView(_n_(446365, "LoginRequiredMixin", lambda: LoginRequiredMixin), _n_(446366, "FormMixin", lambda: FormMixin), _n_(446367, "DetailView", lambda: DetailView)):
    _l_(446473)

    template_name = 'qkchat/thread.html'
    _l_(446368)
    form_class = _n_(446369, "ComposeForm", lambda: ComposeForm)
    _l_(446370)
    success_url = './'
    _l_(446371)

    def get_queryset(self):
        _l_(446380)

        aux = _c_(446378, _a_(446374, _a_(446373, _n_(446372, "Thread", lambda: Thread), "objects"), "by_user"), _a_(446377, _a_(446376, _n_(446375, "self", lambda: self), "request"), "user"))
        _l_(446379)
        return aux

    def get_object(self):
        _l_(446401)

        other_username  = _c_(446384, _a_(446383, _a_(446382, _n_(446381, "self", lambda: self), "kwargs"), "get"), 'username')
        _l_(446385)
        obj, created    = _c_(446393, _a_(446388, _a_(446387, _n_(446386, "Thread", lambda: Thread), "objects"), "get_or_new"), _a_(446391, _a_(446390, _n_(446389, "self", lambda: self), "request"), "user"), _n_(446392, "other_username", lambda: other_username))
        _l_(446394)
        if _n_(446395, "obj", lambda: obj) == None:
            _l_(446398)

            raise _n_(446396, "Http404", lambda: Http404)
            _l_(446397)
        aux = _n_(446399, "obj", lambda: obj)
        _l_(446400)
        return aux

    def get_context_data(self, **kwargs):
        _l_(446414)

        context = _c_(446405, _a_(446403, _n_(446402, "super", lambda: super)(), "get_context_data"), **_n_(446404, "kwargs", lambda: kwargs))
        _l_(446406)
        _n_(446407, "context", lambda: context)['form'] = _c_(446410, _a_(446409, _n_(446408, "self", lambda: self), "get_form"))
        _l_(446411)
        aux = _n_(446412, "context", lambda: context)
        _l_(446413)
        return aux

    def post(self, request, *args, **kwargs):
        _l_(446445)

        if not _a_(446417, _a_(446416, _n_(446415, "request", lambda: request), "user"), "is_authenticated"):
            _l_(446421)

            aux = _c_(446419, _n_(446418, "HttpResponseForbidden", lambda: HttpResponseForbidden))
            _l_(446420)
            return aux
        _n_(446422, "self", lambda: self).object = _c_(446425, _a_(446424, _n_(446423, "self", lambda: self), "get_object"))
        _l_(446426)
        form = _c_(446429, _a_(446428, _n_(446427, "self", lambda: self), "get_form"))
        _l_(446430)
        if _c_(446433, _a_(446432, _n_(446431, "form", lambda: form), "is_valid")):
            _l_(446444)

            aux = _c_(446437, _a_(446435, _n_(446434, "self", lambda: self), "form_valid"), _n_(446436, "form", lambda: form))
            _l_(446438)
            return aux
        else:
            aux = _c_(446442, _a_(446440, _n_(446439, "self", lambda: self), "form_invalid"), _n_(446441, "form", lambda: form))
            _l_(446443)
            return aux

    def form_valid(self, form):
        _l_(446472)

        thread = _c_(446448, _a_(446447, _n_(446446, "self", lambda: self), "get_object"))
        _l_(446449)
        user = _a_(446452, _a_(446451, _n_(446450, "self", lambda: self), "request"), "user")
        _l_(446453)
        message = _c_(446457, _a_(446456, _a_(446455, _n_(446454, "form", lambda: form), "cleaned_data"), "get"), "message")
        _l_(446458)
        _c_(446465, _a_(446461, _a_(446460, _n_(446459, "ChatMessage", lambda: ChatMessage), "objects"), "create"), user=_n_(446462, "user", lambda: user), thread=_n_(446463, "thread", lambda: thread), message=_n_(446464, "message", lambda: message))
        _l_(446466)
        aux = _c_(446470, _a_(446468, _n_(446467, "super", lambda: super)(), "form_valid"), _n_(446469, "form", lambda: form))
        _l_(446471)
        return aux