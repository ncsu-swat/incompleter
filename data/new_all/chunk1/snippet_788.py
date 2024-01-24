# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51946150/django-typeerror-not-supported-between-instances-model-objects
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class DeviceModel(_a_(418196, _n_(418195, "models", lambda: models), "Model")):
    _l_(418209)

    name = _c_(418198, _a_(418197, models, "CharField"), max_length=255)
    _l_(418199)
    pirsh = _c_(418201, _a_(418200, models, "CharField"), max_length=255)
    _l_(418202)

    def __str__(self):
        _l_(418208)

        aux = _a_(418204, _n_(418203, "self", lambda: self), "name") + " - " + _a_(418206, _n_(418205, "self", lambda: self), "pirsh")
        _l_(418207)
        return aux

class Device(_a_(418211, _n_(418210, "models", lambda: models), "Model")):
    _l_(418233)

    created_at = _c_(418213, _a_(418212, models, "DateTimeField"), auto_now_add=True)
    _l_(418214)
    device_model = _c_(418218, _a_(418215, models, "ForeignKey"), _n_(418216, "DeviceModel", lambda: DeviceModel), on_delete=_a_(418217, models, "CASCADE"))
    _l_(418219)
    serial_number = _c_(418221, _a_(418220, models, "CharField"), max_length=255)
    _l_(418222)


    def __str__(self):
        _l_(418232)

        aux = _a_(418225, _a_(418224, _n_(418223, "self", lambda: self), "device_model"), "name") + " - " + _a_(418228, _a_(418227, _n_(418226, "self", lambda: self), "device_model"), "pirsh") + " - " \
                + _a_(418230, _n_(418229, "self", lambda: self), "serial_number")
        _l_(418231)
        return aux

class DeviceTest(_a_(418235, _n_(418234, "models", lambda: models), "Model")):
    _l_(418297)

    device = _c_(418239, _a_(418236, models, "ForeignKey"), _n_(418237, "Device", lambda: Device), on_delete=_a_(418238, models, "CASCADE"))
    _l_(418240)
    created_at = _c_(418242, _a_(418241, models, "DateTimeField"))
    _l_(418243)

    TEST_OK = '+'
    _l_(418244)
    TEST_ERROR = '-'
    _l_(418245)
    TEST_PENDING = '?'
    _l_(418246)
    TEST_RESULT_CHOICES = (
        (TEST_OK, 'Success'),
        (TEST_ERROR, 'Fail'),
        (TEST_PENDING, 'Not checked'),
    )
    _l_(418247)
    status = _c_(418249, _a_(418248, models, "CharField"), max_length=1, choices=TEST_RESULT_CHOICES, default=TEST_PENDING)
    _l_(418250)

    comment = _c_(418252, _a_(418251, models, "TextField"), blank=True, default="")
    _l_(418253)
    tester = _c_(418255, _a_(418254, models, "CharField"), max_length=255)
    _l_(418256)
    action = _c_(418258, _a_(418257, models, "CharField"), max_length=255)
    _l_(418259)

    def save(self, *args, **kwargs):
        _l_(418277)

        ''' On save, update timestamps '''
        _l_(418260)
        if not _a_(418262, _n_(418261, "self", lambda: self), "created_at"):
            _l_(418268)

            _n_(418263, "self", lambda: self).created_at = _c_(418266, _a_(418265, _n_(418264, "timezone", lambda: timezone), "now"))
            _l_(418267)
        aux = _c_(418275, _a_(418272, _n_(418269, "super", lambda: super)(_n_(418270, "DeviceTest", lambda: DeviceTest), _n_(418271, "self", lambda: self)), "save"), *_n_(418273, "args", lambda: args), **_n_(418274, "kwargs", lambda: kwargs))
        _l_(418276)
        return aux

    def __str__(self):
        _l_(418296)

        aux = _a_(418281, _a_(418280, _a_(418279, _n_(418278, "self", lambda: self), "device_id"), "device_model"), "name") + " - " + \
                _a_(418285, _a_(418284, _a_(418283, _n_(418282, "self", lambda: self), "device_id"), "device_model"), "pirsh") + " - " + \
                _a_(418288, _a_(418287, _n_(418286, "self", lambda: self), "device_id"), "serial_number") + " - " + \
                _c_(418292, _n_(418289, "str", lambda: str), _a_(418291, _n_(418290, "self", lambda: self), "created_at")) + " - " + \
                "Result (" + _a_(418294, _n_(418293, "self", lambda: self), "status") + ")"
        _l_(418295)
        return aux