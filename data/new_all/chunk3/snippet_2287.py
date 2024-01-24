# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53260022/django-with-postgres-backend-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models as m
    _l_(571322)

except ImportError:
    pass
try:
    import django.contrib.postgres as pg
    _l_(571324)

except ImportError:
    pass

class node(_a_(571326, _n_(571325, "m", lambda: m), "Model")):
    _l_(571347)

    inputfile = _c_(571329, _a_(571328, _n_(571327, "m", lambda: m), "CharField"), max_length = 255)
    _l_(571330)
    source_id = _c_(571333, _a_(571332, _n_(571331, "m", lambda: m), "IntegerField"))
    _l_(571334)
    source_sim = _c_(571337, _a_(571336, _n_(571335, "m", lambda: m), "CharField"), max_length = 255)
    _l_(571338)
    coordinates = _c_(571345, _a_(571341, _a_(571340, _n_(571339, "pg", lambda: pg), "fields"), "ArrayField"), _c_(571344, _a_(571343, _n_(571342, "m", lambda: m), "FloatField")), size = 3)
    _l_(571346)