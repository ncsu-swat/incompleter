# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68318786/pythondjangoattributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render, get_object_or_404
    _l_(638208)

except ImportError:
    pass
try:
    from django.http import HttpResponse, HttpResponseRedirect
    _l_(638210)

except ImportError:
    pass
try:
    from .models import Question, Choice
    _l_(638212)

except ImportError:
    pass
try:
    from django.template import loader
    _l_(638214)

except ImportError:
    pass
try:
    from django.urls import reverse
    _l_(638216)

except ImportError:
    pass




def index(request):
    _l_(638233)

    latest_question_list = _c_(638220, _a_(638219, _a_(638218, _n_(638217, "Question", lambda: Question), "objects"), "order_by"), '-pub_date')[:5]
    _l_(638221)
    template = _c_(638224, _a_(638223, _n_(638222, "loader", lambda: loader), "get_template"), 'polls/index.html')
    _l_(638225)
    context = {
        'latest_question_list': _n_(638226, "latest_question_list", lambda: latest_question_list)
    }
    _l_(638227)
    aux = _c_(638231, _n_(638228, "render", lambda: render), _n_(638229, "request", lambda: request), 'polls/index.html', _n_(638230, "context", lambda: context))
    _l_(638232)
    return aux

def detail(request, question_id):
    _l_(638244)

    question =_c_(638237, _n_(638234, "get_object_or_404", lambda: get_object_or_404), _n_(638235, "Question", lambda: Question), pk=_n_(638236, "question_id", lambda: question_id))
    _l_(638238)
    aux = _c_(638242, _n_(638239, "render", lambda: render), _n_(638240, "request", lambda: request), "polls/detail.html", {'question':_n_(638241, "question", lambda: question)})
    _l_(638243)
    return aux

def results(request, question_id):
    _l_(638251)

    response = "You are looking at results of question %s"
    _l_(638245)
    aux = _c_(638249, _n_(638246, "HttpResponse", lambda: HttpResponse), _n_(638247, "response", lambda: response) % _n_(638248, "question_id", lambda: question_id))
    _l_(638250)
    return aux

def vote(request, question_id):
    _l_(638287)

    question = _c_(638255, _n_(638252, "get_object_or_404", lambda: get_object_or_404), _n_(638253, "Question", lambda: Question), pk=_n_(638254, "question_id", lambda: question_id))
    _l_(638256)
    try:
        _l_(638286)

        selected_choice = _c_(638262, _a_(638259, _a_(638258, _n_(638257, "question", lambda: question), "choice_set"), "get"), pk=_a_(638261, _n_(638260, "request", lambda: request), "POST")['choice'])
        _l_(638263)
    except (_n_(638264, "KeyError", lambda: KeyError), _a_(638266, _n_(638265, "Choice", lambda: Choice), "DoesNotExist")):
        _l_(638272)

        aux = _c_(638270, _n_(638267, "render", lambda: render), _n_(638268, "request", lambda: request), 'polls/detail.html', {
            'question' : _n_(638269, "question", lambda: question),
            "error_message" : "You didn't select a choice'",
    })
        _l_(638271)

        return aux
    else:
        _n_(638273, "selected_choice", lambda: selected_choice).votes += 1
        _l_(638274)
        _c_(638277, _a_(638276, _n_(638275, "selected_choice", lambda: selected_choice), "save"))
        _l_(638278)
        aux = _c_(638284, _n_(638279, "HttpResponseRedirect", lambda: HttpResponseRedirect), _c_(638283, _n_(638280, "reverse", lambda: reverse), 'polls:results', args=[_a_(638282, _n_(638281, "question", lambda: question), "id")]))
        _l_(638285)
        return aux
# Create your views here.