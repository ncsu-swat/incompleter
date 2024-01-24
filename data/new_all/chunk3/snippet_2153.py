# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60983924/attributeerror-mongoalchemy-object-has-no-attribute-insert-mongodb-flask-mo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask_restplus import Api
    _l_(570222)

except ImportError:
    pass
try:
    from flask import Blueprint
    _l_(570224)

except ImportError:
    pass
try:
    from controller.essential_controller import api as essential_ns
    _l_(570226)

except ImportError:
    pass
'''from controller.author_controller import app as authors_ns'''
_l_(570227)

blueprint = _c_(570230, _n_(570228, "Blueprint", lambda: Blueprint), 'api', _n_(570229, "__name__", lambda: __name__))
_l_(570231)

api = _c_(570234, _n_(570232, "Api", lambda: Api), _n_(570233, "blueprint", lambda: blueprint),
          title='PublicVoice Backend service',
          version='0.0.1',
          description='PublicVoice Backend service'
          )
_l_(570235)

_c_(570239, _a_(570237, _n_(570236, "api", lambda: api), "add_namespace"), _n_(570238, "essential_ns", lambda: essential_ns), path='/essentials')
_l_(570240)