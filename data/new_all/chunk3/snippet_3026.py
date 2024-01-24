# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53463416/django-attributeerror-int-object-has-no-attribute-save
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Profile(_a_(562428, _n_(562427, "models", lambda: models), "Model")):
    _l_(562436)

    user = _c_(562431, _a_(562429, models, "OneToOneField"), User, on_delete=_a_(562430, models, "CASCADE"))
    _l_(562432)
    total_events = _c_(562434, _a_(562433, models, "IntegerField"), default=0) 
    _l_(562435) 

class Event(_a_(562438, _n_(562437, "models", lambda: models), "Model")):
    _l_(562443)

    user = _c_(562440, _a_(562439, models, "ForeignKey"), User, related_name='seller')
    _l_(562441)
    ...
    _l_(562442)