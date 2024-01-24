# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62032946/drf-creating-new-objects-from-nested-representation-raises-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class UserArticle(_a_(540161, _n_(540160, "models", lambda: models), "Model")):
    _l_(540179)

    user = _c_(540164, _a_(540162, models, "ForeignKey"), User, to_field='user_id',
                             on_delete=_a_(540163, models, "PROTECT"),)
    _l_(540165)
    article = _c_(540168, _a_(540166, models, "ForeignKey"), Article, to_field='uuid',
                                 on_delete=_a_(540167, models, "PROTECT"),)
    _l_(540169)
    posted_as = _c_(540172, ArrayField, _c_(540171, _a_(540170, models, "CharField"), max_length=100, blank=True),)
    _l_(540173)
    post_date = _c_(540175, _a_(540174, models, "DateField"))
    _l_(540176)

    class Meta:
        _l_(540178)

        db_table = "core_user_articles"
        _l_(540177)