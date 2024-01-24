# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56159534/attributeerror-at-ask-module-django-db-models-has-no-attribute-student
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render, get_object_or_404
    _l_(686035)

except ImportError:
    pass
try:
    from .models import post
    _l_(686037)

except ImportError:
    pass
try:
    from .models import Lost
    _l_(686039)

except ImportError:
    pass
try:
    from .models import Student
    _l_(686041)

except ImportError:
    pass
try:
    from social import forms
    _l_(686043)

except ImportError:
    pass
try:
    from django.db import models
    _l_(686045)

except ImportError:
    pass



def home (request) :
    _l_(686056)

    context = {
        'titel': 'homepage',
        'posts': _c_(686049, _a_(686048, _a_(686047, _n_(686046, "post", lambda: post), "objects"), "all"))
    }
    _l_(686050)
    aux = _c_(686054, _n_(686051, "render", lambda: render), _n_(686052, "request", lambda: request), 'site.html', _n_(686053, "context", lambda: context)) 
    _l_(686055) 
    return aux 


def post_detail(request, post_id):
    _l_(686070)

    post= _c_(686060, _n_(686057, "get_object_or_404", lambda: get_object_or_404), _n_(686058, "Lost", lambda: Lost), pk=_n_(686059, "post_id", lambda: post_id))
    _l_(686061)
    context = {
        'title': _n_(686062, "post", lambda: post),
        'post': _n_(686063, "post", lambda: post),
    }
    _l_(686064)
    aux = _c_(686068, _n_(686065, "render", lambda: render), _n_(686066, "request", lambda: request), 'details.html', _n_(686067, "context", lambda: context))
    _l_(686069)

    return aux



def Register(request):
    _l_(686107)


    form_data=_c_(686075, _a_(686072, _n_(686071, "forms", lambda: forms), "UserRegistrar"), _a_(686074, _n_(686073, "request", lambda: request), "POST") or None)
    _l_(686076)
    msg=''
    _l_(686077)
    if _c_(686080, _a_(686079, _n_(686078, "form_data", lambda: form_data), "is_valid")):
        _l_(686098)

        student=_c_(686083, _a_(686082, _n_(686081, "models", lambda: models), "Student"))
        _l_(686084)
        _n_(686085, "student", lambda: student).first_name=_a_(686087, _n_(686086, "form_data", lambda: form_data), "cleaned_data")['first_name']
        _l_(686088)
        _n_(686089, "student", lambda: student).last_name=_a_(686091, _n_(686090, "form_data", lambda: form_data), "cleaned_data")['last_name']
        _l_(686092)
        _c_(686095, _a_(686094, _n_(686093, "student", lambda: student), "save"))
        _l_(686096)
        msg='data is saved'
        _l_(686097)

    context={
          'formregister':_n_(686099, "form_data", lambda: form_data),
        'msg':_n_(686100, "msg", lambda: msg)
      }
    _l_(686101)
    aux = _c_(686105, _n_(686102, "render", lambda: render), _n_(686103, "request", lambda: request),'ask.html',_n_(686104, "context", lambda: context))
    _l_(686106)
    return aux