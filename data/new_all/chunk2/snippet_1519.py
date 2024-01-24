# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41192303/getting-nameerror-variable-not-defined-when-it-is-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from survey import AnonymousSurvey
    _l_(444042)

except ImportError:
    pass

#   Define a question, and make a survey.
question = "What language did you first learn to speak?"
_l_(444043)
my_survey = _c_(444046, _n_(444044, "AnonymousSurvey", lambda: AnonymousSurvey), _n_(444045, "question", lambda: question))
_l_(444047)

#   Show the question, and store responses to the question.
_c_(444050, _a_(444049, _n_(444048, "my_survey", lambda: my_survey), "show_question"))
_l_(444051)
_c_(444053, _n_(444052, "print", lambda: print), "Enter 'q' at any time to quit.\n")
_l_(444054)
while True:
    _l_(444066)

    response = _c_(444056, _n_(444055, "input", lambda: input), "Language: ")
    _l_(444057)
    if _n_(444058, "response", lambda: response) == 'q':
        _l_(444060)

        break
        _l_(444059)
    _c_(444064, _a_(444062, _n_(444061, "my_survey", lambda: my_survey), "store_response"), _n_(444063, "response", lambda: response))
    _l_(444065)