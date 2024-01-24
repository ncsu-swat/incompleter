# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56148087/how-to-fix-typeerror-argument-of-type-function-is-not-iterable-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(432854)

except ImportError:
    pass
try:
    from django.contrib import messages
    _l_(432856)

except ImportError:
    pass
try:
    from django.core.mail import send_mail
    _l_(432858)

except ImportError:
    pass
#from demoapp.form import ContactForm


# Create your views here.

def index(request):
    _l_(432863)

    aux = _c_(432861, _n_(432859, "render", lambda: render), _n_(432860, "request", lambda: request),'index.html',{'page':'home'})
    _l_(432862)
    return aux


def contact(request):
    _l_(432897)

    try:
        _l_(432896)

        if _a_(432865, _n_(432864, "request", lambda: request), "method") == 'POST':
            _l_(432888)

            form = _c_(432869, _n_(432866, "ContactForm", lambda: ContactForm), _a_(432868, _n_(432867, "request", lambda: request), "POST"))
            _l_(432870)
            if _c_(432873, _a_(432872, _n_(432871, "form", lambda: form), "is_valid")):
                _l_(432884)

                _c_(432877, _n_(432874, "send_mail", lambda: send_mail), _a_(432876, _n_(432875, "form", lambda: form), "cleaned_data"))
                _l_(432878)
                _c_(432882, _a_(432880, _n_(432879, "messages", lambda: messages), "success"), _n_(432881, "request", lambda: request),'Your message is successfully submitted')
                _l_(432883)

        else:
            form = _c_(432886, _n_(432885, "ContactForm", lambda: ContactForm))
            _l_(432887)

    except:
        _l_(432895)

        _c_(432893, _a_(432890, _n_(432889, "messages", lambda: messages), "error"), _n_(432891, "request", lambda: request),'contact.html',{'page':'contact','form':_n_(432892, "form", lambda: form)})
        _l_(432894)

def clear(request):
    _l_(432911)

    form = _c_(432899, _n_(432898, "ContactForm", lambda: ContactForm))
    _l_(432900)
    _c_(432904, _a_(432902, _n_(432901, "messages", lambda: messages), "error"), _n_(432903, "request", lambda: request),'Fields Cleared')
    _l_(432905)
    aux = _c_(432909, _n_(432906, "render", lambda: render), _n_(432907, "request", lambda: request),'contact.html',{'page':'contact','form':_n_(432908, "form", lambda: form)})
    _l_(432910)
    return aux