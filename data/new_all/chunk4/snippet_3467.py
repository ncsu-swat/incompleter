# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73842091/attribute-error-object-has-no-attributes-while-trying-to-update-the-manytoo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class WatchList(_a_(596250, _n_(596249, "models", lambda: models), "Model")):
    _l_(596271)

    title = _c_(596252, _a_(596251, models, "CharField"), max_length=50)
    _l_(596253)
    storyline = _c_(596255, _a_(596254, models, "CharField"), max_length=200)
    _l_(596256)
    platform = _c_(596259, _a_(596257, models, "ForeignKey"), StreamPlatform, on_delete=_a_(596258, models, "CASCADE"), related_name="watchlist")
    _l_(596260)
    active = _c_(596262, _a_(596261, models, "BooleanField"), default=True)
    _l_(596263)
    created = _c_(596265, _a_(596264, models, "DateTimeField"), auto_now_add=True)
    _l_(596266)

    def __str__(self):
        _l_(596270)

        aux = _a_(596268, _n_(596267, "self", lambda: self), "title")
        _l_(596269)
        return aux


class Review(_a_(596273, _n_(596272, "models", lambda: models), "Model")):
    _l_(596310)

    username = _c_(596276, _a_(596274, models, "ForeignKey"), User, on_delete=_a_(596275, models, "CASCADE"))
    _l_(596277)
    rating = _c_(596281, _a_(596278, models, "PositiveIntegerField"), validators = [_c_(596279, MinValueValidator, 1), _c_(596280, MaxValueValidator, 5)])
    _l_(596282)
    comment = _c_(596284, _a_(596283, models, "CharField"), max_length=200, null=True)
    _l_(596285)
    watchlist = _c_(596289, _a_(596286, models, "ForeignKey"), _n_(596287, "WatchList", lambda: WatchList), on_delete=_a_(596288, models, "CASCADE"), related_name="reviews")
    _l_(596290)
    avg_rating = _c_(596292, _a_(596291, models, "FloatField"), default=0)
    _l_(596293)
    num_rating = _c_(596295, _a_(596294, models, "IntegerField"), default=0)
    _l_(596296)
    active = _c_(596298, _a_(596297, models, "BooleanField"), default=True)
    _l_(596299)
    created = _c_(596301, _a_(596300, models, "DateTimeField"), auto_now_add=True)
    _l_(596302)
    updated = _c_(596304, _a_(596303, models, "DateTimeField"), auto_now=True)
    _l_(596305)

    def __str__(self):
        _l_(596309)

        aux = _a_(596307, _n_(596306, "self", lambda: self), "comment")
        _l_(596308)
        return aux