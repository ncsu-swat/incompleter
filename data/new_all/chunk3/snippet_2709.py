# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65918421/typeerror-anonimoussurvey-takes-0-positional-arguments-but-1-was-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def AnonimousSurvey():
    _l_(574940)

    
    def __init__(self, question):
        _l_(574915)

        
        _n_(574910, "self", lambda: self).question = _n_(574911, "question", lambda: question)
        _l_(574912)
        _n_(574913, "self", lambda: self).responses = []
        _l_(574914)
    def show_question(self):
        _l_(574921)

        _c_(574919, _n_(574916, "print", lambda: print), _a_(574918, _n_(574917, "self", lambda: self), "question"))
        _l_(574920)
    def store_response(self, new_response):
        _l_(574928)

        _c_(574926, _a_(574924, _a_(574923, _n_(574922, "self", lambda: self), "responses"), "append"), _n_(574925, "new_response", lambda: new_response))
        _l_(574927)
    def show_result(self):
        _l_(574939)

        _c_(574930, _n_(574929, "print", lambda: print), "Survay results:")
        _l_(574931)
        for i in _a_(574933, _n_(574932, "self", lambda: self), "responses"):
            _l_(574938)

            _c_(574936, _n_(574934, "print", lambda: print), "- " + _n_(574935, "i", lambda: i))
            _l_(574937)
quest = "hello what is your name?"
_l_(574941)
new_surv = _c_(574944, _n_(574942, "AnonimousSurvey", lambda: AnonimousSurvey), _n_(574943, "quest", lambda: quest))
_l_(574945)
_c_(574948, _a_(574947, _n_(574946, "new_surv", lambda: new_surv), "show_question"))
_l_(574949)