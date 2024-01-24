# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37846721/django-typeerror-modelbase-object-is-not-iterable
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(406018)
try:
    from django.db import migrations, models
    _l_(406020)

except ImportError:
    pass


class Migration(_a_(406022, _n_(406021, "migrations", lambda: migrations), "Migration")):
    _l_(406030)


    dependencies = [
        ('reputation', '0003_auto_20160302_1749'),
    ]
    _l_(406023)

    operations = [
        _c_(406028, _a_(406025, _n_(406024, "migrations", lambda: migrations), "AlterUniqueTogether"), name='reputation',
            unique_together=_c_(406027, _n_(406026, "set", lambda: set), [('user', 'dimension')]),
        ),
    ]
    _l_(406029)