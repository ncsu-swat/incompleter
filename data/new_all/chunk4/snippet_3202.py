# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77422709/django-attributeerror-type-object-has-no-attribute-meta
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import django_filters
    _l_(607800)

except ImportError:
    pass
try:
    from .models import AppUserManager
    _l_(607802)

except ImportError:
    pass

class AppUserManagerFilter(_a_(607804, _n_(607803, "django_filters", lambda: django_filters), "FilterSet")):
    _l_(607809)

    class Meta:
        _l_(607808)

        model = _n_(607805, "AppUserManager", lambda: AppUserManager)
        _l_(607806)
        fields = {
            'email': ['exact', 'icontains'],
            'is_superuser': ['exact'],
            'is_staff': ['exact'],
            'is_active': ['exact'],
        }
        _l_(607807)