# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60221512/how-to-solve-the-problem-of-type-error-in-django
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class NewsletterUser(_a_(535119, _n_(535118, "models", lambda: models), "Model")):
    _l_(535130)

    email = _c_(535121, _a_(535120, models, "EmailField"))
    _l_(535122)
    date_added = _c_(535124, _a_(535123, models, "DateTimeField"), auto_now_add=True)
    _l_(535125)

    def __str__(self):
        _l_(535129)

        aux = _a_(535127, _n_(535126, "self", lambda: self), "email")
        _l_(535128)
        return aux