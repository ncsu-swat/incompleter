# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67137466/django-throwing-attribute-error-and-i-dont-know-why-it-is-happening
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(581812)

except ImportError:
    pass
try:
    from django.http import HttpResponse
    _l_(581814)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(581816)

except ImportError:
    pass
try:
    from machine_website.models import contact_detail
    _l_(581818)

except ImportError:
    pass
try:
    from machine_website.models import product_data
    _l_(581820)

except ImportError:
    pass
try:
    from machine_website.forms import product_Form
    _l_(581822)

except ImportError:
    pass


# Create your views here.

def homepage(request):
    _l_(581853)

    descp1 = _c_(581824, _n_(581823, "product_data", lambda: product_data))
    _l_(581825)
    _n_(581826, "descp1", lambda: descp1).disc = ' this is the discription'
    _l_(581827)
    _n_(581828, "descp1", lambda: descp1).img = '2.jpg'
    _l_(581829)

    descp2 = _c_(581831, _n_(581830, "product_data", lambda: product_data))
    _l_(581832)
    _n_(581833, "descp2", lambda: descp2).disc = ' this is the discription 2'
    _l_(581834)
    _n_(581835, "descp2", lambda: descp2).img = '2.jpg'
    _l_(581836)

    descp3 = _c_(581838, _n_(581837, "product_data", lambda: product_data))
    _l_(581839)
    _n_(581840, "descp3", lambda: descp3).disc = ' this is the discription 3'
    _l_(581841)
    _n_(581842, "descp3", lambda: descp3).img = '5.jpg'
    _l_(581843)

    descp = [_n_(581844, "descp1", lambda: descp1), _n_(581845, "descp2", lambda: descp2),_n_(581846, "descp3", lambda: descp3)]
    _l_(581847)
    aux = _c_(581851, _n_(581848, "render", lambda: render), _n_(581849, "request", lambda: request),'homepage.html', {'descp': _n_(581850, "descp", lambda: descp)})
    _l_(581852)
    return aux

def contact(request):
    _l_(581889)

    if _a_(581855, _n_(581854, "request", lambda: request), "method")=="POST":
        _l_(581884)

        name = _c_(581859, _a_(581858, _a_(581857, _n_(581856, "request", lambda: request), "POST"), "get"), 'name')
        _l_(581860)
        email = _c_(581864, _a_(581863, _a_(581862, _n_(581861, "request", lambda: request), "POST"), "get"), 'email')
        _l_(581865)
        desc = _c_(581869, _a_(581868, _a_(581867, _n_(581866, "request", lambda: request), "POST"), "get"), 'desc')
        _l_(581870)
        contact = _c_(581878, _n_(581871, "contact_detail", lambda: contact_detail), name=_n_(581872, "name", lambda: name) , email=_n_(581873, "email", lambda: email), desc=_n_(581874, "desc", lambda: desc), date=_c_(581877, _a_(581876, _n_(581875, "datetime", lambda: datetime), "today")))
        _l_(581879)
        _c_(581882, _a_(581881, _n_(581880, "contact", lambda: contact), "save"))
        _l_(581883)
    aux = _c_(581887, _n_(581885, "render", lambda: render), _n_(581886, "request", lambda: request),'contact.html')
    _l_(581888)
    return aux

def services(request):
    _l_(581894)

    aux = _c_(581892, _n_(581890, "render", lambda: render), _n_(581891, "request", lambda: request),'services.html')
    _l_(581893)
    return aux

def index(request):
    _l_(581898)

    aux = _c_(581896, _n_(581895, "HttpResponse", lambda: HttpResponse), "this is index page")
    _l_(581897)
    return aux


def more(request):
    _l_(581909)


    info = _c_(581902, _a_(581901, _a_(581900, _n_(581899, "product_data", lambda: product_data), "objects"), "all"))
    _l_(581903)
    aux = _c_(581907, _n_(581904, "render", lambda: render), _n_(581905, "request", lambda: request) ,'more.html' , {'info' : _n_(581906, "info", lambda: info)})
    _l_(581908)

    return aux

IMAGE_FILE_TYPES = ['png' , 'PNG' , 'jpg' , 'JPG' , 'jpeg' , 'jfif']
_l_(581910)

def product_details(request):
    _l_(581969)

    form = _c_(581912, _n_(581911, "product_Form", lambda: product_Form))
    _l_(581913)
    if _a_(581915, _n_(581914, "request", lambda: request), "method") == 'POST':
        _l_(581961)

        form = _c_(581921, _n_(581916, "product_Form", lambda: product_Form), _a_(581918, _n_(581917, "request", lambda: request), "POST"), _a_(581920, _n_(581919, "request", lambda: request), "FILES"))
        _l_(581922)
        if _c_(581925, _a_(581924, _n_(581923, "form", lambda: form), "is_valid")):
            _l_(581960)

            user_pr = _c_(581928, _a_(581927, _n_(581926, "form", lambda: form), "save"), commit=False)
            _l_(581929)
            _n_(581930, "user_pr", lambda: user_pr).img = _a_(581932, _n_(581931, "request", lambda: request), "FILES")['img']
            _l_(581933)
            file_type = _c_(581938, _a_(581937, _a_(581936, _a_(581935, _n_(581934, "user_pr", lambda: user_pr), "img"), "url"), "split"), '.')
            _l_(581939)
            file_type = _c_(581942, _a_(581941, _n_(581940, "file_type", lambda: file_type), "lower"))
            _l_(581943)
            if _n_(581944, "file_type", lambda: file_type) not in _n_(581945, "IMAGE_FILE_TYPES", lambda: IMAGE_FILE_TYPES):
                _l_(581950)

                aux = _c_(581948, _n_(581946, "render", lambda: render), _n_(581947, "request", lambda: request), 'error.html')
                _l_(581949)
                return aux
            _c_(581953, _a_(581952, _n_(581951, "user_pr", lambda: user_pr), "save"))
            _l_(581954)
            aux = _c_(581958, _n_(581955, "render", lambda: render), _n_(581956, "request", lambda: request), 'details.html', {'user_pr': _n_(581957, "user_pr", lambda: user_pr)})
            _l_(581959)
            return aux
    context = {"form": _n_(581962, "form", lambda: form),}
    _l_(581963)
    aux = _c_(581967, _n_(581964, "render", lambda: render), _n_(581965, "request", lambda: request), 'product_details.html', _n_(581966, "context", lambda: context))
    _l_(581968)
    return aux