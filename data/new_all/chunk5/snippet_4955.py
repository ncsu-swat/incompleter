# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72492502/nameerror-name-f-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(689733, _n_(689732, "require_http_methods", lambda: require_http_methods), ["POST"])
def submit_survey(request):
    _l_(689805)

    _c_(689737, _a_(689736, _a_(689735, _n_(689734, "request", lambda: request), "user"), "give_coins"), count=10)
    _l_(689738)
    form_data = _c_(689742, _a_(689741, _a_(689740, _n_(689739, "request", lambda: request), "POST"), "copy"))
    _l_(689743)
    form_items = _c_(689748, _n_(689744, "list", lambda: list), _c_(689747, _a_(689746, _n_(689745, "form_data", lambda: form_data), "items")))
    _l_(689749)
    _c_(689752, _n_(689750, "print", lambda: print), "form_items", _n_(689751, "form_items", lambda: form_items))
    _l_(689753)
    _c_(689756, _a_(689755, _n_(689754, "form_items", lambda: form_items), "pop"), 0)  # the first element is the csrf token. Therefore omit it.
    _l_(689757)  # the first element is the csrf token. Therefore omit it.
    survey = None
    _l_(689758)
    for item in _n_(689759, "form_items", lambda: form_items):
        _l_(689788)

        # Here in 'choice/3', '3' is '<choice_id>'.
        choice_str, choice_id = _n_(689760, "item", lambda: item)
        _l_(689761)
        choice_id = _c_(689766, _n_(689762, "int", lambda: int), _c_(689765, _a_(689764, _n_(689763, "choice_id", lambda: choice_id), "split"), '/')[1])
        _l_(689767)
        choice = _c_(689772, _a_(689770, _a_(689769, _n_(689768, "Choice", lambda: Choice), "objects"), "get"), id=_n_(689771, "choice_id", lambda: choice_id))
        _l_(689773)
        if _n_(689774, "survey", lambda: survey) is None:
            _l_(689779)

            survey = _a_(689777, _a_(689776, _n_(689775, "choice", lambda: choice), "question"), "survey")
            _l_(689778)
        _n_(689780, "choice", lambda: choice).votes = _a_(689782, _n_(689781, "choice", lambda: choice), "votes") + 1
        _l_(689783)
        _c_(689786, _a_(689785, _n_(689784, "choice", lambda: choice), "save"))
        _l_(689787)
    if _n_(689789, "survey", lambda: survey) is not None:
        _l_(689801)

        participant = _c_(689795, _n_(689790, "Participant", lambda: Participant), survey=_n_(689791, "survey", lambda: survey), participation_datetime=_c_(689794, _a_(689793, _n_(689792, "timezone", lambda: timezone), "now")))
        _l_(689796)
        _c_(689799, _a_(689798, _n_(689797, "participant", lambda: participant), "save"))
        _l_(689800)
    aux = _c_(689803, _n_(689802, "redirect", lambda: redirect), '/submit_success/')
    _l_(689804)
    return aux