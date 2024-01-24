# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50539105/django-2-0-tutorial-attributeerror-at-polls-1-vote-reversemanytoonedescript
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.urls import reverse
    _l_(395235)

except ImportError:
    pass
try:
    from django.views import generic
    _l_(395237)

except ImportError:
    pass
try:
    from .models import Choice, Question
    _l_(395239)

except ImportError:
    pass


class IndexView(_a_(395241, _n_(395240, "generic", lambda: generic), "ListView")):
    _l_(395250)

    template_name = 'polls/index.html'
    _l_(395242)
    context_object_name = 'latest_question_list'
    _l_(395243)

    def get_queryset(self):
        _l_(395249)

        """Return the last five published questions."""
        aux = _c_(395247, _a_(395246, _a_(395245, _n_(395244, "Question", lambda: Question), "objects"), "order_by"), '-pub_date')[:5]
        _l_(395248)
        return aux


class DetailView(_a_(395252, _n_(395251, "generic", lambda: generic), "DetailView")):
    _l_(395256)

    model = _n_(395253, "Question", lambda: Question)
    _l_(395254)
    template_name = 'polls/details.html'
    _l_(395255)


class ResultsView(_a_(395258, _n_(395257, "generic", lambda: generic), "DetailView")):
    _l_(395262)

    model = _n_(395259, "Question", lambda: Question)
    _l_(395260)
    template_name = 'polls/results.html'
    _l_(395261)


def vote(request, question_id):
    _l_(395293)

    try:
        _l_(395292)

        selected_choice = _c_(395268, _a_(395265, _a_(395264, _n_(395263, "Question", lambda: Question), "choice_set"), "get"), pk=_a_(395267, _n_(395266, "request", lambda: request), "POST")['choice'])
        _l_(395269)
    except (_n_(395270, "KeyError", lambda: KeyError), _a_(395272, _n_(395271, "Choice", lambda: Choice), "DoesNotExist")):
        _l_(395278)

        aux = _c_(395276, _n_(395273, "render", lambda: render), _n_(395274, "request", lambda: request), 'polls/detail.html', {
            'question': _n_(395275, "question", lambda: question),
            'error_message': "You didn't select a choice.",
        })
        _l_(395277)
        # Redisplay the question voting form.
        return aux
    else:
        _n_(395279, "selected_choice", lambda: selected_choice).votes += 1
        _l_(395280)
        _c_(395283, _a_(395282, _n_(395281, "selected_choice", lambda: selected_choice), "save"))
        _l_(395284)
        aux = _c_(395290, _n_(395285, "HttpResponseRedirect", lambda: HttpResponseRedirect), _c_(395289, _n_(395286, "reverse", lambda: reverse), 'polls:results', args=(_a_(395288, _n_(395287, "question", lambda: question), "id"),)))
        _l_(395291)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return aux