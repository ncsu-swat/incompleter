# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60123122/typeerror-get-got-an-unexpected-keyword-argument-project-id-in-flask-applica
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Blueprint
    _l_(701891)

except ImportError:
    pass
try:
    from flask_restful import Api
    _l_(701893)

except ImportError:
    pass
try:
    from resources.Hello import Hello
    _l_(701895)

except ImportError:
    pass
try:
    from resources.Users import UserResource
    _l_(701897)

except ImportError:
    pass
try:
    from resources.Projects import ProjectResource
    _l_(701899)

except ImportError:
    pass
try:
    from resources.Actions import ActionResource
    _l_(701901)

except ImportError:
    pass

api_bp = _c_(701904, _n_(701902, "Blueprint", lambda: Blueprint), 'api', _n_(701903, "__name__", lambda: __name__))
_l_(701905)
api = _c_(701908, _n_(701906, "Api", lambda: Api), _n_(701907, "api_bp", lambda: api_bp))
_l_(701909)
# Get by id
_c_(701913, _a_(701911, _n_(701910, "api", lambda: api), "add_resource"), _n_(701912, "ProjectResource", lambda: ProjectResource), '/projects/<int:project_id>', endpoint = 'get_by_id')
_l_(701914)