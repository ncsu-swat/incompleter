# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62628292/django-addconstraints-raises-a-typeerror-on-postgres
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
FlashNewsTypes = [
    (1, 'Race'),
    (2, 'League'),
    (3, 'Fteam')
]
_l_(393362)


class FlashNews(_a_(393364, _n_(393363, "models", lambda: models), "Model")):
    _l_(393395)


    race = _c_(393367, _a_(393365, models, "ForeignKey"), Race, on_delete=_a_(393366, models, "CASCADE"), null=True, blank=True)
    _l_(393368)
    league = _c_(393371, _a_(393369, models, "ForeignKey"), League, on_delete=_a_(393370, models, "CASCADE"), null=True, blank=True)
    _l_(393372)
    fteam = _c_(393375, _a_(393373, models, "ForeignKey"), FantasyTeam, on_delete=_a_(393374, models, "CASCADE"), null=True, blank=True)
    _l_(393376)
    type = _c_(393380, _a_(393377, models, "IntegerField"), choices=_n_(393378, "FlashNewsTypes", lambda: FlashNewsTypes), default=_n_(393379, "FlashNewsTypes", lambda: FlashNewsTypes)[0][0])
    _l_(393381)

    class Meta:
        _l_(393394)

        constraints = [
            _c_(393392, _a_(393382, models, "CheckConstraint"), name="unique_notnull_field",
                check=(
                    _c_(393385, _a_(393383, models, "Q"), type=_n_(393384, "FlashNewsTypes", lambda: FlashNewsTypes)[0][0],
                        race__isnull=False,
                        league__isnull=True,
                        fteam__isnull=True,
                    ) | _c_(393388, _a_(393386, models, "Q"), type=_n_(393387, "FlashNewsTypes", lambda: FlashNewsTypes)[1][0],
                        race__isnull=True,
                        league__isnull=False,
                        fteam__isnull=True,
                    ) | _c_(393391, _a_(393389, models, "Q"), type=_n_(393390, "FlashNewsTypes", lambda: FlashNewsTypes)[2][0],
                        race__isnull=True,
                        league__isnull=True,
                        fteam__isnull=False,
                    )
                ),
            )
        ]
        _l_(393393)