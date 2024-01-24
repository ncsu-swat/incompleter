# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62032946/drf-creating-new-objects-from-nested-representation-raises-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class User(_a_(550357, _n_(550356, "models", lambda: models), "Model")):
    _l_(550371)

    user_id = _c_(550359, _a_(550358, models, "CharField"), max_length=129,
        unique=True,
    )
    _l_(550360)
    user_article = _c_(550362, _a_(550361, models, "ManyToManyField"), Article,
        through="UserArticle",
    )
    _l_(550363)
    occupation = _c_(550365, _a_(550364, models, "CharField"), max_length=100, default='null')
    _l_(550366)

    def __str__(self):
        _l_(550370)

        aux = _a_(550368, _n_(550367, "self", lambda: self), "user_id")
        _l_(550369)
        return aux