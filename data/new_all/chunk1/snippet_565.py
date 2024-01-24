# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37846721/django-typeerror-modelbase-object-is-not-iterable
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(390945)
try:
    from django.db import models, migrations
    _l_(390947)

except ImportError:
    pass
try:
    from django.conf import settings
    _l_(390949)

except ImportError:
    pass


class Migration(_a_(390951, _n_(390950, "migrations", lambda: migrations), "Migration")):
    _l_(390962)


    dependencies = [
        ('reputation', '0001_initial'),
    ]
    _l_(390952)

    operations = [
        _c_(390960, _a_(390954, _n_(390953, "migrations", lambda: migrations), "AlterField"), model_name='reputationaction',
            name='user',
            field=_c_(390959, _a_(390956, _n_(390955, "models", lambda: models), "ForeignKey"), to=_a_(390958, _n_(390957, "settings", lambda: settings), "AUTH_USER_MODEL"), related_name='reputation_action'),
        ),
    ]
    _l_(390961)