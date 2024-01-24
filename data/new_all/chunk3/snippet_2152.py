# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60983924/attributeerror-mongoalchemy-object-has-no-attribute-insert-mongodb-flask-mo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from database.db import mongododb
    _l_(578704)

except ImportError:
    pass
try:
    from database.db import Location
    _l_(578706)

except ImportError:
    pass
try:
    from database.db import Essential
    _l_(578708)

except ImportError:
    pass

def create_essential_service(data):
    _l_(578722)

    _c_(578711, _n_(578709, "print", lambda: print), 'data =', _n_(578710, "data", lambda: data))
    _l_(578712)
    essentialData = _c_(578716, _n_(578713, "Essential", lambda: Essential), subscriberName=_n_(578714, "data", lambda: data)['subscriberName'],
    mobileNumber=_n_(578715, "data", lambda: data)['mobileNumber'])
    _l_(578717)

    _c_(578720, _a_(578719, _n_(578718, "essentialData", lambda: essentialData), "save"))
    _l_(578721)


def get_all_service():
    _l_(578732)

    aux = _c_(578730, _a_(578729, _c_(578728, _a_(578725, _a_(578724, _n_(578723, "Essential", lambda: Essential), "query"), "filter"), _a_(578727, _n_(578726, "Essential", lambda: Essential), "serviceType") == 'PoliceService'), "first"))
    _l_(578731)
    return aux

def get_by_service_type(serviceType):
    _l_(578741)

    aux = _c_(578739, _a_(578738, _c_(578737, _a_(578735, _a_(578734, _n_(578733, "Essential", lambda: Essential), "query"), "filter_by"), serviceType=_n_(578736, "serviceType", lambda: serviceType)), "first"))
    _l_(578740)
    return aux