# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62919896/using-partial-on-drfs-action-gives-typeerror-multiple-values-for-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
specialised_action = _c_(567741, _n_(567739, "partial", lambda: partial), _n_(567740, "action", lambda: action), methods=["post"], detail=True, url_path="my-action-url")
_l_(567742)

class SomeViewSet(_n_(567743, "GenericViewSet", lambda: GenericViewSet)):
    _l_(567749)

    @_n_(567744, "specialised_action", lambda: specialised_action)
    def action_handler(self, request, *args, **kwargs):
        _l_(567748)

        _c_(567746, _n_(567745, "print", lambda: print), "do something")
        _l_(567747)