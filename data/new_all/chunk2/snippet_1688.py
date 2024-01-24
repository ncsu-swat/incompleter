# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63318060/typeerror-formlistview-missing-1-required-positional-argument-request
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.core.mail       import send_mail, BadHeaderError
    _l_(444068)

except ImportError:
    pass
try:
    from django.shortcuts       import render, redirect
    _l_(444070)

except ImportError:
    pass
try:
    from django.http            import HttpResponse, HttpResponseRedirect
    _l_(444072)

except ImportError:
    pass
try:
    from .models                import Form
    _l_(444074)

except ImportError:
    pass
try:
    from django.views.generic   import TemplateView
    _l_(444076)

except ImportError:
    pass

def FormListView(request):
    _l_(444121)

    if _a_(444078, _n_(444077, "request", lambda: request), "method") == 'GET':
        _l_(444115)

        form = _c_(444080, _n_(444079, "FormListView", lambda: FormListView))
        _l_(444081)
    else:
        form = _c_(444085, _n_(444082, "FormListView", lambda: FormListView), _a_(444084, _n_(444083, "request", lambda: request), "POST"))
        _l_(444086)
        if _c_(444089, _a_(444088, _n_(444087, "form", lambda: form), "is_valid")):
            _l_(444114)

            name = _a_(444091, _n_(444090, "form", lambda: form), "cleaned_data")['name']
            _l_(444092)
            surname = _a_(444094, _n_(444093, "form", lambda: form), "cleaned_data")['surname']
            _l_(444095)
            email = _a_(444097, _n_(444096, "form", lambda: form), "cleaned_data")['email']
            _l_(444098)
            try:
                _l_(444110)

                _c_(444103, _n_(444099, "send_mail", lambda: send_mail), _n_(444100, "name", lambda: name), _n_(444101, "surname", lambda: surname), _n_(444102, "email", lambda: email), ['kirill_popov_000@mail.ru'])
                _l_(444104)
            except _n_(444105, "BadHeaderError", lambda: BadHeaderError):
                _l_(444109)

                aux = _c_(444107, _n_(444106, "HttpResponse", lambda: HttpResponse), 'Invalid')
                _l_(444108)
                return aux
            aux = _c_(444112, _n_(444111, "redirect", lambda: redirect), 'success')
            _l_(444113)
            return aux
    aux = _c_(444119, _n_(444116, "render", lambda: render), _n_(444117, "request", lambda: request), "index.html", {'form': _n_(444118, "form", lambda: form)})
    _l_(444120)
    return aux

def Success(request):
    _l_(444125)

    aux = _c_(444123, _n_(444122, "HttpResponse", lambda: HttpResponse), 'Success!')
    _l_(444124)
    return aux