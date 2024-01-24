# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60123122/typeerror-get-got-an-unexpected-keyword-argument-project-id-in-flask-applica
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Blueprint
    _l_(654291)

except ImportError:
    pass
try:
    from flask_restful import Api
    _l_(654293)

except ImportError:
    pass
try:
    from resources.Hello import Hello
    _l_(654295)

except ImportError:
    pass
try:
    from resources.Users import UserResource
    _l_(654297)

except ImportError:
    pass
try:
    from resources.Projects import ProjectResource
    _l_(654299)

except ImportError:
    pass
try:
    from resources.Actions import ActionResource
    _l_(654301)

except ImportError:
    pass

api_bp = _c_(654304, _n_(654302, "Blueprint", lambda: Blueprint), 'api', _n_(654303, "__name__", lambda: __name__))
_l_(654305)
api = _c_(654308, _n_(654306, "Api", lambda: Api), _n_(654307, "api_bp", lambda: api_bp))
_l_(654309)
# Get by id
_c_(654313, _a_(654311, _n_(654310, "api", lambda: api), "add_resource"), _n_(654312, "ProjectResource", lambda: ProjectResource), '/projects/<int:project_id>', endpoint = 'get_by_id')
_l_(654314)