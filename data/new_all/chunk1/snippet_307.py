# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/16780359/nameerror-name-positivesmallintegerfield-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(410547)

except ImportError:
    pass

class Song(_a_(410549, _n_(410548, "models", lambda: models), "Model")):
    _l_(410590)

    own = _c_(410552, _a_(410551, _n_(410550, "models", lambda: models), "BooleanField"), default=True)
    _l_(410553)
    heard = _c_(410556, _a_(410555, _n_(410554, "models", lambda: models), "DateTimeField"), blank=True,null=True)
    _l_(410557)
    release_date = _c_(410560, _a_(410559, _n_(410558, "models", lambda: models), "DateField"), blank=True,null=True)
    _l_(410561)
    style = _c_(410564, _a_(410563, _n_(410562, "models", lambda: models), "CharField"), max_length=255,blank=True,null=True)
    _l_(410565)
    artist = _c_(410568, _a_(410567, _n_(410566, "models", lambda: models), "CharField"), max_length=255,blank=True,null=True)
    _l_(410569)
    featuring = _c_(410572, _a_(410571, _n_(410570, "models", lambda: models), "CharField"), max_length=255,blank=True,null=True)
    _l_(410573)
    title = _c_(410576, _a_(410575, _n_(410574, "models", lambda: models), "CharField"), max_length=255,blank=True,null=True)
    _l_(410577)
    listen = _c_(410580, _a_(410579, _n_(410578, "models", lambda: models), "URLField"), max_length=255,blank=True,null=True)
    _l_(410581)
    highest_chart_pos = _c_(410584, _a_(410583, _n_(410582, "models", lambda: models), "PositiveSmallIntegerField"))
    _l_(410585)
    note = _c_(410588, _a_(410587, _n_(410586, "models", lambda: models), "TextField"), blank=True,null=True)
    _l_(410589)