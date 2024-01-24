# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37846721/django-typeerror-modelbase-object-is-not-iterable
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(396539)
try:
    from django.db import migrations, models
    _l_(396541)

except ImportError:
    pass


def dedupe_reputation_actions(apps, schema_editor):
    _l_(396577)

    Reputation = _c_(396544, _a_(396543, _n_(396542, "apps", lambda: apps), "get_model"), 'reputation', 'Reputation')
    _l_(396545)

    qs = _c_(396558, _a_(396557, _c_(396556, _a_(396552, _c_(396551, _a_(396550, _c_(396549, _a_(396548, _a_(396547, _n_(396546, "Reputation", lambda: Reputation), "objects"), "all")), "values"), 'user', 'dimension'), "annotate"), total=_c_(396555, _a_(396554, _n_(396553, "models", lambda: models), "Count"), 'user')), "filter"), total__gt=1)
    _l_(396559)

    for dupe in _n_(396560, "qs", lambda: qs):
        _l_(396576)

        reps = _c_(396568, _n_(396561, "list", lambda: list), _c_(396567, _a_(396564, _a_(396563, _n_(396562, "Reputation", lambda: Reputation), "objects"), "filter"), user=_n_(396565, "dupe", lambda: dupe)['user'], dimension=_n_(396566, "dupe", lambda: dupe)['dimension']))
        _l_(396569)

        for rep in _n_(396570, "reps", lambda: reps)[1:]:
            _l_(396575)

            _c_(396573, _a_(396572, _n_(396571, "rep", lambda: rep), "delete"))
            _l_(396574)


class Migration(_a_(396579, _n_(396578, "migrations", lambda: migrations), "Migration")):
    _l_(396586)


    dependencies = [
        ('reputation', '0002_auto_20151117_1108'),
    ]
    _l_(396580)

    operations = [
        _c_(396584, _a_(396582, _n_(396581, "migrations", lambda: migrations), "RunPython"), _n_(396583, "dedupe_reputation_actions", lambda: dedupe_reputation_actions))
    ]
    _l_(396585)