# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76359431/typeerror-in-django-float-argument-must-be-a-string-or-a-number-not-tuple
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Order(_a_(465807, _n_(465806, "models", lambda: models), "Model")):
    _l_(465828)


    coin = _c_(465809, _a_(465808, models, "CharField"), max_length=100)
    _l_(465810)
    symbol = _c_(465812, _a_(465811, models, "CharField"), max_length=50)
    _l_(465813)
    bought_price = _c_(465815, _a_(465814, models, "FloatField"))
    _l_(465816)
    quantity = _c_(465818, _a_(465817, models, "IntegerField"), default=1)
    _l_(465819)
    bought_at = _c_(465822, _a_(465820, models, "DateTimeField"), default=_a_(465821, datetime, "now"))
    _l_(465823)
    user = _c_(465826, _a_(465824, models, "ForeignKey"), User, on_delete=_a_(465825, models, "CASCADE"))
    _l_(465827)