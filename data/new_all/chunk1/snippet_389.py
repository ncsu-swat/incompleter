# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62628292/django-addconstraints-raises-a-typeerror-on-postgres
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Migration(_a_(390269, _n_(390268, "migrations", lambda: migrations), "Migration")):
    _l_(390284)


    dependencies = [
        ('myapp', '0055_flashnews'),
    ]
    _l_(390270)

    operations = [
        _c_(390282, _a_(390271, migrations, "AddConstraint"), model_name='flashnews',
            constraint=_c_(390281, _a_(390272, models, "CheckConstraint"), check=_c_(390280, _a_(390273, models, "Q"), _c_(390275, _a_(390274, models, "Q"), ('fteam__isnull', True), ('league__isnull', True), ('race__isnull', False), ('type', 1)), _c_(390277, _a_(390276, models, "Q"), ('fteam__isnull', False), ('league__isnull', True), ('race__isnull', True), ('type', 2)), _c_(390279, _a_(390278, models, "Q"), ('fteam__isnull', True), ('league__isnull', False), ('race__isnull', True), ('type', 3)), _connector='OR'), name='%(app_label)s_%(class)s_value_matches_type'),
        ),
    ]
    _l_(390283)