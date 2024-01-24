# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63313991/attributeerror-function-object-has-no-attribute-as-view-whats-wrong
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.core.mail import send_mail, BadHeaderError
    _l_(431008)

except ImportError:
    pass
try:
    from django.shortcuts import render, redirect
    _l_(431010)

except ImportError:
    pass
try:
    from django.http import HttpResponse, HttpResponseRedirect
    _l_(431012)

except ImportError:
    pass
try:
    from .models import Form
    _l_(431014)

except ImportError:
    pass

def FormListView(request):
    _l_(431059)

    if _a_(431016, _n_(431015, "request", lambda: request), "method") == 'GET':
        _l_(431053)

        form = _c_(431018, _n_(431017, "FormListView", lambda: FormListView))
        _l_(431019)
    else:
        form = _c_(431023, _n_(431020, "FormListView", lambda: FormListView), _a_(431022, _n_(431021, "request", lambda: request), "POST"))
        _l_(431024)
        if _c_(431027, _a_(431026, _n_(431025, "form", lambda: form), "is_valid")):
            _l_(431052)

            name = _a_(431029, _n_(431028, "form", lambda: form), "cleaned_data")['name']
            _l_(431030)
            surname = _a_(431032, _n_(431031, "form", lambda: form), "cleaned_data")['surname']
            _l_(431033)
            email = _a_(431035, _n_(431034, "form", lambda: form), "cleaned_data")['email']
            _l_(431036)
            try:
                _l_(431048)

                _c_(431041, _n_(431037, "send_mail", lambda: send_mail), _n_(431038, "name", lambda: name), _n_(431039, "surname", lambda: surname), _n_(431040, "email", lambda: email), ['kirill_popov_000@mail.ru'])
                _l_(431042)
            except _n_(431043, "BadHeaderError", lambda: BadHeaderError):
                _l_(431047)

                aux = _c_(431045, _n_(431044, "HttpResponse", lambda: HttpResponse), 'Invalid')
                _l_(431046)
                return aux
            aux = _c_(431050, _n_(431049, "redirect", lambda: redirect), 'success')
            _l_(431051)
            return aux
    aux = _c_(431057, _n_(431054, "render", lambda: render), _n_(431055, "request", lambda: request), "index.html", {'form': _n_(431056, "form", lambda: form)})
    _l_(431058)
    return aux

def Success(request):
    _l_(431063)

    aux = _c_(431061, _n_(431060, "HttpResponse", lambda: HttpResponse), 'Success!')
    _l_(431062)
    return aux