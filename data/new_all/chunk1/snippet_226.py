# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62362926/getting-typeerror-init-missing-1-required-positional-a-rgument-on-delet
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(413210)

except ImportError:
    pass
# Create your models here.
class Topic(_a_(413212, _n_(413211, "models", lambda: models), "Model")):
    _l_(413221)

    top_name=_c_(413215, _a_(413214, _n_(413213, "models", lambda: models), "CharField"), max_length=264,unique=True)
    _l_(413216)
    def __str__(self):
        _l_(413220)

        aux = _a_(413218, _n_(413217, "self", lambda: self), "top_name")
        _l_(413219)
        return aux
class Webpage(_a_(413223, _n_(413222, "models", lambda: models), "Model")):
    _l_(413241)

    topic= _c_(413227, _a_(413225, _n_(413224, "models", lambda: models), "ForeignKey"), _n_(413226, "Topic", lambda: Topic))
    _l_(413228)
    name = _c_(413231, _a_(413230, _n_(413229, "models", lambda: models), "CharField"), max_length=264,unique=True)
    _l_(413232)
    url = _c_(413235, _a_(413234, _n_(413233, "models", lambda: models), "URLField"), unique= True)
    _l_(413236)

    def __str__(self):
        _l_(413240)

        aux = _a_(413238, _n_(413237, "self", lambda: self), "name")
        _l_(413239)
        return aux
class AccessRecord(_a_(413243, _n_(413242, "models", lambda: models), "Model")):
    _l_(413259)

    name = _c_(413247, _a_(413245, _n_(413244, "models", lambda: models), "ForeignKey"), _n_(413246, "Webpage", lambda: Webpage))
    _l_(413248)
    date = _c_(413251, _a_(413250, _n_(413249, "models", lambda: models), "DateField"))
    _l_(413252)

    def __str__(self):
        _l_(413258)

        aux = _c_(413256, _n_(413253, "str", lambda: str), _a_(413255, _n_(413254, "self", lambda: self), "date"))
        _l_(413257)
        return aux