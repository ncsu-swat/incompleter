# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60983924/attributeerror-mongoalchemy-object-has-no-attribute-insert-mongodb-flask-mo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import request
    _l_(528049)

except ImportError:
    pass
try:
    from flask_restplus import Resource
    _l_(528051)

except ImportError:
    pass
try:
    from service import essential_service
    _l_(528053)

except ImportError:
    pass
try:
    from models.dto import dto as EssentialDto
    _l_(528055)

except ImportError:
    pass

api = _a_(528058, _a_(528057, _n_(528056, "EssentialDto", lambda: EssentialDto), "EssentialDto"), "api")
_l_(528059)
essential = _a_(528062, _a_(528061, _n_(528060, "EssentialDto", lambda: EssentialDto), "EssentialDto"), "essential")
_l_(528063)

@_c_(528066, _a_(528065, _n_(528064, "api", lambda: api), "route"), '/')
class EssentialController(_n_(528067, "Resource", lambda: Resource)):
    _l_(528099)

    @_c_(528070, _a_(528069, _n_(528068, "api", lambda: api), "doc"), 'Get all essential services')
    @_c_(528074, _a_(528072, _n_(528071, "api", lambda: api), "marshal_list_with"), _n_(528073, "essential", lambda: essential), envelope='data')
    def get(self):
        _l_(528079)

        """List all essential service"""
        aux = _c_(528077, _a_(528076, _n_(528075, "essential_service", lambda: essential_service), "get_all_service"))
        _l_(528078)
        return aux

    @_c_(528082, _a_(528081, _n_(528080, "api", lambda: api), "response"), 201, 'essential services successfully created.')
    @_c_(528085, _a_(528084, _n_(528083, "api", lambda: api), "doc"), 'create a new essential service')
    @_c_(528089, _a_(528087, _n_(528086, "api", lambda: api), "expect"), _n_(528088, "essential", lambda: essential), validate=True)
    def post(self):
        _l_(528098)

        """Creates a Essential service """
        data = _a_(528091, _n_(528090, "request", lambda: request), "json")
        _l_(528092)
        aux = _c_(528096, _a_(528094, _n_(528093, "essential_service", lambda: essential_service), "create_essential_service"), data=_n_(528095, "data", lambda: data))
        _l_(528097)
        return aux