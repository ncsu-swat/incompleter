# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43055952/typeerror-modelbase-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(470355)

except ImportError:
    pass


class Season(_a_(470357, _n_(470356, "models", lambda: models), "Model")):
    _l_(470376)

    season_created = _c_(470360, _a_(470359, _n_(470358, "models", lambda: models), "DateTimeField"), auto_now_add=True)
    _l_(470361)
    season_number = _c_(470364, _a_(470363, _n_(470362, "models", lambda: models), "IntegerField"), unique=True)
    _l_(470365)

    def __unicode__(self):
        _l_(470369)

        aux = _a_(470367, _n_(470366, "self", lambda: self), "season_number")
        _l_(470368)
        return aux

    def __str__(self):
        _l_(470375)

        aux = _c_(470373, _n_(470370, "str", lambda: str), _a_(470372, _n_(470371, "self", lambda: self), "season_number"))
        _l_(470374)
        return aux


class Episode(_a_(470378, _n_(470377, "models", lambda: models), "Model")):
    _l_(470415)

    episode_season = _c_(470384, _a_(470380, _n_(470379, "models", lambda: models), "ForeignKey"), _n_(470381, "Season", lambda: Season), related_name='episodes', on_delete=_a_(470383, _n_(470382, "models", lambda: models), "CASCADE"))
    _l_(470385)
    episode_created = _c_(470388, _a_(470387, _n_(470386, "models", lambda: models), "DateTimeField"), auto_now_add=True)
    _l_(470389)
    episode_number = _c_(470392, _a_(470391, _n_(470390, "models", lambda: models), "IntegerField"))
    _l_(470393)
    episode_title = _c_(470396, _a_(470395, _n_(470394, "models", lambda: models), "CharField"), max_length=300, default='')
    _l_(470397)

    def __unicode__(self):
        _l_(470404)

        aux = '%d. %d' % (_a_(470400, _a_(470399, _n_(470398, "self", lambda: self), "episode_season"), "season_number"), _a_(470402, _n_(470401, "self", lambda: self), "episode_number"))
        _l_(470403)
        return aux

    def __str__(self):
        _l_(470411)

        aux = '%d. %d' % (_a_(470407, _a_(470406, _n_(470405, "self", lambda: self), "episode_season"), "season_number"), _a_(470409, _n_(470408, "self", lambda: self), "episode_number"))
        _l_(470410)
        return aux

    class Meta:
        _l_(470414)

        unique_together = ('episode_season', 'episode_number')
        _l_(470412)
        ordering = ('episode_number',)
        _l_(470413)


class Character(_a_(470417, _n_(470416, "models", lambda: models), "Model")):
    _l_(470444)

    character_created = _c_(470420, _a_(470419, _n_(470418, "models", lambda: models), "DateTimeField"), auto_now_add=True)
    _l_(470421)
    character_legal_first_name = _c_(470424, _a_(470423, _n_(470422, "models", lambda: models), "CharField"), max_length=50, default='', null=True)
    _l_(470425)
    character_legal_last_name = _c_(470428, _a_(470427, _n_(470426, "models", lambda: models), "CharField"), max_length=100, default='', null=True)
    _l_(470429)
    character_preferred_name = _c_(470432, _a_(470431, _n_(470430, "models", lambda: models), "CharField"), max_length=150, default='', primary_key=True)
    _l_(470433)

    def __unicode__(self):
        _l_(470437)

        aux = _a_(470435, _n_(470434, "self", lambda: self), "character_preferred_name")
        _l_(470436)
        return aux

    def __str__(self):
        _l_(470441)

        aux = _a_(470439, _n_(470438, "self", lambda: self), "character_preferred_name")
        _l_(470440)
        return aux

    class Meta:
        _l_(470443)

        ordering = ('character_preferred_name',)
        _l_(470442)