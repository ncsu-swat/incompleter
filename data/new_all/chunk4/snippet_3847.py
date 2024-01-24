# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66557221/typeerror-init-got-an-unexpected-keyword-argument-deon-deletefault
# -*- coding: utf-8 -*-


from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db.models.fields.related import ForeignKey
    _l_(594491)

except ImportError:
    pass
try:
    from django.contrib.auth.models import User
    _l_(594493)

except ImportError:
    pass
try:
    from datetime import *
    _l_(594495)

except ImportError:
    pass
try:
    from django.db import models
    _l_(594497)

except ImportError:
    pass
try:
    from django.dispatch import receiver
    _l_(594499)

except ImportError:
    pass
try:
    from django.db.models.signals import post_save
    _l_(594501)

except ImportError:
    pass
try:
    from taggit.managers import TaggableManager
    _l_(594503)

except ImportError:
    pass
try:
    import unicodedata
    _l_(594505)

except ImportError:
    pass

# Create your models here.
class Debate(_a_(594507, _n_(594506, "models", lambda: models), "Model")):
    _l_(594597)

    #parametros de la tabla.
    id_debate = _c_(594510, _a_(594509, _n_(594508, "models", lambda: models), "AutoField"), primary_key=True)
    _l_(594511)
    title = _c_(594514, _a_(594513, _n_(594512, "models", lambda: models), "CharField"), max_length=100)
    _l_(594515)
    text = _c_(594518, _a_(594517, _n_(594516, "models", lambda: models), "CharField"), max_length=1000, blank=True, null=True)
    _l_(594519)
    date = _c_(594523, _a_(594521, _n_(594520, "models", lambda: models), "DateField"), default=_a_(594522, datetime, "now"), blank=True)
    _l_(594524)
    end_date = _c_(594527, _a_(594526, _n_(594525, "models", lambda: models), "DateField"), default=None, blank=True, null=True)
    _l_(594528)
    owner_type = _c_(594531, _a_(594530, _n_(594529, "models", lambda: models), "CharField"), max_length=50, default='username')
    _l_(594532)
    length = _c_(594535, _a_(594534, _n_(594533, "models", lambda: models), "IntegerField"), default=300, blank=True)
    _l_(594536)
    id_user = _c_(594542, _a_(594538, _n_(594537, "models", lambda: models), "ForeignKey"), _n_(594539, "User", lambda: User),on_delete=_a_(594541, _n_(594540, "models", lambda: models), "CASCADE"))
    _l_(594543)
    state = _c_(594546, _a_(594545, _n_(594544, "models", lambda: models), "CharField"), max_length=20, default='open')
    _l_(594547)
    args_max = _c_(594550, _a_(594549, _n_(594548, "models", lambda: models), "IntegerField"), deon_deletefault=1)
    _l_(594551)
    position_max = _c_(594554, _a_(594553, _n_(594552, "models", lambda: models), "IntegerField"), default=3)
    _l_(594555)
    counterargs_max = _c_(594558, _a_(594557, _n_(594556, "models", lambda: models), "IntegerField"), default=1)
    _l_(594559)
    counterargs_type = _c_(594562, _a_(594561, _n_(594560, "models", lambda: models), "IntegerField"), default=0) # 0:ambas # 1: contraria
    _l_(594563) # 0:ambas # 1: contraria
    members_type = _c_(594566, _a_(594565, _n_(594564, "models", lambda: models), "IntegerField"), default=0) #0 debate publico
    _l_(594567) #0 debate publico
    participation_type = _c_(594570, _a_(594569, _n_(594568, "models", lambda: models), "CharField"), max_length=50, default='all')
    _l_(594571)
    img = _c_(594574, _a_(594573, _n_(594572, "models", lambda: models), "FileField"), blank=True, null=True, default="RDdefault.png")
    _l_(594575)

    tags = _c_(594577, _n_(594576, "TaggableManager", lambda: TaggableManager))
    _l_(594578)

    def __unicode__(self):
        _l_(594582)

        aux = _a_(594580, _n_(594579, "self", lambda: self), "title")
        _l_(594581)
        return aux
    def __getitem__(self, key):
        _l_(594588)

        aux = _c_(594586, _n_(594583, "getattr", lambda: getattr), _n_(594584, "self", lambda: self), _n_(594585, "key", lambda: key))
        _l_(594587)
        return aux
    def as_dict(self):
        _l_(594596)

        aux = {'text': _a_(594590, _n_(594589, "self", lambda: self), "text"), 'type':_a_(594592, _n_(594591, "self", lambda: self), "members_type"), 'id':_a_(594594, _n_(594593, "self", lambda: self), "id_debate")}
        _l_(594595)
        return aux