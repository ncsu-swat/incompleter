# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72217488/django-typeerror-field-id-expected-a-number-but-got-user
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(643300, _n_(643299, "login_required", lambda: login_required), login_url='login')
def addNote(request):
    _l_(643356)

    notebooks = _c_(643306, _a_(643303, _a_(643302, _n_(643301, "Notebook", lambda: Notebook), "objects"), "filter"), user=_a_(643305, _n_(643304, "request", lambda: request), "user"))
    _l_(643307)

    if _a_(643309, _n_(643308, "request", lambda: request), "method") == 'POST':
        _l_(643348)

        data = _a_(643311, _n_(643310, "request", lambda: request), "POST")
        _l_(643312)
        note = _c_(643316, _a_(643315, _a_(643314, _n_(643313, "request", lambda: request), "POST"), "get"), 'content')
        _l_(643317)

        if _n_(643318, "data", lambda: data)['notebook'] != 'none':
            _l_(643334)

            notebook = _c_(643323, _a_(643321, _a_(643320, _n_(643319, "Notebook", lambda: Notebook), "objects"), "get"), id=_n_(643322, "data", lambda: data)['notebook'])
            _l_(643324)
        elif _n_(643325, "data", lambda: data)['notebook_new'] != '':
            _l_(643333)

            notebook, created = _c_(643330, _a_(643328, _a_(643327, _n_(643326, "Notebook", lambda: Notebook), "objects"), "get_or_create"), name=_n_(643329, "data", lambda: data)['notebook_new'])  
            _l_(643331)  
        else:                                                                      
            notebook = None
            _l_(643332)

        _c_(643343, _a_(643337, _a_(643336, _n_(643335, "Notes", lambda: Notes), "objects"), "create"), notebook=_n_(643338, "notebook", lambda: notebook),
            title=_n_(643339, "data", lambda: data)['title_note'],
            content=_n_(643340, "note", lambda: note),
            user=_a_(643342, _n_(643341, "request", lambda: request), "user"),
        )
        _l_(643344)
        aux = _c_(643346, _n_(643345, "redirect", lambda: redirect), 'home')
        _l_(643347)

        return aux

    context = {'notebooks': _n_(643349, "notebooks", lambda: notebooks)}
    _l_(643350)
    aux = _c_(643354, _n_(643351, "render", lambda: render), _n_(643352, "request", lambda: request), 'base/add_note.html', _n_(643353, "context", lambda: context))
    _l_(643355)
    return aux