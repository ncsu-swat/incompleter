# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52695868/serializers-django-rest-framework-attributeerror-got-attributeerror-when-att
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class KeywordsSerializer(_a_(431164, _n_(431163, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(431168)

    class Meta:
        _l_(431167)

        model = Keyword
        _l_(431165)
        fields ='__all__'
        _l_(431166)

class UserKeywordSerializer(_a_(431170, _n_(431169, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(431177)

    keywords = _c_(431172, _n_(431171, "KeywordsSerializer", lambda: KeywordsSerializer), read_only=True,many=True)
    _l_(431173)

    class Meta:
        _l_(431176)

        model = UserKeyword
        _l_(431174)
        fields = '__all__'
        _l_(431175)