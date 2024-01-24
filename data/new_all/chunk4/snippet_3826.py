# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67015173/django-rest-api-attributeerror-the-serializer-field-might-be-named-incorrectly
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from rest_framework import serializers
    _l_(590981)

except ImportError:
    pass

class ConstituentNameLists(_a_(590983, _n_(590982, "serializers", lambda: serializers), "Serializer")):
    _l_(590992)

    '''
    Returns Index Constituents
    '''
    _l_(590984)
    strings = _c_(590990, _a_(590986, _n_(590985, "serializers", lambda: serializers), "ListField"), child = _c_(590989, _a_(590988, _n_(590987, "serializers", lambda: serializers), "CharField"), max_length=100)
    )
    _l_(590991)