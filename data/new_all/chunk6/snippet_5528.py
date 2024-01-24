# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72492502/nameerror-name-f-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(356540, _n_(356539, "require_http_methods", lambda: require_http_methods), ["POST"])
def submit_survey(request):
    _l_(356612)

    _c_(356544, _a_(356543, _a_(356542, _n_(356541, "request", lambda: request), "user"), "give_coins"), count=10)
    _l_(356545)
    form_data = _c_(356549, _a_(356548, _a_(356547, _n_(356546, "request", lambda: request), "POST"), "copy"))
    _l_(356550)
    form_items = _c_(356555, _n_(356551, "list", lambda: list), _c_(356554, _a_(356553, _n_(356552, "form_data", lambda: form_data), "items")))
    _l_(356556)
    _c_(356559, _n_(356557, "print", lambda: print), "form_items", _n_(356558, "form_items", lambda: form_items))
    _l_(356560)
    _c_(356563, _a_(356562, _n_(356561, "form_items", lambda: form_items), "pop"), 0)  # the first element is the csrf token. Therefore omit it.
    _l_(356564)  # the first element is the csrf token. Therefore omit it.
    survey = None
    _l_(356565)
    for item in _n_(356566, "form_items", lambda: form_items):
        _l_(356595)

        # Here in 'choice/3', '3' is '<choice_id>'.
        choice_str, choice_id = _n_(356567, "item", lambda: item)
        _l_(356568)
        choice_id = _c_(356573, _n_(356569, "int", lambda: int), _c_(356572, _a_(356571, _n_(356570, "choice_id", lambda: choice_id), "split"), '/')[1])
        _l_(356574)
        choice = _c_(356579, _a_(356577, _a_(356576, _n_(356575, "Choice", lambda: Choice), "objects"), "get"), id=_n_(356578, "choice_id", lambda: choice_id))
        _l_(356580)
        if _n_(356581, "survey", lambda: survey) is None:
            _l_(356586)

            survey = _a_(356584, _a_(356583, _n_(356582, "choice", lambda: choice), "question"), "survey")
            _l_(356585)
        _n_(356587, "choice", lambda: choice).votes = _a_(356589, _n_(356588, "choice", lambda: choice), "votes") + 1
        _l_(356590)
        _c_(356593, _a_(356592, _n_(356591, "choice", lambda: choice), "save"))
        _l_(356594)
    if _n_(356596, "survey", lambda: survey) is not None:
        _l_(356608)

        participant = _c_(356602, _n_(356597, "Participant", lambda: Participant), survey=_n_(356598, "survey", lambda: survey), participation_datetime=_c_(356601, _a_(356600, _n_(356599, "timezone", lambda: timezone), "now")))
        _l_(356603)
        _c_(356606, _a_(356605, _n_(356604, "participant", lambda: participant), "save"))
        _l_(356607)
    aux = _c_(356610, _n_(356609, "redirect", lambda: redirect), '/submit_success/')
    _l_(356611)
    return aux