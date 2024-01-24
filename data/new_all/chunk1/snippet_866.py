# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58683181/django-rest-framework-authentication-permissions-error-typeerror-str-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Drone(_a_(404698, _n_(404697, "models", lambda: models), "Model")):
    _l_(404725)

    name = _c_(404700, _a_(404699, models, "CharField"), max_length=250,
                            unique=True)
    _l_(404701)
    drone_category = _c_(404704, _a_(404702, models, "ForeignKey"), DroneCategory,
                                       related_name='drones',
                                       on_delete=_a_(404703, models, "CASCADE"))
    _l_(404705)
    manufacturing_date = _c_(404707, _a_(404706, models, "DateTimeField"))
    _l_(404708)
    has_it_competed = _c_(404710, _a_(404709, models, "BooleanField"), default=False)
    _l_(404711)
    inserted_timestamp = _c_(404713, _a_(404712, models, "DateTimeField"), auto_now_add=True)
    _l_(404714)
    owner = _c_(404717, _a_(404715, models, "ForeignKey"), 'auth.User',
        related_name='drones',
        on_delete=_a_(404716, models, "CASCADE"))
    _l_(404718)

    class Meta:
        _l_(404720)

        ordering = ('name',)
        _l_(404719)

    def __str__(self):
        _l_(404724)

        aux = _a_(404722, _n_(404721, "self", lambda: self), "name")
        _l_(404723)
        return aux