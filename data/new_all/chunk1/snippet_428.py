# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47784216/django-rest-framework-attributeerror-function-object-has-no-attribute-model
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from rest_framework import serializers
    _l_(413199)

except ImportError:
    pass
try:
    from .models import Developers
    _l_(413201)

except ImportError:
    pass

class DevSerializer(_a_(413203, _n_(413202, "serializers", lambda: serializers), "HyperlinkedModelSerializer")):
    _l_(413208)

    class Meta:
        _l_(413207)

        model = _n_(413204, "Developers", lambda: Developers)
        _l_(413205)
        fields = ('name', 'surname', 'skills', 'education', 'employment_history')
        _l_(413206)