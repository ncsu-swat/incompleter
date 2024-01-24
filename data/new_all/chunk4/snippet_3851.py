# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66557221/typeerror-init-got-an-unexpected-keyword-argument-deon-deletefault
# -*- coding: utf-8 -*-


from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db.models.fields.related import ForeignKey
    _l_(646277)

except ImportError:
    pass
try:
    from django.contrib.auth.models import User
    _l_(646279)

except ImportError:
    pass
try:
    from datetime import *
    _l_(646281)

except ImportError:
    pass
try:
    from django.db import models
    _l_(646283)

except ImportError:
    pass
try:
    from django.dispatch import receiver
    _l_(646285)

except ImportError:
    pass
try:
    from django.db.models.signals import post_save
    _l_(646287)

except ImportError:
    pass
try:
    from taggit.managers import TaggableManager
    _l_(646289)

except ImportError:
    pass
try:
    import unicodedata
    _l_(646291)

except ImportError:
    pass

# Create your models here.
class Debate(_a_(646293, _n_(646292, "models", lambda: models), "Model")):
    _l_(646383)

    #parametros de la tabla.
    id_debate = _c_(646296, _a_(646295, _n_(646294, "models", lambda: models), "AutoField"), primary_key=True)
    _l_(646297)
    title = _c_(646300, _a_(646299, _n_(646298, "models", lambda: models), "CharField"), max_length=100)
    _l_(646301)
    text = _c_(646304, _a_(646303, _n_(646302, "models", lambda: models), "CharField"), max_length=1000, blank=True, null=True)
    _l_(646305)
    date = _c_(646309, _a_(646307, _n_(646306, "models", lambda: models), "DateField"), default=_a_(646308, datetime, "now"), blank=True)
    _l_(646310)
    end_date = _c_(646313, _a_(646312, _n_(646311, "models", lambda: models), "DateField"), default=None, blank=True, null=True)
    _l_(646314)
    owner_type = _c_(646317, _a_(646316, _n_(646315, "models", lambda: models), "CharField"), max_length=50, default='username')
    _l_(646318)
    length = _c_(646321, _a_(646320, _n_(646319, "models", lambda: models), "IntegerField"), default=300, blank=True)
    _l_(646322)
    id_user = _c_(646328, _a_(646324, _n_(646323, "models", lambda: models), "ForeignKey"), _n_(646325, "User", lambda: User),on_delete=_a_(646327, _n_(646326, "models", lambda: models), "CASCADE"))
    _l_(646329)
    state = _c_(646332, _a_(646331, _n_(646330, "models", lambda: models), "CharField"), max_length=20, default='open')
    _l_(646333)
    args_max = _c_(646336, _a_(646335, _n_(646334, "models", lambda: models), "IntegerField"), deon_deletefault=1)
    _l_(646337)
    position_max = _c_(646340, _a_(646339, _n_(646338, "models", lambda: models), "IntegerField"), default=3)
    _l_(646341)
    counterargs_max = _c_(646344, _a_(646343, _n_(646342, "models", lambda: models), "IntegerField"), default=1)
    _l_(646345)
    counterargs_type = _c_(646348, _a_(646347, _n_(646346, "models", lambda: models), "IntegerField"), default=0) # 0:ambas # 1: contraria
    _l_(646349) # 0:ambas # 1: contraria
    members_type = _c_(646352, _a_(646351, _n_(646350, "models", lambda: models), "IntegerField"), default=0) #0 debate publico
    _l_(646353) #0 debate publico
    participation_type = _c_(646356, _a_(646355, _n_(646354, "models", lambda: models), "CharField"), max_length=50, default='all')
    _l_(646357)
    img = _c_(646360, _a_(646359, _n_(646358, "models", lambda: models), "FileField"), blank=True, null=True, default="RDdefault.png")
    _l_(646361)

    tags = _c_(646363, _n_(646362, "TaggableManager", lambda: TaggableManager))
    _l_(646364)

    def __unicode__(self):
        _l_(646368)

        aux = _a_(646366, _n_(646365, "self", lambda: self), "title")
        _l_(646367)
        return aux
    def __getitem__(self, key):
        _l_(646374)

        aux = _c_(646372, _n_(646369, "getattr", lambda: getattr), _n_(646370, "self", lambda: self), _n_(646371, "key", lambda: key))
        _l_(646373)
        return aux
    def as_dict(self):
        _l_(646382)

        aux = {'text': _a_(646376, _n_(646375, "self", lambda: self), "text"), 'type':_a_(646378, _n_(646377, "self", lambda: self), "members_type"), 'id':_a_(646380, _n_(646379, "self", lambda: self), "id_debate")}
        _l_(646381)
        return aux