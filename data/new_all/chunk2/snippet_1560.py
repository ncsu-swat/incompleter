# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77537701/attributeerror-activitiesclient-object-has-no-attribute-base-url
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(470169)

except ImportError:
    pass
try:
    from config import BASE_URL
    _l_(470171)

except ImportError:
    pass
try:
    from utils.request import APIRequest
    _l_(470173)

except ImportError:
    pass


class ActivitiesClient:
    _l_(470206)

    def __int__(self):
        _l_(470185)

        _c_(470176, _a_(470175, _n_(470174, "super", lambda: super)(), "__init__"))
        _l_(470177)
        _n_(470178, "self", lambda: self).base_url = _n_(470179, "BASE_URL", lambda: BASE_URL) + "Activities"
        _l_(470180)
        _n_(470181, "self", lambda: self).request = _c_(470183, _n_(470182, "APIRequest", lambda: APIRequest))
        _l_(470184)

    def create_activity(self, payload):
        _l_(470197)

        aux = _c_(470195, _a_(470188, _a_(470187, _n_(470186, "self", lambda: self), "request"), "post_request"), _a_(470190, _n_(470189, "self", lambda: self), "base_url"), _c_(470194, _a_(470192, _n_(470191, "json", lambda: json), "dumps"), _n_(470193, "payload", lambda: payload)))
        _l_(470196)
        return aux

    def get_all_activities(self):
        _l_(470205)

        aux = _c_(470203, _a_(470200, _c_(470199, _n_(470198, "APIRequest", lambda: APIRequest)), "get_request"), _a_(470202, _n_(470201, "self", lambda: self), "base_url"))
        _l_(470204)
        # return self.request.get_request(self.base_url)
        return aux


_c_(470212, _n_(470207, "print", lambda: print), _c_(470211, _a_(470210, _c_(470209, _n_(470208, "ActivitiesClient", lambda: ActivitiesClient)), "get_all_activities")))
_l_(470213)