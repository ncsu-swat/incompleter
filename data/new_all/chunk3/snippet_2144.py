# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61365330/celery-running-signature-from-database-attributeerror-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(532989)

except ImportError:
    pass
try:
    from celery.canvas import Signature
    _l_(532991)

except ImportError:
    pass
flatten = _a_(532996, _c_(532995, _a_(532994, _a_(532993, _n_(532992, "jsonpickle", lambda: jsonpickle), "pickler"), "Pickler")), "flatten")
_l_(532997)
restore = _a_(533002, _c_(533001, _a_(533000, _a_(532999, _n_(532998, "jsonpickle", lambda: jsonpickle), "unpickler"), "Unpickler")), "restore")
_l_(533003)

def signature_dumps(obj: _n_(533004, "Signature", lambda: Signature)) -> _n_(533005, "str", lambda: str):
    _l_(533013)

    """
    Serialize celery signature object to string
    :param obj: celery.canvas:Signature
    :return: str
    """
    aux = _c_(533011, _a_(533007, _n_(533006, "json", lambda: json), "dumps"), _c_(533010, _n_(533008, "flatten", lambda: flatten), _n_(533009, "obj", lambda: obj)), indent=2)
    _l_(533012)
    return aux


def signature_loads(s: _n_(533014, "str", lambda: str)) -> _n_(533015, "Signature", lambda: Signature):
    _l_(533023)

    """
    Create celery signature object from string value
    :param s: string representation of signature
    :return: celery.canvas:Signature object
    """
    aux = _c_(533021, _n_(533016, "restore", lambda: restore), _c_(533020, _a_(533018, _n_(533017, "json", lambda: json), "loads"), _n_(533019, "s", lambda: s)))
    _l_(533022)
    return aux