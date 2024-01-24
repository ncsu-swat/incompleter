# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52695868/serializers-django-rest-framework-attributeerror-got-attributeerror-when-att
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Keyword(_a_(466148, _n_(466147, "models", lambda: models), "Model")):
    _l_(466164)

    name=_c_(466150, _a_(466149, models, "CharField"), max_length=500,unique=True)
    _l_(466151)
    image = _c_(466153, _a_(466152, models, "ImageField"), upload_to='keywords/', blank=True, null=True)
    _l_(466154)
    mood=_c_(466156, _a_(466155, models, "ManyToManyField"), Mood,blank=True)
    _l_(466157)
    def __str__(self):
        _l_(466163)

        aux = _c_(466161, _n_(466158, "str", lambda: str), _a_(466160, _n_(466159, "self", lambda: self), "name"))
        _l_(466162)
        return aux

class UserKeyword(_a_(466166, _n_(466165, "models", lambda: models), "Model")):
    _l_(466184)

    keywords=_c_(466169, _a_(466167, models, "ManyToManyField"), _n_(466168, "Keyword", lambda: Keyword))
    _l_(466170)
    count=_c_(466172, _a_(466171, models, "IntegerField"), blank=True,null=True,default=0)
    _l_(466173)
    user=_c_(466176, _a_(466174, models, "ForeignKey"), User,on_delete=_a_(466175, models, "CASCADE"))
    _l_(466177)
    def __str__(self):
        _l_(466183)

        aux = _c_(466181, _n_(466178, "str", lambda: str), _a_(466180, _n_(466179, "self", lambda: self), "id"))
        _l_(466182)
        return aux