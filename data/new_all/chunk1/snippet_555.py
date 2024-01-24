# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30953615/typeerror-object-is-not-json-serializable-in-django-1-8-python-3-4
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.http import HttpRequest,HttpResponse
    _l_(394275)

except ImportError:
    pass
try:
    from django.http import JsonResponse
    _l_(394277)

except ImportError:
    pass
try:
    from json import dumps
    _l_(394279)

except ImportError:
    pass

def get_stats(request):
    _l_(394321)

    if _a_(394281, _n_(394280, "request", lambda: request), "method") == "POST":
        _l_(394286)

        srch_dropV = _a_(394283, _n_(394282, "request", lambda: request), "POST")['srch_dropAJ']
        _l_(394284)
    else:
        srch_dropV = ''
        _l_(394285)
    if(_n_(394287, "srch_dropV", lambda: srch_dropV) == 'Green'):
        _l_(394293)

        students = _c_(394291, _a_(394290, _a_(394289, _n_(394288, "GreenBased", lambda: GreenBased), "objects"), "all"))
        _l_(394292)
    if(_n_(394294, "srch_dropV", lambda: srch_dropV) == 'Yellow'):
        _l_(394300)

        students = _c_(394298, _a_(394297, _a_(394296, _n_(394295, "YellowBased", lambda: YellowBased), "objects"), "all"))
        _l_(394299)
    response_data = {}
    _l_(394301)
    try:
        _l_(394314)

        _n_(394302, "response_data", lambda: response_data)['result'] = 'Success'
        _l_(394303)
        _n_(394304, "response_data", lambda: response_data)['message'] = _c_(394307, _n_(394305, "list", lambda: list), _n_(394306, "students", lambda: students))
        _l_(394308)
    except:
        _l_(394313)

        _n_(394309, "response_data", lambda: response_data)['result'] = 'Ouch!'
        _l_(394310)
        _n_(394311, "response_data", lambda: response_data)['message'] = 'Script has not ran correctly'
        _l_(394312)
    aux = _c_(394319, _n_(394315, "HttpResponse", lambda: HttpResponse), _c_(394318, _n_(394316, "JsonResponse", lambda: JsonResponse), _n_(394317, "response_data", lambda: response_data)), content_type="application/json")
    _l_(394320)
    return aux