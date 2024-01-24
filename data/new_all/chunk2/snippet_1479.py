# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53784399/nameerror-name-key-is-not-definedunable-to-display-error-using-bottle
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bottle import request, template,route,run,post
    _l_(448080)

except ImportError:
    pass

@_c_(448082, _n_(448081, "route", lambda: route), '/')
def index():
    _l_(448086)

    aux = _c_(448084, _n_(448083, "template", lambda: template), 'val.html')
    _l_(448085)
    return aux

@_c_(448088, _n_(448087, "post", lambda: post), '/result')
def result():
    _l_(448100)

    result=_a_(448090, _n_(448089, "request", lambda: request), "forms")
    _l_(448091)
    _c_(448094, _n_(448092, "print", lambda: print), _n_(448093, "result", lambda: result))       #Unable to print 
    _l_(448095)       #Unable to print 
    aux = _c_(448098, _n_(448096, "template", lambda: template), "result",result = _n_(448097, "result", lambda: result))
    _l_(448099)

    return aux


if _n_(448101, "__name__", lambda: __name__) == '__main__':
    _l_(448105)

    _c_(448103, _n_(448102, "run", lambda: run), host='localhost',port=8080,debug='True',reloader='True')
    _l_(448104)