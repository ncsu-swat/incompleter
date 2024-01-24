# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51946150/django-typeerror-not-supported-between-instances-model-objects
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if (_n_(409865, "dev_filter", lambda: dev_filter)!="") and (_n_(409866, "dev_filter", lambda: dev_filter)!="-1"):
    _l_(409880)

    device_list = _c_(409873, _a_(409871, _c_(409870, _a_(409869, _a_(409868, _n_(409867, "Device", lambda: Device), "objects"), "all")), "filter"), device_model = _n_(409872, "dev_filter", lambda: dev_filter))
    _l_(409874)
else:
    device_list = _c_(409878, _a_(409877, _a_(409876, _n_(409875, "Device", lambda: Device), "objects"), "all"))
    _l_(409879)

dev_status_list = []
_l_(409881)
for dev in _n_(409882, "device_list", lambda: device_list):
    _l_(409902)

    try:
        _l_(409901)

        _c_(409894, _a_(409884, _n_(409883, "dev_status_list", lambda: dev_status_list), "append"), _a_(409893, _c_(409892, _a_(409891, _c_(409890, _a_(409887, _a_(409886, _n_(409885, "DeviceTest", lambda: DeviceTest), "objects"), "filter"), device_id=_a_(409889, _n_(409888, "dev", lambda: dev), "pk")), "latest"), 'created_at'), "status"))
        _l_(409895)
    except:
        _l_(409900)

        _c_(409898, _a_(409897, _n_(409896, "dev_status_list", lambda: dev_status_list), "append"), "Not checked")
        _l_(409899)

device_list = [_n_(409903, "device_list", lambda: device_list) for (dev_status_list, device_list) in _c_(409909, _n_(409904, "sorted", lambda: sorted), _c_(409908, _n_(409905, "zip", lambda: zip), _n_(409906, "dev_status_list", lambda: dev_status_list), _n_(409907, "device_list", lambda: device_list)))]
_l_(409910)

if (_n_(409911, "order", lambda: order) == '-'):
    _l_(409916)

    _c_(409914, _a_(409913, _n_(409912, "device_list", lambda: device_list), "reverse"))
    _l_(409915)