# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67946350/attributeerror-when-trying-to-created-nested-serializer-in-django-rest-framework
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Set(_a_(536228, _n_(536227, "models", lambda: models), "Model")):
    _l_(536241)

    id = _c_(536231, _a_(536229, models, "UUIDField"), primary_key=True, default=_a_(536230, uuid, "uuid4"), editable=False)
    _l_(536232)
    ...
    _l_(536233)

    objects = _c_(536235, _a_(536234, models, "Manager"))
    _l_(536236)

    def __str__(self):
        _l_(536240)

        aux = _a_(536238, _n_(536237, "self", lambda: self), "name")
        _l_(536239)
        return aux

class Card(_a_(536243, _n_(536242, "models", lambda: models), "Model")):
    _l_(536261)

    id = _c_(536246, _a_(536244, models, "UUIDField"), primary_key=True, default=_a_(536245, uuid, "uuid4"), editable=False)
    _l_(536247)
    ...
    _l_(536248)
    set = _c_(536252, _a_(536249, models, "ForeignKey"), _n_(536250, "Set", lambda: Set), on_delete=_a_(536251, models, "CASCADE"), related_name='Cards', related_query_name='Cards')
    _l_(536253)


    objects = _c_(536255, _a_(536254, models, "Manager"))
    _l_(536256)

    def __str__(self):
        _l_(536260)

        aux = _a_(536258, _n_(536257, "self", lambda: self), "name")
        _l_(536259)
        return aux