# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43055952/typeerror-modelbase-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from rest_framework import serializers
    _l_(466119)

except ImportError:
    pass
try:
    from offense_api.models import Season, Episode, Character
    _l_(466121)

except ImportError:
    pass


class SeasonSerializer(_a_(466123, _n_(466122, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(466132)

    episodes = _c_(466126, _a_(466125, _n_(466124, "serializers", lambda: serializers), "StringRelatedField"), many=True)
    _l_(466127)

    class Meta:
        _l_(466131)

        model = _n_(466128, "Season", lambda: Season)
        _l_(466129)
        fields = ('season_number', 'episodes')
        _l_(466130)


class EpisodeSerializer(_a_(466134, _n_(466133, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(466139)


    class Meta:
        _l_(466138)

        model = _n_(466135, "Episode", lambda: Episode)
        _l_(466136)
        fields = ('episode_number', 'episode_title', 'episode_season')
        _l_(466137)


class CharacterSerializer(_a_(466141, _n_(466140, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(466146)


    class Meta:
        _l_(466145)

        model = _n_(466142, "Character", lambda: Character)
        _l_(466143)
        fields = ('character_legal_first_name', 'character_legal_last_name', 'character_preferred_name',)
        _l_(466144)