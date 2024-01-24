# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56159534/attributeerror-at-ask-module-django-db-models-has-no-attribute-student
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render, get_object_or_404
    _l_(679299)

except ImportError:
    pass
try:
    from .models import post
    _l_(679301)

except ImportError:
    pass
try:
    from .models import Lost
    _l_(679303)

except ImportError:
    pass
try:
    from .models import Student
    _l_(679305)

except ImportError:
    pass
try:
    from social import forms
    _l_(679307)

except ImportError:
    pass
try:
    from django.db import models
    _l_(679309)

except ImportError:
    pass



def home (request) :
    _l_(679320)

    context = {
        'titel': 'homepage',
        'posts': _c_(679313, _a_(679312, _a_(679311, _n_(679310, "post", lambda: post), "objects"), "all"))
    }
    _l_(679314)
    aux = _c_(679318, _n_(679315, "render", lambda: render), _n_(679316, "request", lambda: request), 'site.html', _n_(679317, "context", lambda: context)) 
    _l_(679319) 
    return aux 


def post_detail(request, post_id):
    _l_(679334)

    post= _c_(679324, _n_(679321, "get_object_or_404", lambda: get_object_or_404), _n_(679322, "Lost", lambda: Lost), pk=_n_(679323, "post_id", lambda: post_id))
    _l_(679325)
    context = {
        'title': _n_(679326, "post", lambda: post),
        'post': _n_(679327, "post", lambda: post),
    }
    _l_(679328)
    aux = _c_(679332, _n_(679329, "render", lambda: render), _n_(679330, "request", lambda: request), 'details.html', _n_(679331, "context", lambda: context))
    _l_(679333)

    return aux



def Register(request):
    _l_(679371)


    form_data=_c_(679339, _a_(679336, _n_(679335, "forms", lambda: forms), "UserRegistrar"), _a_(679338, _n_(679337, "request", lambda: request), "POST") or None)
    _l_(679340)
    msg=''
    _l_(679341)
    if _c_(679344, _a_(679343, _n_(679342, "form_data", lambda: form_data), "is_valid")):
        _l_(679362)

        student=_c_(679347, _a_(679346, _n_(679345, "models", lambda: models), "Student"))
        _l_(679348)
        _n_(679349, "student", lambda: student).first_name=_a_(679351, _n_(679350, "form_data", lambda: form_data), "cleaned_data")['first_name']
        _l_(679352)
        _n_(679353, "student", lambda: student).last_name=_a_(679355, _n_(679354, "form_data", lambda: form_data), "cleaned_data")['last_name']
        _l_(679356)
        _c_(679359, _a_(679358, _n_(679357, "student", lambda: student), "save"))
        _l_(679360)
        msg='data is saved'
        _l_(679361)

    context={
          'formregister':_n_(679363, "form_data", lambda: form_data),
        'msg':_n_(679364, "msg", lambda: msg)
      }
    _l_(679365)
    aux = _c_(679369, _n_(679366, "render", lambda: render), _n_(679367, "request", lambda: request),'ask.html',_n_(679368, "context", lambda: context))
    _l_(679370)
    return aux