# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60123122/typeerror-get-got-an-unexpected-keyword-argument-project-id-in-flask-applica
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Blueprint
    _l_(653778)

except ImportError:
    pass
try:
    from flask_restful import Api
    _l_(653780)

except ImportError:
    pass
try:
    from resources.Hello import Hello
    _l_(653782)

except ImportError:
    pass
try:
    from resources.Users import UserResource
    _l_(653784)

except ImportError:
    pass
try:
    from resources.Projects import ProjectResource
    _l_(653786)

except ImportError:
    pass
try:
    from resources.Actions import ActionResource
    _l_(653788)

except ImportError:
    pass

api_bp = _c_(653791, _n_(653789, "Blueprint", lambda: Blueprint), 'api', _n_(653790, "__name__", lambda: __name__))
_l_(653792)
api = _c_(653795, _n_(653793, "Api", lambda: Api), _n_(653794, "api_bp", lambda: api_bp))
_l_(653796)
# Get by id
_c_(653800, _a_(653798, _n_(653797, "api", lambda: api), "add_resource"), _n_(653799, "ProjectResource", lambda: ProjectResource), '/projects/<int:project_id>', endpoint = 'get_by_id')
_l_(653801)