# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52675510/attributeerror-settings-object-has-no-attribute-auth-user-model-value-after
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Vote(_a_(416967, _n_(416966, "models", lambda: models), "Model")):
    _l_(416986)


    rate_type = _c_(416969, _a_(416968, models, "BooleanField"))
    _l_(416970)
    question = _c_(416973, _a_(416971, models, "ForeignKey"), "Question", related_name='question_rate', on_delete=_a_(416972, models, "PROTECT"))
    _l_(416974)
    answer = _c_(416977, _a_(416975, models, "ForeignKey"), "Answer", related_name='answer_rate', on_delete=_a_(416976, models, "PROTECT"))
    _l_(416978)
    user = _c_(416982, _a_(416979, models, "ForeignKey"), _c_(416980, get_user_model), on_delete=_a_(416981, models, "PROTECT"))
    _l_(416983)


    class Meta:
        _l_(416985)

        unique_together = [('question', 'user'), ('answer', 'user'), ]
        _l_(416984)