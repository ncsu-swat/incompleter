# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48868516/type-error-with-django-post-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_n_(700153, "require_POST", lambda: require_POST)
def addTodo(request):
    _l_(700191)

    form = _c_(700157, _n_(700154, "TodoForm", lambda: TodoForm), _a_(700156, _n_(700155, "request", lambda: request), "POST"))
    _l_(700158)

    _c_(700162, _n_(700159, "print", lambda: print), _a_(700161, _n_(700160, "form", lambda: form), "errors"))
    _l_(700163)
    _c_(700167, _n_(700164, "print", lambda: print), _a_(700166, _n_(700165, "request", lambda: request), "POST")['task_title'])
    _l_(700168)
    if _a_(700170, _n_(700169, "request", lambda: request), "method") == 'POST':
        _l_(700187)

        if _c_(700173, _a_(700172, _n_(700171, "form", lambda: form), "is_valid")):
            _l_(700186)

            new_todo = _c_(700177, _n_(700174, "Task", lambda: Task), task_title=_a_(700176, _n_(700175, "request", lambda: request), "POST")['task_title'])
            _l_(700178)
            _c_(700181, _a_(700180, _n_(700179, "new_todo", lambda: new_todo), "save"))
            _l_(700182)
            _c_(700184, _n_(700183, "print", lambda: print), 'DONE')
            _l_(700185)
    aux = _c_(700189, _n_(700188, "redirect", lambda: redirect), 'index')
    _l_(700190)

    return aux