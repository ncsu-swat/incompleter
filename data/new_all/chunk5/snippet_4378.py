# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58844911/why-am-i-getting-a-typeerror-while-trying-to-access-httprequest-postchoice-v
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render, get_object_or_404
    _l_(663139)

except ImportError:
    pass
try:
    from django.http import HttpResponseRedirect
    _l_(663141)

except ImportError:
    pass
try:
    from django.urls import reverse
    _l_(663143)

except ImportError:
    pass
try:
    from .models import Question, Choice
    _l_(663145)

except ImportError:
    pass

def vote(request, question_id):
    _l_(663182)

    question = _c_(663149, _n_(663146, "get_object_or_404", lambda: get_object_or_404), _n_(663147, "Question", lambda: Question), pk=_n_(663148, "question_id", lambda: question_id))
    _l_(663150)
    try:
        _l_(663181)

        selected_choice = _c_(663157, _a_(663153, _a_(663152, _n_(663151, "question", lambda: question), "choice_set"), "get"), _n_(663154, "Question", lambda: Question), pk=_a_(663156, _n_(663155, "request", lambda: request), "POST")['choice'])
        _l_(663158)
    except (_n_(663159, "KeyError", lambda: KeyError), _a_(663161, _n_(663160, "Choice", lambda: Choice), "DoesNotExist")):
        _l_(663167)

        aux = _c_(663165, _n_(663162, "render", lambda: render), _n_(663163, "request", lambda: request), 'polls/detail.html', {'question': _n_(663164, "question", lambda: question), 'error_message': 'Please select a choice and vote'})
        _l_(663166)
        return aux
    else:
        _n_(663168, "selected_choice", lambda: selected_choice).no_of_votes += 1
        _l_(663169)
        _c_(663172, _a_(663171, _n_(663170, "selected_choice", lambda: selected_choice), "save"))
        _l_(663173)
        aux = _c_(663179, _n_(663174, "HttpResponseRedirect", lambda: HttpResponseRedirect), _c_(663178, _n_(663175, "reverse", lambda: reverse), 'polls:result', args=(_a_(663177, _n_(663176, "question", lambda: question), "id"),)))
        _l_(663180)
        return aux

def result(request, question_id):
    _l_(663193)

    question = _c_(663186, _n_(663183, "get_object_or_404", lambda: get_object_or_404), _n_(663184, "Question", lambda: Question), pk=_n_(663185, "question_id", lambda: question_id))
    _l_(663187)
    aux = _c_(663191, _n_(663188, "render", lambda: render), _n_(663189, "request", lambda: request), 'polls/result.html', {'question': _n_(663190, "question", lambda: question)})
    _l_(663192)
    return aux