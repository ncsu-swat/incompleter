# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57537309/typeerror-str-returned-non-string-type-magicmock
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import factory
    _l_(425395)

except ImportError:
    pass
try:
    import mock
    _l_(425397)

except ImportError:
    pass
try:
    from imagekit.signals import source_saved
    _l_(425399)

except ImportError:
    pass
try:
    from .mocks import storage_mock, image_mock
    _l_(425401)

except ImportError:
    pass
try:
    from .models import Car
    _l_(425403)

except ImportError:
    pass


@_c_(425408, _a_(425406, _a_(425405, _n_(425404, "factory", lambda: factory), "django"), "mute_signals"), _n_(425407, "source_saved", lambda: source_saved))
class CarFactory(_a_(425411, _a_(425410, _n_(425409, "factory", lambda: factory), "django"), "DjangoModelFactory")):
    _l_(425417)

    class Meta:
        _l_(425414)

        model = _n_(425412, "Car", lambda: Car)
        _l_(425413)

    image = _n_(425415, "image_mock", lambda: image_mock)
    _l_(425416)


def test_case_one(self):
    _l_(425427)

    with _c_(425421, _a_(425419, _n_(425418, "mock", lambda: mock), "patch"), 'django.core.files.storage.default_storage._wrapped', _n_(425420, "storage_mock", lambda: storage_mock)):
        _l_(425426)

        car = _c_(425424, _a_(425423, _n_(425422, "CarFactory", lambda: CarFactory), "create"))
        _l_(425425)